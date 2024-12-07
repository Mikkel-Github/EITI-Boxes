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

            <div class="Outer Column">
                <h1>Reports</h1>
                <br>
                <div class="Row">
                    <div class="Simulation-Setup-Container Column">
                        <button class="btn btn-primary" @mousedown="OpenReport(report.id)" v-for="report in reports">{{ report.id + " - " + report.company_name }}</button>
                    </div>
                    <div class="Column Flex" />
                </div>
            </div>
        </div>
    </div>
</template>

<style>
</style>

<script lang="ts">
import { Inertia } from '@inertiajs/inertia';
import { getReports } from '@/services/DatabaseHandler';

export default {
    data() {
        return {
            reports: [],
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        OpenReport(id: Number) {
            Inertia.visit(`/report/${id}`);
        },
    },
    async mounted() {
        console.log("Setup")
        this.reports = await getReports()
        console.log(this.reports)
    },
    beforeUnmount() {
    }
}
</script>
