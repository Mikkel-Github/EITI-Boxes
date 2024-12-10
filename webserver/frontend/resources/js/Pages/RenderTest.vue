<script setup lang="ts">
import { defineProps, onMounted, ref } from 'vue'
import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'

// Define the props for dimensions and positions
const props = defineProps({
  boxDimensions: {
    type: Object as () => { height: number; width: number; length: number },
    default: () => ({ height: 10, width: 10, length: 10 })
  },
  boxPositions: {
    type: Array,
    default: () => [
      { x: 0, y: 0, z: 0 },
      { x: 5, y: 0, z: 1 },
      { x: 10, y: 0, z: 2 }
    ]
  }
})

// Create a ref for the container where the 3D canvas will be attached
const container = ref<HTMLElement | null>(null)

onMounted(() => {
    console.log(props.boxPositions)
  if (!container.value) return

  // Set up the basic scene
  const scene = new THREE.Scene()
  const camera = new THREE.PerspectiveCamera(65, container.value.clientWidth / container.value.clientHeight, 0.1, 1000)
  const renderer = new THREE.WebGLRenderer({ alpha: true })
  renderer.setSize(container.value.clientWidth, container.value.clientHeight)
  container.value.appendChild(renderer.domElement)

  scene.scale.set(100, 100, 100)

  // Set up the lighting
  const light = new THREE.AmbientLight(0xffffff, 1); // Ambient light
  scene.add(light)

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1)
  directionalLight.position.set(10, 10, 10).normalize() // Directional light
  scene.add(directionalLight)

  // Get positions and dimensions from props
  const positions = props.boxPositions
  const dimension = props.boxDimensions

  // Scale factor (cm to meters)
  const scaleFactor = 0.01 // 1 cm = 0.01 meters

  // Load GLTF model for the robot
  const loader = new GLTFLoader()
  loader.load(
    'http://localhost:8000/models/robot/mir_100.gltf', // Robot model URL
    (gltf) => {
      console.log('Robot model loaded:', gltf)
      const robot = gltf.scene

      // Apply any textures if available
      robot.traverse((child) => {
        if (child.isMesh && child.material.map) {
          const texture = child.material.map
          texture.encoding = THREE.sRGBEncoding
          texture.anisotropy = 16
        }
      })

      // Scale the robot model (assuming the model is in cm and we need to scale it)
      robot.scale.set(1, 1, 1)

      // Position the robot at (0, 0, 0)
      robot.position.set(0, 0, 0)

      // Add the robot to the scene
      scene.add(robot)
    },
    undefined,
    (error) => {
      console.error('Error loading robot model:', error)
    }
  )

  // Load GLTF model for the box
  loader.load(
    'http://localhost:8000/models/box/box.gltf', // Box model URL
    (gltf) => {
      console.log('Box model loaded:', gltf) // Check if the model is loaded
      const boxModel = gltf.scene

      // Apply texture to the box model if available
      boxModel.traverse((child) => {
        if (child.isMesh && child.material.map) {
          const texture = child.material.map
          texture.encoding = THREE.sRGBEncoding
          texture.anisotropy = 16
        }
      })

      // Convert scale and position to meters
      const instanceCount = positions.length
      const geometry = boxModel.children[0].geometry // Get the geometry of the first child mesh
      const material = boxModel.children[0].material // Get the material of the first child mesh
      const instancedMesh = new THREE.InstancedMesh(geometry, material, instanceCount)

      // Apply scale directly to InstancedMesh (box in meters)
      instancedMesh.scale.set(dimension.width, dimension.height, dimension.length)
      // Position the robot at (0, 0, 0)
      instancedMesh.position.set(0, 0, 0)

      positions.forEach((position) => {
        const boxClone = instancedMesh.clone() // Clone the model for each box

        // Set the position of each box directly based on the provided positions
        boxClone.position.set(
          position.x * scaleFactor, // Convert from cm to meters
          position.z * scaleFactor,
          position.y * scaleFactor
        )

        // Add the cloned box to the scene
        scene.add(boxClone)
      })

      // Update camera position based on spherical coordinates
      updateCameraPosition()
    },
    undefined,
    (error) => {
      console.error('Error loading box model:', error)
    }
  )

  // Variables for camera interaction
  const cameraDistance = 130
  let azimuthalAngle = Math.PI / 3.1 // Horizontal rotation (around Y axis)
  let polarAngle = Math.PI / 2.9 // Vertical rotation (around X axis)
  let distance = cameraDistance // Distance from the target point

  let isMouseDown = false
  let lastMouseX = 0
  let lastMouseY = 0

  // Mouse control for rotation and zoom
  const onMouseDown = (event: MouseEvent) => {
    isMouseDown = true
    lastMouseX = event.clientX
    lastMouseY = event.clientY
  }

  const onMouseMove = (event: MouseEvent) => {
    if (!isMouseDown) return

    const deltaX = event.clientX - lastMouseX
    const deltaY = event.clientY - lastMouseY

    azimuthalAngle += deltaX * 0.005
    polarAngle = Math.max(0.1, Math.min(Math.PI - 0.1, polarAngle - deltaY * 0.005))

    lastMouseX = event.clientX
    lastMouseY = event.clientY
  }

  const onMouseUp = () => {
    isMouseDown = false
  }

  const onMouseWheel = (event: WheelEvent) => {
    const delta = event.deltaY || event.detail || -event.wheelDelta
    distance += delta * 0.1
    distance = Math.max(50, Math.min(500, distance))
  }

  window.addEventListener('mousedown', onMouseDown)
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)
  window.addEventListener('wheel', onMouseWheel)

  function updateCameraPosition() {
    const x = distance * Math.sin(polarAngle) * Math.cos(azimuthalAngle)
    const y = distance * Math.cos(polarAngle)
    const z = distance * Math.sin(polarAngle) * Math.sin(azimuthalAngle)

    camera.position.set(x, y, z)
    camera.lookAt(new THREE.Vector3(0, 4, 0))
  }

  // Animation loop
  function animate() {
    requestAnimationFrame(animate)
    updateCameraPosition()
    renderer.render(scene, camera)
  }

  animate()
})
</script>

<template>
  <div ref="container" style="width: 100%; height: 100%; cursor: grab;"></div>
</template>
