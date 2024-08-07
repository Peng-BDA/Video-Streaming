#
# Copyright 2021 HiveMQ GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time
import paho.mqtt.client as paho
from paho import mqtt
import binascii
import serial

# Config serial port
ser = serial.Serial("/dev/ttyAMA0", 9600)
driverHorizonDegree = 0
driverVerticalDegree = 0

def UARTServo(servonum, angle):
    servonum = 64 + servonum
    date1 = int(angle/100 + 48)
    date2 = int((angle%100)/10 + 48)
    date3 = int(angle%10 + 48)
    cmd=bytearray([36,servonum,date1,date2,date3,35])
    ser.write(cmd)
    time.sleep(0.05)

UARTServo(1,0)
UARTServo(2,0)

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    global driverHorizonDegree, driverVerticalDegree

    operationCode = int(msg.payload.decode('utf-8'))

    if operationCode==1 and driverHorizonDegree<180:
        driverHorizonDegree += 30
        UARTServo(1,driverHorizonDegree)
    elif operationCode==2 and driverHorizonDegree>0:
        driverHorizonDegree -= 30
        UARTServo(1,driverHorizonDegree)
    elif operationCode==3 and driverVerticalDegree<180:
        driverVerticalDegree += 30
        UARTServo(2,driverVerticalDegree)
    elif operationCode==4 and driverVerticalDegree>0:
        driverVerticalDegree -= 30
        UARTServo(2,driverVerticalDegree)

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("elliot", "Elliot456")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("90a408bbb7e64fdebaeefdd412a92c08.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("driver/#", qos=1)

# a single publish, this can also be done in loops, etc.
# client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()

