<script setup lang="ts">
// import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import SimulationFeed from '../Components/BoxItComponents/SimulationFeed.vue';
import Header from '../Components/BoxItComponents/Header.vue';
import RenderTest from '../Pages/RenderTest.vue';
</script>

<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column Flex">
            <Header />

            <div class="Outer Column Flex">
                <div class="Row Flex">
                    <div class="Column">
                        <h1>Report #{{ report_id }}</h1>
                        <h2>{{ companyName }}</h2>
                        <br>
                        <div class="Row" style="gap: 5rem;">
                            <div class="Column" style="gap: 2rem;">
                                <div class="Column">
                                    <h2>Shipment settings</h2>
                                    <span><span style="font-weight: bold;">Robot model:</span>      {{ robot_model }}</span>
                                    <span><span style="font-weight: bold;">Map:</span>              {{ map.name }}</span>
                                    <span><span style="font-weight: bold;">Route:</span>            {{ route.name }}</span>
                                    <span><span style="font-weight: bold;">Box size:</span>
                                        <div class="Column" style="margin-left: 2rem; gap: 0;">
                                            <span>height: {{ dimensions.height }}cm</span>
                                            <span>width:   {{ dimensions.width }}cm</span>
                                            <span>length: {{ dimensions.length }}cm</span>
                                        </div>
                                    </span>
                                    <span><span style="font-weight: bold;">Box weight:</span>       {{ mass }}g</span>
                                </div>
                                <hr>
                                <div class="Column">
                                    <h2>Simulation details</h2>
                                    <span><span style="font-weight: bold;">Simulation time:</span>    {{ formatTime(simulation.time.toFixed(0))}}</span>
                                    <span><span style="font-weight: bold;">Orientations tried:</span>    {{ simulation.orientations_tried }}</span>
                                    <span><span style="font-weight: bold;">Simulation runs:</span>    {{ simulation.runs }}</span>
                                    <span><span style="font-weight: bold;">Confidence:</span>    {{ simulation.confidence }}</span>
                                </div>
                            </div>
                            <div class="Column">
                                <h2>Shipment details</h2>
                                <div class="Column">
                                    <span><span style="font-weight: bold;">Boxes moved per run:</span>     {{ shipment.boxes_per_run }}</span>
                                    <span><span style="font-weight: bold;">Total boxes to move:</span>     {{ shipment.total_boxes }}</span>
                                    <span><span style="font-weight: bold;">Total trips to make:</span>     {{ Math.ceil(shipment.total_boxes / shipment.boxes_per_run).toFixed(0) }}</span>
                                    <span><span style="font-weight: bold;">Trips per hour:</span>          {{ shipment.full_runs_hour }}</span>
                                    <span><span style="font-weight: bold;">Boxes moved per hour:</span>    {{ shipment.full_runs_boxes_hour }}</span>
                                    <span><span style="font-weight: bold;">Weight per trip:</span>         {{ (mass * shipment.boxes_per_run) / 1000 }}kg</span>
                                    <span><span style="font-weight: bold;">Predicted route time:</span>    {{ formatTime(shipment.predicted_time.toFixed(0)) }}</span>
                                    <span><span style="font-weight: bold;">Predicted total time:</span>    {{ formatTime(shipment.predicted_time * Math.ceil(shipment.total_boxes / shipment.boxes_per_run).toFixed(0)) }}</span>
                                </div>
                                <br>
                                <hr>
                                <h2>Robot settings</h2>
                                        <!-- self.acceleration = acceleration
                                        self.deacceleration = deacceleration
                                        self.speed = speed
                                        self.velocity = velocity
                                        self.velocity_theta = velocity_theta -->

                                <div class="Column">
                                    <span><span style="font-weight: bold;">Acceleration:</span>     {{ robot_settings.acceleration.toFixed(2) }}</span>
                                    <span><span style="font-weight: bold;">Deacceleration:</span>   {{ robot_settings.deacceleration.toFixed(2) }}</span>
                                    <span><span style="font-weight: bold;">Speed:</span>            {{ robot_settings.speed.toFixed(2) }}</span>
                                    <span><span style="font-weight: bold;">Velocity:</span>         {{ robot_settings.velocity.toFixed(2) }}</span>
                                    <span><span style="font-weight: bold;">Velocity Theta:</span>   {{ robot_settings.velocity_theta.toFixed(2) }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="Simulation-Setup-Container Row Flex">
                        <!-- 3D view -->
                        <RenderTest v-if="positions.length > 0" :boxDimensions="dimensions" :boxPositions="positions" />
                    </div>
                </div>
           </div>
        </div>
    </div>
</template>

<style>
</style>

<script lang="ts">
import { getReports } from '@/services/DatabaseHandler';

export default {
    data() {
        return {
            mass: 10,
            dimensions: { height: 10, width: 10, length: 20 },
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
                orientations_tried: 0,
                runs: 56,
            },
            shipment: {
                predicted_time: 30,
                boxes_per_run: 10,
                total_boxes: 100,
                full_runs_hour: 0,
                full_runs_boxes_hour: 0,
            },
            positions: [],
            robot_settings: {
                acceleration: 1,
                deacceleration: 1,
                speed: 1.5,
                velocity: 1,
                velocity_theta: 1,
            }
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        formatTime(seconds: number): string {
            const hours = Math.floor(seconds / 3600); // 1 hour = 3600 seconds
            const minutes = Math.floor((seconds % 3600) / 60); // 1 minute = 60 seconds
            const remainingSeconds = seconds % 60;

            // Format the time as "HH:MM:SS" with leading zeros if necessary
            return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
        },
        setup() {
            this.companyName = this.report.company_name;
            this.robot_model = this.report.robot_model;
            this.map.name = this.report.map;
            this.route.name = this.report.route;
            this.simulation.time = this.report.time_spent;
            this.simulation.confidence = this.report.confidence;
            this.simulation.orientations_tried = this.report.orientations_tried;
            this.simulation.runs = this.report.runs;
            this.shipment.predicted_time = this.report.predicted_route_time;
            this.shipment.boxes_per_run = this.report.boxes_moved_per_run;
            this.shipment.total_boxes = this.report.total_boxes

            this.shipment.full_runs_hour = Math.floor(3600 / this.shipment.predicted_time);
            this.shipment.full_runs_boxes_hour = (this.shipment.full_runs_hour * this.shipment.boxes_per_run)

            this.amount = this.report.total_boxes
            this.mass = this.report.mass
            this.dimensions = { height: this.report.height, width: this.report.width, length: this.report.length }

            this.positions = this.report.positions

            this.robot_settings = {
                acceleration: this.report.acceleration,
                deacceleration: this.report.deacceleration,
                speed: this.report.speed,
                velocity: this.report.velocity,
                velocity_theta: this.report.velocity_theta,
            }
        },
    },
    async mounted() {
        this.report_id = window.location.href.split('/').pop();

        const reports = await getReports()
        this.report = reports[this.report_id - 1]
        console.log(this.report)

        this.setup();
    },
}
</script>
