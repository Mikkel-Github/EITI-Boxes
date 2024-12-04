<script setup lang="ts">
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import SimulationFeed from '../Components/BoxItComponents/SimulationFeed.vue';
import Header from '../Components/BoxItComponents/Header.vue';
</script>

<template>
    <div class="" style="width: 100vw; height: 120vh;">
        <div class="Column">
            <Header />

            <div class="Outer">
                <h1>Current Report Feed</h1>
                <br>
                <div class="Simulation-Setup-Container Row">
                    <!-- 3D view -->
                    <RenderView />
                    <!-- Box specifications -->
                    <SimulationSetup v-if="!running_simulations" />
                    <!-- Live simulation feedback -->
                    <SimulationFeed v-else />
                </div>

                <div v-if="!running_simulations" class="Row Flex V-Center" style="margin-top: 2rem;">
                    <button class="btn btn-primary" @click="publishMessage">Start</button>
                </div>
                <div v-if="running_simulations" class="Row Flex V-Center" style="margin-top: 2rem;">
                    <button class="btn btn-red" @click="stopSimulating">Stop Simulating</button>
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
            dimensions: {height: 0, width: 0, length: 0},
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
        mqttService.subscribe('your/topic', (message) => {
            console.log('Received message:', message);
        });
    },
    beforeUnmount() {
        mqttService.disconnect();
    }
}
</script>
