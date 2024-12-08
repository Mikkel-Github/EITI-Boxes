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

def announce_orientation_evaluation(runs_for_orientation):
    print("Finished an orientation!")
    send_message("website/runresult", runs_for_orientation)

def announce_best_run(best_run, total_time: int, total_runs: int):
    print("Found the best run!")
    data = {}
    data["runs"] = total_runs
    data["confidence"] = 0.946
    data["time_spent"] = total_time
    data["predicted_route_time"] = best_run.result.time
    data["boxes_moved_per_run"] = len(best_run.positions)
    data["positions"] = [position.to_dict() for position in best_run.positions]  # Convert to dict
    data["dimension"] = best_run.orientation.to_dict()
    data["acceleration"] = best_run.robot_settings.acceleration
    data["deacceleration"] = best_run.robot_settings.deacceleration
    data["speed"] = best_run.robot_settings.speed
    data["velocity"] = best_run.robot_settings.velocity
    data["velocity_theta"] = best_run.robot_settings.velocity_theta

    send_message("website/bestrun", data)
