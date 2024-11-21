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
                <h1 >Transportation Setup</h1>
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
.Primary {
    color: #e9b66f;
}

.vr {
    border-left: 2px solid #7a5c30;
}

input {
    max-height: 42px;
    min-width: 200px;
}

select {
    min-width: 200px;
}

h1 {
    font-size: 24pt;
    font-weight: 700;
}

h2 {
    font-size: 16pt;
    font-weight: 700;
}

hr {
    margin-top: 1.0rem;
    margin-bottom: 0.6rem;
}

.Outer {
    @apply px-8 py-0
}

.btn {
    @apply font-bold py-2 px-4 rounded;
}
.btn-primary {
    background-color: #e9b66f;
    color: #212121;
    transition: background-color 0.2s;
}
.btn-primary:hover {
    background-color: #b58848;
}
.btn-red {
    @apply bg-red-500 text-white;
}
.btn-red:hover {
    @apply bg-red-700;
}
.Row {
    display: flex;
    gap: .4rem;
}

.Column {
    display: flex;
    flex-direction: column;
    gap: .4rem;
}

.H-Center {
    align-items: center;
}

.V-Center {
    align-items: center;
    justify-content: center
}

.Flex {
    flex: 1;
}

.Simulation-Setup-Container {
}

.Box-Specification-Container {
}

.Input-Field-Container {
}

.Dimensions-Field-Container {
}
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
            let payload = {n_boxes: this.amount, mass: this.mass, height: this.dimensions.height, width: this.dimensions.width, lenght: this.dimensions.length}
            // mqttService.publish('box_spawner/spawn',JSON.stringify(payload));
            this.running_simulations = true;
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
