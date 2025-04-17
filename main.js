async function connectToPico() {
    try {
        const device = await navigator.bluetooth.requestDevice({
            acceptAllDevices: true,
            optionalServices: ['battery_service'] // Remplace par ton service GATT
        });

        const server = await device.gatt.connect();
        console.log("Connecté à la Pico W !");
        
        const service = await server.getPrimaryService('battery_service');
        const characteristic = await service.getCharacteristic('battery_level');

        const value = await characteristic.readValue();
        console.log("Valeur reçue :", value.getUint8(0));
    } catch (error) {
        console.error("Erreur de connexion Bluetooth :", error);
    }
}