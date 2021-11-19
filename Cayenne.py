import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "91482850-734e-11ea-8221-599f77add412"
MQTT_PASSWORD  = "bf1f3bc3546894785a7b07ef6492b6b32eb4b4af"
MQTT_CLIENT_ID = "86f72a70-74d6-11ea-9915-d7baa233c5cd"

# The callback for when a message is received from Cayenne.
def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

i=0
timestamp = 0

while True:
  client.loop()

  if (time.time() > timestamp + 10):
    client.celsiusWrite(1, i)
    client.luxWrite(2, i*10)
    client.hectoPascalWrite(3, i+800)
    timestamp = time.time()
    i = i+5