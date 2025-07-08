from machine import Pin
import time

# Configuration du L298N
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(20, Pin.OUT)
IN4 = Pin(21, Pin.OUT)
IN5 = Pin(10, Pin.OUT)
IN6 = Pin(11, Pin.OUT)
IN7 = Pin(12, Pin.OUT)
IN8 = Pin(13, Pin.OUT)

# Fonction pour activer la pompe 1
def activer_pompe1():
    IN1.value(1)
    IN2.value(0)
    IN5.value(1)
    IN6.value(0)

# Fonction pour activer la pompe 2
def activer_pompe2():
    IN3.value(0)
    IN4.value(1)
    IN7.value(0)
    IN8.value(1)

# Fonction pour arrêter toutes les pompes
def arreter_pompes():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    IN5.value(0)
    IN6.value(0)
    IN7.value(0)
    IN8.value(0)

# Lancement d'une pompe spécifique
def run_pump(pump_id, duration):
    print("lauched")
    print(activer_pompe1)
    print(activer_pompe2)
    print(f"→ run_pump appelée avec pump_id={pump_id}, duration={duration}")
    if pump_id == 1:
        activer_pompe1()
    elif pump_id == 2:
        activer_pompe2()
    else:
        print("Pompe non supportée")
        return
    time.sleep(3)
    arreter_pompes()
