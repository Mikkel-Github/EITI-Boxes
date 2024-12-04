<script setup lang="ts">
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import SimulationFeed from '../Components/BoxItComponents/SimulationFeed.vue';
import Header from '../Components/BoxItComponents/Header.vue';
</script>

<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column">
            <Header />

            <div class="Outer">
                <h1>Report #{{ report_id }}</h1>
                <h2>{{ companyName }}</h2>
                <br>
                <div class="Row" style="gap: 5rem;">
                    <div class="Column" style="gap: 2rem;">
                        <div class="Column">
                            <h2>Shipment settings</h2>
                            <span><span style="font-weight: bold;">Robot model:</span>    {{ robot_model }}</span>
                            <span><span style="font-weight: bold;">Map:</span>    {{ map.name }}</span>
                            <span><span style="font-weight: bold;">Route:</span>    {{ route.name }}</span>
                        </div>
                        <div class="Column">
                            <h2>Simulation details</h2>
                            <span><span style="font-weight: bold;">Simulation time:</span>    {{ simulation.time }}</span>
                            <span><span style="font-weight: bold;">Confidence:</span>    {{ simulation.confidence }}</span>
                            <span><span style="font-weight: bold;">runs:</span>    {{ simulation.runs }}</span>
                        </div>
                    </div>
                    <div class="Column">
                        <h2>Shipment details</h2>
                        <div class="Column">
                            <span><span style="font-weight: bold;">Predicted route time:</span>    {{ shipment.predicted_time }}</span>
                            <span><span style="font-weight: bold;">Predicted total time:</span>    {{ shipment.predicted_time * (shipment.boxes_per_run / shipment.total_boxes) }}</span>
                            <span><span style="font-weight: bold;">Boxes moved per run:</span>     {{ shipment.boxes_per_run }}</span>
                            <span><span style="font-weight: bold;">Boxes moved per hour:</span>    {{ shipment.boxes_per_run * (shipment.predicted_time / 3600) }}</span>
                        </div>
                    </div>
                </div>
           </div>
        </div>
    </div>
</template>

<style>
</style>

<script lang="ts">
import mqttService from '@/services/MqttService';

export default {
    data() {
        return {
            running_simulations: false,
            mass: 0,
            amount: 0,
            dimensions: { height: 0, width: 0, length: 0 },
            report_id: "",
            companyName: "Googologoloo",
            robot_model: "MiR100",
            map: {
                id: 1234,
                name: "Warehouse 1",
            },
            route: {
                id: 1234,
                name: "Product route 1",
            },
            simulation: {
                time: 10800,
                confidence: 0.998,
                runs: 56,
            },
            shipment: {
                predicted_time: 30,
                boxes_per_run: 10,
                total_boxes: 100,
            }
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        publishMessage() {
            // mqttService.publish('box_spawner/spawn',JSON.stringify(payload));
        },
        stopSimulating() {
            // mqttService.publish('box_spawner/stop');
        }
    },
    mounted() {
        this.report_id = window.location.href.split('/').pop();

        mqttService.subscribe('your/topic', (message) => {
            console.log('Received message:', message);
        });
    },
    beforeUnmount() {
        mqttService.disconnect();
    }
}
</script>
