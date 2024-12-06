<script setup lang="ts">
import { OrbitControls } from '@tresjs/cientos'
import Box from './Box.vue';
import Robot from './Robot.vue';
</script>

<template>
  <div class="Box-Specification-Container Column Flex">
    <h2>Preview</h2>
        <div class="Column Flex" style="cursor: grab;">
            <TresCanvas preset="realistic" shadows="true">
                <TresGridHelper v-if="showGrid" :args="[10, 10]" />
                <TresAxesHelper v-if="showOrientation" :args="[5]" />

                <TresPerspectiveCamera
                    ref="cameraRef"
                    :position="[0.8, 0.4, 0.8]"
                    :look-at="[0, 0, 0]"/>
                <OrbitControls
                    :auto-rotate="autoRotate"
                    :auto-rotate-speed="0.2"
                    :maxDistance="4"
                    :zoomSpeed="0.4"
                    :rotateSpeed="0.8"
                    @change="onOrbitChange"/>
                <Suspense>
                    <Box :scale="interpolatedScale" :position="{ x: 0, y: ((interpolatedScale.height / 2) / 100) + 0.002, z: 0 }"/>
                </Suspense>
                <Suspense>
                    <Robot ref="robot" />
                </Suspense>
                <TresAmbientLight :intensity="0.3" />
                <TresDirectionalLight :position="[1, 3, 3]" :look-at="[0, 0, 0]" :intensity="0.5" />
                <TresDirectionalLight :position="[-1, 3, -3]" :look-at="[0, 0, 0]" :intensity="0.4" />
            </TresCanvas>
            <div style="position: absolute;">
                <div @mousedown="showSettings = !showSettings" style="cursor: pointer; display: flex; align-items: center; background-color: #cfcfcf; height: 30px; width: 30px; border-radius: 10px; filter: drop-shadow(2px 2px 2px #6b6b6b);">
                    <div style="height: 22px; width: 22px; margin: auto; fill: #333333;">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"/></svg>
                    </div>
                </div>
                <transition name="drop">
                    <div v-if="showSettings" style="display: flex; flex-direction: column; align-items: flex-start; gap: 3px; margin-top: 7px;">
                        <button class="Button" :style="showGrid ? 'background-color: green;' : 'background-color: red;'" @mousedown="showGrid = !showGrid">Grid</button>
                        <button class="Button" :style="showOrientation ? 'background-color: green;' : 'background-color: red;'" @mousedown="showOrientation = !showOrientation">Orientation</button>
                        <button class="Button" :style="autoRotate ? 'background-color: green;' : 'background-color: red;'" @mousedown="autoRotate = !autoRotate">Rotate</button>
                    </div>
                </transition>
            </div>
        </div>
        <div class="Row" style="justify-content: space-between;">
            <div class="camera-info">
                Camera Position: {{ cameraState.position.x.toFixed(2) + ", " + cameraState.position.y.toFixed(2) + ", " + cameraState.position.z.toFixed(2) }}
            </div>
            <div class="camera-info">
                Camera Rotation: {{ cameraState.rotation.x.toFixed(2) + ", " + cameraState.rotation.y.toFixed(2) + ", " + cameraState.rotation.z.toFixed(2) }}
            </div>
            <div class="orbit-info">
                Zoom Level: {{ (4 - cameraState.zoom).toFixed(2) }}
            </div>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            interpolatedScale: {height: 10, width: 10, length: 10}, // Current width for interpolation
            initialScale: {height: 10, width: 10, length: 10},
            showSettings: false,
            showGrid: false,
            showOrientation: false,
            autoRotate: true,
            cameraState: { zoom: 1, position: { x: 0.8, y: 0.4, z: 0.8}, rotation: { x: 0, y: 0, z: 0} }
        };
    },
    props: {
        scale: {
          type: { height: Number, width: Number, length: Number },
          required: true
        }
    },
    mounted() {
    },
    methods: {
        calculateDistance(point1: { x: number, y: number, z: number }, point2: { x: number, y: number, z: number }): number {
            const dx = point2.x - point1.x;
            const dy = point2.y - point1.y;
            const dz = point2.z - point1.z;

            return Math.sqrt(dx * dx + dy * dy + dz * dz);
        },
        onOrbitChange(data) {
            const camera_data = data.object;
            this.cameraState.zoom = this.calculateDistance({x: 0, y: 0, z: 0}, camera_data.position)
            this.cameraState.position = camera_data.position;
            this.cameraState.rotation = camera_data.rotation;
        },
        interpolateScale(targetScale: { height: Number, width: Number, length: Number }) {
            const duration = 350; // 1 second
            const steps = 60; // Number of frames (assuming ~60fps)
            const stepTime = duration / steps;

            const delta_height = targetScale.height - this.initialScale.height;
            const delta_width = targetScale.width - this.initialScale.width;
            const delta_length = targetScale.length - this.initialScale.length;

            let currentStep = 0;
            const interval = setInterval(() => {
                currentStep++;
                const temp_height = this.initialScale.height + delta_height * (currentStep / steps);
                const temp_width = this.initialScale.width + delta_width * (currentStep / steps);
                const temp_length = this.initialScale.length + delta_length * (currentStep / steps);
                this.interpolatedScale = { height: temp_height, width: temp_width, length: temp_length };
                if (currentStep >= steps) {
                    clearInterval(interval);
                    this.interpolatedScale = targetScale; // Ensure final precision
                }
            }, stepTime);
        },
    },
    watch: {
        scale: {
            handler(newScale: { height: Number, width: Number, length: Number }) {
                console.log(`new scale: (${newScale.height}, ${newScale.width}, ${newScale.length})`)
                this.initialScale = this.interpolatedScale;
                console.log(`initialScale: (${this.initialScale.height}, ${this.initialScale.width}, ${this.initialScale.length})`)
                this.interpolateScale(newScale);
            },
            immediate: true, // Trigger interpolation on first render
        },
    },
};
</script>
