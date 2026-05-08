console.log("Inside app.js");
console.log(document.body);

const myWebGPUCanvas: HTMLCanvasElement|null = document.querySelector("#myWebGPUCanvas");

// Getting an adapter returns a promise, so we put it in an async function.
async function main() {
	
	// 1. We first need to get access to the GPUAdapter and GPUDevice objects.
	if (!navigator.gpu) {
	  throw Error("WebGPU not supported.");
	}

	// The WebGPU Adapter's role is mainly inspection to know the capabilities of the device.
	// ANALOGY: the Adapter is a car rental agency's catalog. You look through it to see 
	// which cars have four-wheel drive or enough trunk space. The Device is the actual car 
	// you’ve signed the papers for and are currently driving.
	const adapter: GPUAdapter|null = await navigator.gpu.requestAdapter();
	if (!adapter) {
		throw Error("Couldn't request a GPUAdapter");
	}

	// The WebGPU Device is the object we interact with to use the gpu.
	const device: GPUDevice = await adapter.requestDevice()
	console.log(adapter, device);

	
	// ---------------------------------------------------------------------------------------
	// 2. We get the canvas drawing context.
	const context: GPUCanvasContext|null|undefined = myWebGPUCanvas?.getContext("webgpu");
	if (!context) {
		throw Error("Failed to get canvas drawing context.");
	}

	// We get the GPUTextureFormat which is optimal on this system for displaying 8 bit, 
	// standard dynamic range content. (either bgra8unorm or rgba8unorm)
	const presentationFormat = navigator.gpu.getPreferredCanvasFormat();

	// Assign a GPUDevice and the optimal presentationFormat to the drawing context of the canvas.
	context.configure({
	  device,
	  format: presentationFormat,
	});


	// 3. We create a GPUShaderModule which contains a vertex & fragment shader.
	//
	const module = device.createShaderModule({
	  label: 'our hardcoded red triangle shaders', // named for debug purposes
	  code: /* wgsl */ `
	    // This vertex shader function => runs once per vertex.
	    // In “triangle-list” mode, every 3 times the vertex shader is executed a triangle will be drawn connecting the 3 position values we return.
	    @vertex fn vs(
	      @builtin(vertex_index) vertexIndex : u32 // This is the index of the current vertex.
	    ) -> @builtin(position) vec4f { //  tells GPU this return value = clip-space position of vertex. {x, y, z, w}

	      // This is an array of clip space coordinates.
	      let pos = array(
	        vec2f( 0.0,  0.5),  // top center
	        vec2f(-0.5, -0.5),  // bottom left
	        vec2f( 0.5, -0.5)   // bottom right
	      );
	
	      return vec4f(pos[vertexIndex], 0.0, 1.0);
	    }
	
	    // This fragment shader function => runs once per pixel covered by triangle.
	    @fragment fn fs() -> @location(0) vec4f { // location(0) indicates that the output goes to color attachment 0.
	      return vec4f(0.0, 1.0, 0.0, 1.0); // Colors every pixel red.
	    }
	  `,
	});


	// 4. Create a render pipeline.
	const pipeline = device.createRenderPipeline({
	  label: 'our hardcoded red triangle pipeline',
	  layout: 'auto',
	  vertex: {
	    entryPoint: 'vs',
	    module,
	  },
	  fragment: {
	    entryPoint: 'fs',
	    module,
	    targets: [{ format: presentationFormat }],
	  },
	});

	// 5.
	const renderPassDescriptor = {
	  label: 'our basic canvas renderPass',
	  colorAttachments: [
	    {
	      view: GPUTextureView, //<- to be filled out when we render
	      clearValue: [0.9, 0.3, 0.3, 1],
	      loadOp: 'clear',
	      storeOp: 'store',
	    },
	  ],
	};

	function render() {
		// Get the current texture from the canvas context and
		// set it as the texture to render to.
		renderPassDescriptor.colorAttachments[0].view = context.getCurrentTexture().createView();
	
		// make a command encoder to start encoding commands
		const encoder = device.createCommandEncoder({ label: 'our encoder' });
	
		// make a render pass encoder to encode render specific commands
		const pass = encoder.beginRenderPass(renderPassDescriptor);
		pass.setPipeline(pipeline);
		pass.draw(3);  // call our vertex shader 3 times
		pass.end();
		
		const commandBuffer = encoder.finish();
		device.queue.submit([commandBuffer]);
	}
	
	render();
}

main()
