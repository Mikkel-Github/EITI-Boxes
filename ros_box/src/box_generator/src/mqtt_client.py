from box_spawner_client import spawn_boxes, reset_gazebo
import paho.mqtt.client as mqtt
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box_spawner/spawn")
    client.subscribe("box_spawner/delete") # don't know if we need this
    client.subscribe("box_spawner/reset")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    payload = ""
    if(str(msg.payload) != "b''"): # Payload is NOT empty
        payload = json.loads(msg.payload)

    print(msg.topic + " " + str(payload))

    if(str(msg.topic) == "box_spawner/spawn"):
        # Call box spawn algorithm
        # if algorithm didn't fail - Call spawn boxes
        print("Spawn boxes")
        spawn_boxes(payload['n_boxes'], payload['mass'], payload['height'], payload['width'], payload['length'])
    elif(str(msg.topic) == "box_spawner/reset"):
        reset_gazebo()
        print("Reset Simulation")


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("ec2-16-16-27-107.eu-north-1.compute.amazonaws.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()
