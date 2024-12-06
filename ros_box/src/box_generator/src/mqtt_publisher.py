import paho.mqtt.client as mqtt
import json

def send_message(topic, message, broker_address="localhost", port=1883):
    """
    Sends a message to the specified MQTT topic.

    :param topic: The MQTT topic to send the message to.
    :param message: The message to send (could be a dictionary, string, etc.).
    :param broker_address: The MQTT broker address (default is localhost).
    :param port: The MQTT broker port (default is 1883).
    """
    # Create a new MQTT client instance
    client = mqtt.Client()

    # Connect to the broker
    client.connect(broker_address, port, 60)

    # Convert the message to a JSON string (if it is a dictionary)
    if isinstance(message, dict):
        message = json.dumps(message)

    # Publish the message to the specified topic
    client.publish(topic, str(message))

    # Disconnect after sending the message
    client.disconnect()

# Example usage
if __name__ == "__main__":
    send_message("website/runresult", {"n_boxes": 5, "width": 10, "length": 20, "height": 15, "mass": 50})

def announce_orientation_evaluation(runs_for_orientation):
    print("Finished an orientation!")
    send_message("website/runresult", runs_for_orientation)

def announce_best_run(best_run):
    print("Found the best run!")
    send_message("website/bestrun", best_run)
