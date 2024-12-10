<script setup lang="ts">
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import SimulationFeed from '../Components/BoxItComponents/SimulationFeed.vue';
import Header from '../Components/BoxItComponents/Header.vue';

import dayjs from 'dayjs';
</script>

<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column">
            <Header />

            <div class="Outer Column" style="gap: 20px;">
                <h1>Reports</h1>
                <div v-for="(groupedReports, warehouse) in groupedReports" :key="warehouse" >
                    <h2>{{ warehouse }}</h2>
                    <div class="Row">
                        <div class="Column">
                            <button v-for="report in groupedReports" :key="report.id" class="btn btn-primary" @mousedown="OpenReport(report.id)">
                                {{ report.id + " - " + dayjs(report.created_at).format('MMMM D, YYYY h:mm A') + " - " + report.robot_model + " - " + report.route }}
                            </button>
                        <hr>
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
        groupedReports() {
            const groups: { [key: string]: Array<any> } = {};
            this.reports.forEach((report) => {
                if (report.map) {
                    if (!groups[report.map]) {
                        groups[report.map] = [];
                    }
                    groups[report.map].push(report);
                }
            });
            return groups;
        },
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
