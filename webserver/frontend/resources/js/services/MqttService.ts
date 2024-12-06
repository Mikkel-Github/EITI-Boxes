import mqtt from 'mqtt';

class MqttService {
    private client: mqtt.MqttClient;

    constructor(brokerUrl: string) {
        this.client = mqtt.connect(brokerUrl, {
            protocolVersion: 4
        });
    }

    subscribe(topic: string, callback: (topic: string, message: string) => void) {
        this.client.subscribe(topic, (err) => {
            if (!err) {
                this.client.on('message', (topic, message) => {
                    callback(topic.toString(), message.toString());
                });
            }
        });
    }

    publish(topic: string, message: string) {
        this.client.publish(topic, message);
    }

    disconnect() {
        this.client.end();
    }
}

// export default new MqttService('ws://ec2-16-16-27-107.eu-north-1.compute.amazonaws.com:8080'); // Update with your broker URL
export default new MqttService('ws://localhost:8883'); // Update with your broker URL

