// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
import { Suspense } from 'react'
import { Canvas } from '@react-three/fiber'
import { PerspectiveCamera, CameraControls, Environment } from '@react-three/drei'
import { useLoader } from '@react-three/fiber'
import { ColladaLoader } from 'three/examples/jsm/loaders/ColladaLoader.js'
// import './App.css'
function RobotPartMesh({ position }) {
  // Load the DAE file from the public folder
  const collada = useLoader(ColladaLoader, 'meca_500_r3_j3.dae')
  const mesh = collada.scene.children.find((child) => child.isMesh)

  if (!mesh) return null;

  // Render the scene contained within the Collada object
  return (
    <mesh position={position} scale={9} geometry={mesh.geometry}>
      <meshStandardMaterial wireframe color="hotpink" metalness={0.8} roughness={0.5} />
    </mesh>
  )
  // return (
  //   <mesh>
  //     <boxGeometry args={[3, 3, 3]} />
  //     <meshPhongMaterial />
  //   </mesh>
  // )
}

function App() {

  return (
    <>
      <div style={{ height: '100%', width: '100%', position: 'relative', display: 'flex', flexDirection: 'column' }}>
        <h1>Robot Viewer</h1>
        <Canvas >
          <PerspectiveCamera makeDefault position={[0, 3, 10]} />
          <CameraControls />
          <ambientLight intensity={1.2} />
          <directionalLight intensity={0.9} position={[1, 3, 5]} />
          <directionalLight intensity={0.9} position={[-1, -3, -5]} />
          <Suspense fallback={null}>
            <RobotPartMesh position={[1, 1, 1]} />
          </Suspense>
          <Environment preset={"park"} background={true} />
        </Canvas>
      </div>
    </>
  )
}




export default App
