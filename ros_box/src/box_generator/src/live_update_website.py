import time
import paho.mqtt.client as mqtt
import json
from box_placement_algorithm import Algorithm
import random

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box_placement/generate_setup")
    client.subscribe("box_placement/websiteready")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("MESSAGE")
    payload = ""
    if(str(msg.payload) != "b''"): # Payload is NOT empty
        payload = json.loads(msg.payload)

    print(msg.topic + " " + str(payload))

    if(str(msg.topic) == "box_placement/generate_setup"):
        len_layouts = a.Setup(payload['n_boxes'], payload['width'], payload['length'], payload['height'], payload['mass'], False)
        data = {}
        data["generated_orientations"] = len_layouts
        client.publish("website/showlivesim", json.dumps(data))
        # client.publish("box_placement", str(layouts[0]))
    if(str(msg.topic) == "box_placement/websiteready"):
        # Start Mock Simulation
        a.StartSimulation()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("mqtt", 1883, 60)

a = Algorithm()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()

# mqttc.loop_start()  # Use loop_start() to run the loop in a separate thread.