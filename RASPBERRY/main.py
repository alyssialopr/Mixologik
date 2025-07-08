import network
import socket
import utime
import time
import ujson
from machine import Pin

# ––– 1. Connexion Wi‑Fi –––
ssid = 'PoleDeVinci_Private'
password = 'Creatvive_Lab_2024'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Connexion en cours…")
while not wlan.isconnected():
    utime.sleep(1)
print("Connecté, IP =", wlan.ifconfig()[0])

# ––– 2. Recettes cocktails –––
recipes = {
    'mango': [(1, 5) (3, 1)],
    'golden': [(1, 2), (2, 2)],
    'mangueSour': [(2, 3), (1, 1)],
    'rum': [(1, 3), (1, 1)],
}

recette_en_attente = []

# ––– 3. Configuration GPIO pompes –––
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(20, Pin.OUT)
IN4 = Pin(21, Pin.OUT)
IN5 = Pin(10, Pin.OUT)
IN6 = Pin(11, Pin.OUT)
IN7 = Pin(12, Pin.OUT)
IN8 = Pin(13, Pin.OUT)

def activer_pompe1():
    IN1.value(1)
    IN2.value(0)

def activer_pompe2():
    IN3.value(0)
    IN4.value(1)

def activer_pompe3():
    IN5.value(1)
    IN6.value(0)

def activer_pompe4():    
    IN7.value(0)
    IN8.value(1)

def arreter_pompes():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    IN5.value(0)
    IN6.value(0)
    IN7.value(0)
    IN8.value(0)

def run_pump(pump_id, duration):
    print(f"→ run_pump appelée avec pump_id={pump_id}, duration={duration}")
    if pump_id == 1:
        activer_pompe1()
    elif pump_id == 2:
        activer_pompe2()
    elif pump_id == 3:
        activer_pompe3()
    elif pump_id == 4:
        activer_pompe4()
    
    else:
        print("Pompes non supportées")
        return
    time.sleep(duration)
    arreter_pompes()
    


# ––– 4. Lancer une recette au bouton –––
def lancer_recette(pin):
    global recette_en_attente
    if recette_en_attente:
        print("Lancement de la recette via le bouton")
        for pump_id, duration in recette_en_attente:
            run_pump(pump_id, duration)
        recette_en_attente = []
    else:
        print("Aucune recette en attente")

# ––– 5. Configuration du bouton –––
bouton = Pin(1, Pin.IN, Pin.PULL_UP)
bouton.irq(trigger=Pin.IRQ_FALLING, handler=lancer_recette)

# ––– 6. Serveur HTTP –––
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
try:
    s.bind(addr)
except OSError as e:
    print("Erreur socket :", e)
    s.close()
    raise

s.listen(1)
print('Serveur HTTP en écoute sur', addr)

while True:
    client, addr = s.accept()
    req = client.recv(1024).decode()
    path = req.split('\r\n')[0].split(' ')[1]

    if path.startswith('/dispense'):
        try:
            name = path.split('=')[1]
            if name in recipes:
                recette_en_attente = recipes[name]
                resp = ujson.dumps({'status': 'ready', 'message': f'Cocktail {name} prêt, appuie sur le bouton'})
            else:
                resp = ujson.dumps({'status': 'error', 'error': 'Cocktail inconnu'})
        except Exception as e:
            resp = ujson.dumps({'status':'error', 'error': str(e)})

        header = (
            'HTTP/1.1 200 OK\r\n'
            'Content-Type: application/json\r\n'
            'Access-Control-Allow-Origin: *\r\n'
            'Access-Control-Allow-Methods: GET\r\n'
            '\r\n'
        )
        client.send(header + resp)

    else:
        file_path = path.lstrip('/') or 'index.html'
        try:
            with open(file_path) as f:
                content = f.read()
            if file_path.endswith('.css'):
                ctype = 'text/css'
            elif file_path.endswith('.js'):
                ctype = 'application/javascript'
            else:
                ctype = 'text/html'
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {ctype}\r\n\r\n'
            client.send(header + content)
        except:
            client.send('HTTP/1.1 404 Not Found\r\n\r\nNot found')

    client.close()
    utime.sleep(0.1)