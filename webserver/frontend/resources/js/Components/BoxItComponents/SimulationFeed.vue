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
                    <input v-model="dimensions.height" placeholder="10" @mousedown="dimensions.height=''">
                </div>
                <!-- Width -->
                <div class="Input-Field-Container Column">
                    <span>Width (cm)</span>
                    <input v-model="dimensions.width" placeholder="20" @mousedown="dimensions.width=''">
                </div>
                <!-- Depth -->
                <div class="Input-Field-Container Column">
                    <span>Length (cm)</span>
                    <input v-model="dimensions.length" placeholder="40" @mousedown="dimensions.length=''">
                </div>
            </div>
            <div class="Column">
                <!-- Mass -->
                <div class="Input-Field-Container Column">
                    <span>Mass of one box (g)</span>
                    <div class="Row">
                        <input v-model="mass" placeholder="350" @mousedown="mass=''" :disabled="autofit">
                    </div>
                </div>
                <!-- Amount -->
                <div class="Input-Field-Container Column">
                    <span>Amount of boxes</span>
                    <div class="Row">
                        <input v-model="amount" placeholder="200" @mousedown="amount=''" :disabled="autofit">
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
                        <option>Maximize moved boxes per hour</option>
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
                <span>Upload new map</span>
                <button @mousedown="OpenMapCreator" class="btn btn-blue">Create map</button>
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
            dimensions: {height: "", width: "", length: ""},
            map_creator_open: false,
            maps: [
                "Warehouse 1",
                "Warehouse 2",
                "Warehouse 3",
            ],
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        OpenMapCreator() {
            this.map_creator_open = true;
        }
    },
    mounted() {
    },
    beforeUnmount() {
    }
}
</script>

