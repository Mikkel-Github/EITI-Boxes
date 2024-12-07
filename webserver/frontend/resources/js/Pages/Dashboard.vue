<script setup lang="ts">
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
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
                    <SimulationSetup @settingsUpdated="updateSettings" @toggleMap="toggleMap" />
                </div>

                <div class="Row V-Center" style="margin-top: 1rem; margin-bottom: 1rem;">
                    <button class="btn btn-primary" @click="StartSimulation">Start</button>
                </div>
            </div>
        </div>
        <FileUpload v-if="map_creator_open" @toggleMap="toggleMap"/>
    </div>
</template>

<style>
</style>

<script lang="ts">
import { Inertia } from '@inertiajs/inertia';

import { Report, saveReport, getReports } from '@/services/DatabaseHandler';
import mqttService from '@/services/MqttService';

export default {
    data() {
        return {
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
        updateSettings(data) {
            this.mass = data.mass
            this.amount = data.amount
            console.log("This data")
            console.log(this.mass)
            console.log(this.amount)

            const new_dimensions = { height: this.dimensions.height, width: this.dimensions.width, length: this.dimensions.length }

            if(data.dimensions.height != '') new_dimensions.height = data.dimensions.height
            if(data.dimensions.width != '') new_dimensions.width = data.dimensions.width
            if(data.dimensions.length != '') new_dimensions.length = data.dimensions.length

            this.dimensions = new_dimensions

            console.log(this.dimensions)
        },
        toggleMap(data) {
            console.log("toggleMap")
            this.map_creator_open = !this.map_creator_open
        },
        StartSimulation() {
            let payload = {n_boxes: this.amount, mass: this.mass, height: this.dimensions.height, width: this.dimensions.width, length: this.dimensions.length}
            mqttService.publish('box_placement/generate_setup', JSON.stringify(payload));
        },
        stopSimulating() {
            // mqttService.publish('box_spawner/stop');
        },
    },
    mounted() {
        mqttService.subscribe('website/showlivesim', async (topic, message) => {
            if(topic != 'website/showlivesim') return

            const data = JSON.parse(message.toString())
            if(!data.hasOwnProperty('generated_orientations') || data.generated_orientations == '') return

            const reports = await getReports()
            let id = 1
            if(reports.length > 0) id = reports.at(-1).id + 1
            console.log(id)

            console.log(data)
            const partialReport: Report = { id: id, company_name: "Company A", robot_model: "MiR 100", map: "Warehouse 1", route: "Route A" };
            console.log(partialReport)
            const savedReport = await saveReport(partialReport);

            Inertia.visit(`/simulation/${id}/${data.generated_orientations}`);
        });
    },
    beforeUnmount() {
        mqttService.disconnect();
    }
}
</script>
