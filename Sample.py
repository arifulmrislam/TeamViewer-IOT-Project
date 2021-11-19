import json
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import Adafruit_DHT
import sys

tv_iot_api_version = "v1.0"
host = "localhost"
port = 18884
global Arif 

client_id = "84ae8bdf039748f7a823563d71272f81"
sensor_id = "31405bac1d89444988ddc3c9234a62e6"
sensor = Adafruit_DHT.DHT11
pin = 4


tls = {'certfile': "./cert.crt",
       'keyfile': "./priv_key.key",
       'ca_certs': "./TeamViewerAuthority.crt"}

def getdata():
    global Arif 
    Arif = 400
    print(Arif)

def push_data():
    global Arif
    #Replace metric values with your real sensor data.
    VAL_TEMPERATURE = int(sys.argv[1]);

    mqtt_topic_push_data = "/" + tv_iot_api_version + "/" + client_id + "/sensor/" + sensor_id 
    metrics_temp = {'metrics': [{"value":VAL_TEMPERATURE, "metricId": "724a01015dcb46a081cf679d232486a1"}]}
    msgs = []
    msgs.append({'topic': mqtt_topic_push_data, 'payload': json.dumps(metrics_temp)})
    try:
        publish.multiple(msgs, hostname=host, port=port, tls=tls)
    except Exception as e:
        print(str(e))



try:
    
    getdata()
    push_data()

except KeyboardInterrupt:
    print ("stopping")
    
