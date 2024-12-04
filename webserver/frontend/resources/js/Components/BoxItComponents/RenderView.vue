<script setup lang="ts">
import { TresCanvas } from '@tresjs/core'

import { shallowRef } from 'vue'

const boxRef = shallowRef()

import { useRafFn } from '@vueuse/core'

const { pause, resume } = useRafFn(() => {
  if (boxRef.value) {
    boxRef.value.rotation.y += 0.01
  }
})
</script>

<template>
    <!-- Box sepcifications -->
    <div class="Box-Specification-Container Column Flex">
        <h2>Preview</h2>
        <div class="Column Flex">
            <!-- <img src="../../../images/mir_robot_with_boxes.png" style="max-width: 70%; margin: auto; border-radius: 20px; border: 3px solid #e9b66f;"/> -->
            <TresCanvas preset="realistic" shadows="true"> <!-- clear-color="#82DBC5" -->
                <TresPerspectiveCamera
                    :position="[3, 3, 3]"
                    :look-at="[0, 0, 0]" />
                <TresMesh
                    ref="boxRef"
                    receive-shadow
                    cast-shadow>
                    <TresBoxGeometry :args="[1, 1, 1]" />
                    <TresMeshToonMaterial color="orange" />
                </TresMesh>
                <TresAmbientLight :intensity="1" />
                <TresDirectionalLight
                    cast-shadow
                    :position="[1, 3, 3]"
                    :look-at="[0, 0, 0]"
                    :intensity="1"
                />
                <TresMesh
                    receive-shadow
                    :position="[0, -2, 0]"
                    :rotation="[-Math.PI / 2, 0, 0]" >
                    <TresPlaneGeometry :args="[10, 10, 10, 10]" />
                    <TresMeshStandardMaterial color="#f7f7f7" />
                </TresMesh>
            </TresCanvas>
        </div>
    </div>
</template>

<script lang="ts">

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

