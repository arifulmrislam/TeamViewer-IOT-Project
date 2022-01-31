# TeamViewer-IOT-Project
# `TeamViewer IoT Solution`

`Putty and MQTT Broker:`

1.Download and Install Putty software.
```
  https://www.putty.org/
```

2.Enable SSH on Raspberry Pi.

3.Set the IP address and Subnet Mask in the same network.

4.Open Putty and Connect with Raspberry Pi.

5.Install
  ```
  Paho Mqtt broker to Rasberry pi”
```
```
  http://www.steves-internet-guide.com/into-mqtt-python-client/
```

6. `sudo pip install paho-mqtt` in Putty 

Add Device and TeamViewer Agent:

1.Open TeamViewer-IoT-Management console.

2.Sign-up and take security by third-party apps (youraccount@gmail.com /P1).

3.Add device,

  -	Select device 
  -	Select my computer 
  -	Copy the command and paste to Putty

4.Restart your agent. 

5.Click to connect the device.

6.Open TeamViewer desktop and connect and login.

7.Log in to your Raspberry Pi from the Remote console of TV (TeamViewer IoT).

8.Copy and paste the Agent command through a remote console.

9.Restart your agent again.

10.Again, open your remote console and remote apps.

11.Create your Client, Sensor and Metric.

12.Go to your Dashboard (Any application) and create your Metric value display widget.

13.On try it put an integer value and push.

14.Download the sample python code and copy and paste it to the raspberry pi.

15.Open the sample file change the value and run the script, it will push the value.
(If the python program does not work, we should change pip number, like pip2, pip3)

DHT11 and TeamViewer:

1.Download and install Adafruit to your Raspberry Pi.

2.To update: 

  “sudo apt-get update”

3.Python library for dependency: 

  “sudo apt-get install python-dev”
  -	git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  -	cd Adafruit_Python_DHT
  -	sudo python2 setup.py install
  -	sudo python3 setup.py install
  -	CD to Example folder and change DHT11 and PIN as well
  -	Run “python sample.py” to get the value

4.Paste the Adafruit code to the script of the sample python code of TV (TeamViewer IoT).

5.Instead of value in Push function link the global variable of Adafruit. Boom...!!

MODBUS TCP server Simulator and TeamViewer:

1.Run Node-Red.

2.Install Modbus-TCP Node and setup.

3.Install Python shell in node to change the data of Python Shell (put the link of python shell of TV).

4.Get the data by MODBUS TCP node and convert the data into INTEGER by below Code to Function Node (Node-Red).

  -	let pay = msg.payload;
  -	const buf = Buffer.allocUnsafe(4); // (4) is ok
  -	buf.writeUInt16BE(pay[0]); // high byte
  -	msg.payload = buf.readInt16BE();
  -	return msg;

5.Write below code to Python shell,

  -	Import sys
  -	Varaiable= int(sys.argv[1]);

6.Then sent the data from MODBUS server Simulator (Easy Modbus server simulator) to Python shell of TV to push.

🚩 Connect with me on social
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/ariful-islam-arif-2987b51a3/)
- Twitter: [Twitter](https://twitter.com/arifulislam301)
- Instagram: [Instagram](https://www.instagram.com/ariful_mr_islam/)

🔔 Subscribe to my YouTube channel: [YouTube](https://www.youtube.com/channel/UCED68cm6nHaAlAk0h9I3yAQ)


