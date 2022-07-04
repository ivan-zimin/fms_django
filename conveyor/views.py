import requests
from django.shortcuts import render
import paho.mqtt.client as mqtt
import ssl

sensor_0 = None
sensor_1 = None
sensor_2 = None
sensor_3 = None


def fms_subscribe():
    conv = mqtt.Client(client_id="arefkga74np0lpbahno4")

    conv.tls_set(ca_certs="/Users/ivan/Desktop/rootCA.crt",
                 certfile="/Users/ivan/Desktop/cert.pem",
                 keyfile="/Users/ivan/Desktop/key.pem",
                 cert_reqs=ssl.CERT_REQUIRED,
                 tls_version=ssl.PROTOCOL_TLSv1_2)

    conv.connect("mqtt.cloud.yandex.net", port=8883, keepalive=5)

    def subscribe(client: conv):
        def on_message(client, userdata, msg):
            if msg.topic == '$devices/arefkga74np0lpbahno4/state/sensor_0':
                global sensor_0
                sensor_0 = msg.payload.decode()
            if msg.topic == '$devices/arefkga74np0lpbahno4/state/sensor_1':
                global sensor_1
                sensor_1 = msg.payload.decode()
            if msg.topic == '$devices/arefkga74np0lpbahno4/state/sensor_2':
                global sensor_2
                sensor_2 = msg.payload.decode()
            if msg.topic == '$devices/arefkga74np0lpbahno4/state/sensor_3':
                global sensor_3
                sensor_3 = msg.payload.decode()

        client.subscribe('$devices/arefkga74np0lpbahno4/state/sensor_0')
        client.subscribe('$devices/arefkga74np0lpbahno4/state/sensor_1')
        client.subscribe('$devices/arefkga74np0lpbahno4/state/sensor_2')
        client.subscribe('$devices/arefkga74np0lpbahno4/state/sensor_3')

        client.on_message = on_message

    subscribe(conv)
    conv.loop_start()


def main_page(request):

    fms_subscribe()
    config_json = 'https://storage.yandexcloud.net/fms-file-bucket/config.json'
    config_info = requests.get(config_json).json()

    context = {
        "sensor_0": sensor_0,
        "sensor_1": sensor_1,
        "sensor_2": sensor_2,
        "sensor_3": sensor_3,
        "lock_0": config_info["0"],
        "lock_1": config_info["1"],
        "lock_2": config_info["2"],
        "lock_3": config_info["3"],
        "belt": config_info["4"],
    }
    return render(request, 'conveyor/index.html', context)
