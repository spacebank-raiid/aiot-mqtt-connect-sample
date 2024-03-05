import paho.mqtt.client as mqtt

# 연결 성공 콜백
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        print("Connected with result code " + str(reason_code))
        client.subscribe("mqtt/test")
        print("mqtt/test subscribed")

# 메시지 수신 콜백
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 콜백 함수 지정
client.on_connect = on_connect
client.on_message = on_message

# 연결 설정
client.tls_set()
client.connect("search.raiid.ai", 8883, 60)

# 메시지 발행
client.publish("mqtt/test", payload="Hello World", qos=0)

client.loop_forever()
