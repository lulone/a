function sendDistanceWhenHumanPresence () {
    if (Environment.PIR(DigitalPin.P2)) {
        distance = sonar.ping(
        DigitalPin.P10,
        DigitalPin.P13,
        PingUnit.Centimeters
        )
        serial.writeString("!1:PIR:" + distance + "#")
    } else {
        serial.writeString("!1:PIR:" + 0 + "#")
    }
}
function sendTempNHumiToGateway () {
    DHT20_CYCLE += 1
    if (DHT20_CYCLE == 30) {
        DHT20_CYCLE = 0
        dht11_dht22.queryData(
        DHTtype.DHT22,
        DigitalPin.P3,
        true,
        false,
        false
        )
        if (dht11_dht22.readDataSuccessful()) {
            serial.writeString("!1:HUMI:" + dht11_dht22.readData(dataType.humidity) + "#")
            basic.pause(100)
            serial.writeString("!1:TEMP:" + dht11_dht22.readData(dataType.temperature) + "#")
        }
    }
}
let distance = 0
let DHT20_CYCLE = 0
basic.showString("DA")
DHT20_CYCLE = 0
basic.forever(function () {
    sendTempNHumiToGateway()
    sendDistanceWhenHumanPresence()
    basic.pause(1000)
})
