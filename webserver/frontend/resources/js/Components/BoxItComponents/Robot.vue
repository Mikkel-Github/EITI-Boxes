<script setup lang="ts">
import { useGLTF } from '@tresjs/cientos'
import { ref, onMounted } from 'vue'

// Load the model
const { scene: model } = await useGLTF('http://localhost:8000/models/robot/mir_100.gltf')

// Create a reference to manage the position
const position = ref({ x: 0, y: 0, z: 0 })

onMounted(() => {
  // Set the model's initial position
  model.position.set(position.value.x, position.value.y, position.value.z)
})
</script>

<template>
  <!-- Attach the 3D model to the scene -->
  <primitive :object="model" cast-shadow receive-shadow />
</template>
