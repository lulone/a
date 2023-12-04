def sendDistanceWhenHumanPresence():
    global distance
    if Environment.PIR(DigitalPin.P2):
        distance = sonar.ping(DigitalPin.P10, DigitalPin.P13, PingUnit.CENTIMETERS)
        serial.write_string("!1:PIR:" + str(distance) + "#")
    else:
        serial.write_string("!1:PIR:" + str(0) + "#")
def sendTempNHumiToGateway():
    global DHT20_CYCLE
    DHT20_CYCLE += 1
    if DHT20_CYCLE == 30:
        DHT20_CYCLE = 0
        dht11_dht22.query_data(DHTtype.DHT22, DigitalPin.P3, True, False, False)
        if dht11_dht22.read_data_successful():
            serial.write_string("!1:HUMI:" + str(dht11_dht22.read_data(dataType.HUMIDITY)) + "#")
            basic.pause(100)
            serial.write_string("!1:TEMP:" + str(dht11_dht22.read_data(dataType.TEMPERATURE)) + "#")
distance = 0
DHT20_CYCLE = 0
basic.show_string("DA")
DHT20_CYCLE = 0

def on_forever():
    sendTempNHumiToGateway()
    sendDistanceWhenHumanPresence()
    basic.pause(1000)
basic.forever(on_forever)
