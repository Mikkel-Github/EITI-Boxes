<script setup lang="ts">
import { useGLTF } from '@tresjs/cientos'
import { shallowRef, watch, defineProps } from 'vue'

const { scene: model } = await useGLTF('http://127.0.0.1:8000/models/box/box.gltf')

// Define props for scale
const props = defineProps({
    scale: {
        type: Object,
        required: true,
        validator: (value) => (
            typeof value.height === 'number' &&
            typeof value.width === 'number' &&
            typeof value.length === 'number'
        ),
    },
    position: {
        type: Object,
        required: true,
        validator: (value) => (
            typeof value.x === 'number' &&
            typeof value.y === 'number' &&
            typeof value.z === 'number'
        ),
    },
})

const boxRef = shallowRef()

// Watch the scale prop and update model scale accordingly
watch(() => props.scale, (newScale) => {
    if (boxRef.value) {
        boxRef.value.scale.set(newScale.width, newScale.height, newScale.length)
    }
}, { immediate: true })

// Watch the position prop and update model position
watch(() => props.position, (newPosition) => {
    if (boxRef.value) {
        boxRef.value.position.set(newPosition.x, newPosition.y, newPosition.z)
    }
}, { immediate: true })

</script>

<template>
  <!-- Attach the 3D model to the scene, and bind the scale to the boxRef -->
  <primitive ref="boxRef" :object="model" cast-shadow receive-shadow />
</template>
