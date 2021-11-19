import cayenne.client
import time
from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "169.254.115.30"
SERVER_PORT = 502

MQTT_USERNAME  = "91482850-734e-11ea-8221-599f77add412"
MQTT_PASSWORD  = "bf1f3bc3546894785a7b07ef6492b6b32eb4b4af"
MQTT_CLIENT_ID = "86f72a70-74d6-11ea-9915-d7baa233c5cd"

c = ModbusClient()

c.host(SERVER_HOST)
c.port(SERVER_PORT)

def on_message(message):
  print("message received: " + str(message))
  
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


  
while True:
    client.loop()
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
            
    # if open() is ok, read register (modbus function 0x03)
    if c.is_open():
        # read 10 registers at address 0, store result in regs list
        regs = c.read_holding_registers(4, 1)
        client.celsiusWrite(1, regs)
        # if success display registers
        if regs:
            print("reg ad #0 to 9: "+str(regs))

    # sleep 2s before next polling
    time.sleep(2)
    