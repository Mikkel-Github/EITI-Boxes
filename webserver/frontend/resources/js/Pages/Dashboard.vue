<script setup lang="ts">
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import SimulationFeed from '../Components/BoxItComponents/SimulationFeed.vue';
import Header from '../Components/BoxItComponents/Header.vue';
import FileUpload from '../Components/BoxItComponents/FileUpload.vue';
</script>

<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column">
            <Header />

            <div class="Outer Column Flex">
                <h1 >Transportation Setup</h1>
                <br>
                <div class="Simulation-Setup-Container Row Flex">
                    <!-- 3D view -->
                    <RenderView :scale="dimensions" />
                    <!-- Box specifications -->
                    <SimulationSetup v-if="!running_simulations" v-model="dimensions" @toggleMap="toggleMap" />
                    <!-- Live simulation feedback -->
                    <SimulationFeed v-else />
                </div>

                <div v-if="!running_simulations" class="Row V-Center" style="margin-top: 1rem; margin-bottom: 1rem;">
                    <button class="btn btn-primary" @click="publishMessage">Start</button>
                </div>
                <div v-if="running_simulations" class="Row V-Center" style="margin-top: 1rem; margin-bottom: 1rem;">
                    <button class="btn btn-red" @click="stopSimulating">Stop Simulating</button>
                </div>
            </div>
        </div>
        <FileUpload v-if="map_creator_open" @toggleMap="toggleMap"/>
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
            dimensions: {height: 10, width: 10, length: 10},
            map_creator_open: false,
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        toggleMap(data) {
            console.log("toggleMap")
            this.map_creator_open = !this.map_creator_open
        },
        publishMessage() {
            let payload = {n_boxes: this.amount, mass: this.mass, height: this.dimensions.height, width: this.dimensions.width, lenght: this.dimensions.length}
            // mqttService.publish('box_spawner/spawn',JSON.stringify(payload));
            this.running_simulations = true;
        },
        stopSimulating() {
            // mqttService.publish('box_spawner/stop');
        },
    },
    mounted() {
        mqttService.subscribe('your/topic', (message) => {
            console.log('Received message:', message);
        });
        mqttService.subscribe('mikkl20/box_spawner/spawn', (message) => {
            console.log('Received message:', message);
        });
    },
    beforeUnmount() {
        mqttService.disconnect();
    }
}
</script>
