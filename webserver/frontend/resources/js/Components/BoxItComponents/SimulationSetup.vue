<script setup lang="ts">
import FileUpload from './FileUpload.vue'
</script>

<template>
    <!-- Box sepcifications -->
    <div class="Box-Specification-Container Column Flex">
        <h2>Box Dimensions</h2>
        <p style="font-style: italic; font-size: 11pt;">Measurements of one box.</p>
        <div class="Row">
            <!-- Dimensions -->
            <div class="Dimensions-Field-Container Column">
                <!-- Height -->
                <div class="Input-Field-Container Column">
                    <span>Height (cm)</span>
                    <input v-model="dimensions.height" placeholder="10" @blur="UpdateSize">
                </div>
                <!-- Width -->
                <div class="Input-Field-Container Column">
                    <span>Width (cm)</span>
                    <input v-model="dimensions.width" placeholder="20" @blur="UpdateSize">
                </div>
                <!-- Depth -->
                <div class="Input-Field-Container Column">
                    <span>Length (cm)</span>
                    <input v-model="dimensions.length" placeholder="40" @blur="UpdateSize">
                </div>
            </div>
            <div class="Column">
                <!-- Mass -->
                <div class="Input-Field-Container Column">
                    <span>Mass of one box (g)</span>
                    <div class="Row">
                        <input v-model="mass" placeholder="350">
                    </div>
                </div>
                <!-- Amount -->
                <div class="Input-Field-Container Column">
                    <span>Amount of boxes</span>
                    <div class="Row">
                        <input v-model="amount" placeholder="200">
                    </div>
                </div>
                <!-- Fragile -->
                <div class="Input-Field-Container Column">
                    <div class="Row" >
                        <span>Fragile content</span>
                        <p v-if="fragile" style="margin-left: 0.5rem; color: red">Boxes will NOT be rotated but keep their initial orientation!</p>
                    </div>
                    <div class="Row Flex" >
                        <input v-model="fragile" type="checkbox" style="color: red; height: 100%;">
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <h2>Simulation Settings</h2>
        <div class="Row">
            <div class="Column">
                <div class="Column">
                    <span>Robot Model</span>
                    <select>
                        <option>MiR100</option>
                        <option>MiR250</option>
                        <option>MiR600</option>
                        <option>MiR1350</option>
                    </select>
                </div>
                <div class="Column">
                    <span>Prioritize</span>
                    <select>
                        <option>Maximize boxes moved per hour</option>
                        <option>Maximize number of boxes per trip</option>
                        <option>Maximize safety</option>
                    </select>
                </div>
            </div>
            <div class="Column">
                <span>Map</span>
                <select>
                    <option v-for="(map, index) in maps">{{ map }}</option>
                </select>
                <span>Create new map</span>
                <button @mousedown="OpenMapCreator" class="btn btn-primary">Upload map</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

export default {
    data() {
        return {
            mass: "",
            amount: "",
            fragile: false,
            dimensions: {height: "", width: "", length: ""},
            maps: [
                "Warehouse 1",
                "Warehouse 2",
                "Warehouse 3",
            ],
        }
    },
    props: {
        modelValue: {
            type: { height: Number, width: Number, length: Number },
            required: true,
        },
    },
    computed: {
    },
    methods: {
        UpdateSize() {
            const capture = { height: this.dimensions.height, width: this.dimensions.width, length: this.dimensions.length }
            if(capture.height == '' || capture.width == '' || capture.length == '') { return }
            this.$emit('update:modelValue', capture); // Emit the standard v-model update event
        },
        OpenMapCreator() {
            console.log("OpenMapCreator")
            this.$emit('toggleMap');
        }
    },
    mounted() {
    },
    beforeUnmount() {
    }
}
</script>
