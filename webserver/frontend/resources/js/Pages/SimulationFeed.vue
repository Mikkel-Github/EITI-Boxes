<script setup lang="ts">

</script>

<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column">
            <Header />

            <div class="Outer Column Flex">
                <h1>Report #{{ id }} Live Feed</h1>

                <br>

                <div class="Column" >
                    <h2 style="margin-bottom: 0.4rem;">Orientations tried: {{ Number(tweened_orientations_tried.number).toFixed(0) }}/{{ total_orientations }}</h2>
                    <h2 style="margin-bottom: 0.4rem;">Runs: {{ Number(tweened_runs.number).toFixed(0) }}</h2>
                    <h2 style="margin-bottom: 0.4rem;">Confidence: {{ Number(tweened_confidence.number).toFixed(0) }}</h2>
                    <h2 style="margin-bottom: 0.4rem;">Time spent: {{ Number(tweened_time_spent.number).toFixed(0) }}</h2>
                </div>

                <span v-if="loading_percentage < 100" style="width: 245px; margin: auto; margin-bottom: 1rem; font-size: 16pt;">Performing optimization{{loading_text}}</span>
                <span v-else style="margin: auto; margin-bottom: 1rem; font-size: 16pt;">Completed!</span>

                <div class="meter animate">
                    <span :style="`width: ${loading_percentage}%; ${loading_percentage == 100 ? 'border-top-left-radius: 8px; border-bottom-left-radius: 8px;' : ''}` "></span>
                </div>

                <div class="Row V-Center" style="margin-top: 1rem; margin-bottom: 1rem;">
                    <button :style="`${loading_percentage < 100 ? '' : 'opacity: 0;'}`" class="btn btn-red" @click="stopSimulating">Stop Simulating</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.meter {
    height: 20px;
    position: relative;
    background: #555;
    border-radius: 25px;
    padding: 2px;
    box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.3);
}

.meter > span {
    display: block;
    height: 100%;
    min-height: 16px;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    background-color: rgb(43,194,83);
    background-image: linear-gradient(
        center bottom,
        rgb(43,194,83) 37%,
        rgb(84,240,84) 69%
    );
    box-shadow:
        inset 0 2px 9px  rgba(255,255,255,0.3),
        inset 0 -2px 6px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;

    transition: width 0.5s ease-in-out;
}

.meter > span:after {
    content: "";
    position: absolute;
    top: 0; left: 0; bottom: 0; right: 0;
    background-image: linear-gradient(
        -45deg,
        rgba(255, 255, 255, .2) 25%,
        transparent 25%,
        transparent 50%,
        rgba(255, 255, 255, .2) 50%,
        rgba(255, 255, 255, .2) 75%,
        transparent 75%,
        transparent
    );
    z-index: 1;
    background-size: 50px 50px;
    animation: move 2s linear infinite;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    overflow: hidden;
}

.meter > span::after, .animate > span > span {
    animation: move 2s linear infinite;
}

@keyframes move {
    0% {
        background-position: 0 0;
    }
    100% {
        background-position: 50px 50px;
    }
}
</style>

<script lang="ts">
import { Inertia } from '@inertiajs/inertia';

import { ref, reactive, watch } from 'vue'
import gsap from 'gsap'

import mqttService from '@/services/MqttService';
import { Report, updateReport } from '@/services/DatabaseHandler';

// Components
import RenderView from '../Components/BoxItComponents/RenderView.vue';
import SimulationSetup from '../Components/BoxItComponents/SimulationSetup.vue';
import Header from '../Components/BoxItComponents/Header.vue';


