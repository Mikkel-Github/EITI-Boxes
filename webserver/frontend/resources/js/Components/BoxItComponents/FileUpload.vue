<template>
    <div  class="Floating-Window">
        <div class="Inside-Floating-Window">
            <div @mousedown="CloseMapCreator" class="Close-Button">x</div>
            <div class="Column Flex" style="align-items: center; padding-top: 6px;">
                <h2>Create new map</h2>
                <br>
                <div class="Input-Field-Container Column">
                    <span>Map name</span>
                    <div class="Row">
                        <input v-model="map_name" placeholder="name">
                    </div>
                    <span>File</span>
                    <div class="Row">
                        <input type="file" placeholder="">
                    </div>
                    <br>
                    <div class="Row" style="justify-content: center;">
                        <button @mousedown="OpenMapCreator" class="btn btn-primary">Create map</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- The lowest level div, if clicked will close the window -->
        <div class="Background" @mousedown="CloseMapCreator" />
    </div>
</template>

<style>
.Floating-Window {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
}

.Background {
    position: absolute;
    background-color: #21212190;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    z-index: 0;
}

.Inside-Floating-Window {
    background-color: white;
    height: 310px;
    width: 500px;

    position: relative;
    top: 50%;
    transform: translateY(-50%);
    margin: auto;

    border-radius: 20px;
    filter: drop-shadow(4px 4px 4px #21212180);

    z-index: 1;
}

.Close-Button {
    position: absolute;
    font-weight: bold;
    font-size: 20pt;
    margin-left: 14px;
    color: red;

    cursor: pointer;
}
</style>

<script lang="ts">
export default {
    data() {
        return {
            map_name: "",
        }
    },
    props: {
        map_creator_open: {
            type: Boolean,
        }
    },
    computed: {
    },
    methods: {
        CloseMapCreator() {
            this.$emit('toggleMap');
        }
    },
    mounted() {
    },
    beforeUnmount() {
    }
}
</script>
