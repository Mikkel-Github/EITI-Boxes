<template>
    <div>
        <div class="Outer Column">
            <h1 style="margin-bottom: 2rem;">Transportation Setup</h1>

            <div class="Simulation-Setup-Container Row">
                <!-- 3D view -->
                <div class="Image Flex">
                </div>
                <!-- Box sepcifications -->
                <div class="Box-Specification-Container Column Flex">
                    <!-- Dimensions -->
                    <div class="Dimensions-Field-Container Column">
                        <h2>Box Dimensions</h2>
                        <p style="font-style: italic; font-size: 11pt;">Measurements provided in centimeters</p>
                        <!-- Height -->
                        <div class="Input-Field-Container Column">
                            <span>Height</span>
                            <input v-model="dimensions.height" placeholder="height" @mousedown="dimensions.height=''">
                        </div>
                        <!-- Width -->
                        <div class="Input-Field-Container Column">
                            <span>Width</span>
                            <input v-model="dimensions.width" placeholder="width" @mousedown="dimensions.width=''">
                        </div>
                        <!-- Depth -->
                        <div class="Input-Field-Container Column">
                            <span>Length</span>
                            <input v-model="dimensions.length" placeholder="length" @mousedown="dimensions.length=''">
                        </div>
                    </div>
                    <hr>
                    <!-- Amount -->
                    <div class="Input-Field-Container Column">
                        <span>Amount of boxes</span>
                        <div class="Row">
                            <input v-model="amount" placeholder="amount" @mousedown="amount=''" :disabled="autofit">
                            <div class="Row H-Center">
                                <span>Autofit amount of boxes:</span>
                                <input v-model="autofit" type="checkbox">
                            </div>
                        </div>
                    </div>
                    <!-- Mass -->
                    <div class="Input-Field-Container Column">
                        <span>Mass of one box</span>
                        <div class="Row">
                            <input v-model="mass" placeholder="mass" @mousedown="mass=''" :disabled="autofit">
                        </div>
                    </div>

                    {{ amount }}
                    {{ dimensions.height }}
                    {{ dimensions.width }}
                    {{ dimensions.depth }}
                </div>
            </div>
            <div class="Row Flex V-Center" style="margin-top: 2rem;">
                <button class="btn btn-blue" @click="publishMessage">Start</button>
            </div>
        </div>
    </div>
</template>

<style>
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
    @apply px-10 py-10
}

.btn {
    @apply font-bold py-2 px-4 rounded;
}
.btn-blue {
    @apply bg-blue-500 text-white;
}
.btn-blue:hover {
    @apply bg-blue-700;
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
            mass: 0,
            amount: 0,
            autofit: false,
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
            mqttService.publish('box_spawner/spawn',JSON.stringify(payload));
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