export default {
    components: {
        RenderView,
        SimulationSetup,
        Header,
    },
    data() {
        return {
            loading_text: "",

            running_simulations: false,

            loading_percentage: 0,

            runs: 0,
            orientations_tried: 0,
            confidence: 0,
            time_spent: 0,
        }
    },
    props: {
    },
    computed: {
    },
    setup() {
        const url_params = window.location.href.split('/')
        console.log(url_params)
        const id = ref(url_params[4]);
        const total_orientations = ref(url_params[5]);

        const tweened_loading_percentage = reactive({ loading_percentage: 0 })

        const tweened_orientations_tried = reactive({ orientations_tried: 0 })
        const tweened_runs = reactive({ runs: 0 })
        const tweened_confidence = reactive({ confidence: 0 })
        const tweened_time_spent = reactive({ time_spent: 0 })


        return {
            id,
            total_orientations,
            tweened_orientations_tried,
            tweened_runs,
            tweened_confidence,
            tweened_time_spent
        }
    },
    watch: {
        orientations_tried: {
            handler(newValue: Number) {
                gsap.to(this.tweened_orientations_tried, { duration: 0.5, number: Number(newValue) || 0 })
            },
            immediate: true, // Trigger interpolation on first render
        },
        runs: {
            handler(newValue: Number) {
                gsap.to(this.tweened_runs, { duration: 0.5, number: Number(newValue) || 0 })
            },
            immediate: true, // Trigger interpolation on first render
        },
        confidence: {
            handler(newValue: Number) {
                gsap.to(this.tweened_confidence, { duration: 0.5, number: Number(newValue) || 0 })
            },
            immediate: true, // Trigger interpolation on first render
        },
        time_spent: {
            handler(newValue: Number) {
                gsap.to(this.tweened_time_spent, { duration: 0.5, number: Number(newValue) || 0 })
            },
            immediate: true, // Trigger interpolation on first render
        },
    },
    methods: {
        progressLoadingText() {
            if(this.loading_text == "...") {
                this.loading_text = ""
                return
            }
            this.loading_text += "."
        },
        publishMessage() {
            // mqttService.publish('box_spawner/spawn',JSON.stringify(payload));
        },
    },
    mounted() {
        mqttService.subscribe('website/runresult', (topic, message) => {
            if(topic != 'website/runresult') return
            console.log('Received message on topic website/runresult:', message);

            this.orientations_tried++;
            this.runs += Number(message)

            this.loading_percentage = (this.orientations_tried / this.total_orientations) * 100
        });
        mqttService.subscribe('website/bestrun', async (topic, message) => {
            if(topic != 'website/bestrun') return
            console.log('Received message on topic website/bestrun:', message);

            const data = JSON.parse(message.toString())
            if(!data.hasOwnProperty('runs') || data.runs == '' || !data.hasOwnProperty('confidence') || data.confidence == '' || !data.hasOwnProperty('time_spent') || data.time_spent == '' || !data.hasOwnProperty('predicted_route_time') || data.predicted_route_time == '' || !data.hasOwnProperty('boxes_moved_per_run') || data.boxes_moved_per_run == '' || !data.hasOwnProperty('positions') || data.positions == '' || !data.hasOwnProperty('dimension') || data.dimension == '') return

            const report: Report = {
                orientations_tried: Number(this.total_orientations),
                runs: Number(data.runs),
                confidence: Number(data.confidence),
                time_spent: Number(data.time_spent),
                predicted_route_time: Number(data.predicted_route_time),
                boxes_moved_per_run: Number(data.boxes_moved_per_run),
                positions: data.positions,
                height: Number(data.dimension.height),
                width: Number(data.dimension.width),
                length: Number(data.dimension.length),
                acceleration: Number(data.acceleration),
                deacceleration: Number(data.deacceleration),
                speed: Number(data.speed),
                velocity: Number(data.velocity),
                velocity_theta: Number(data.velocity_theta),
            };
            const finalReport = await updateReport(this.id, report);

            Inertia.visit(`/report/${this.id}`);
        });

        mqttService.publish('box_placement/websiteready');

        setInterval(() => {
            this.progressLoadingText()
        }, 1000);


        /* setInterval(() => {
            if(this.loading_percentage >= 100) {
                this.loading_percentage = 100
                return
            }

            this.orientations_tried++
            this.runs += Math.floor(Math.random() * 20) + 11

            this.loading_percentage += Math.floor(Math.random() * 5);

        }, 2000); */
    },
    beforeUnmount() {
        mqttService.disconnect();
    }
}
</script>
