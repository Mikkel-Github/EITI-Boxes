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
                <h1>Reports</h1>
                <br>
                <div class="Simulation-Setup-Container Row">
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
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
    },
    mounted() {
    },
    beforeUnmount() {
    }
}
</script>
