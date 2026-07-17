import time
import pyvista as pv
import numpy as np
from pyvista import examples

# Download the high-resolution Stanford Bunny
# bunny = examples.download_bunny()
res = 50
plane = pv.Plane(i_resolution=res, j_resolution=res)

# 2. Get the number of cells on the plane
num_cells = plane.n_cells

# 3. Compute checkerboard cell data values (0 or 1)
# Each cell on a grid can be indexed by its (i, j) coordinates
i_res = res
j_res = res

# Generate grid coordinates for cells
cell_ids = np.arange(num_cells)
i_indices = cell_ids % i_res
j_indices = cell_ids // i_res

# Alternating pattern formula
checkerboard = (i_indices + j_indices) % 2

# 4. Assign the pattern to the plane's cell data
plane.cell_data['checkerboard'] = checkerboard
pl = pv.Plotter()
actor = pl.add_mesh(plane)

# Declare the uniform
actor.add_shader_replacement(
    'vertex',
    '//VTK::CustomUniforms::Dec',
    """
    uniform float u_time;
    uniform vec2 u_principal_point;
    uniform vec4 u_distortion_coeffs;
    uniform vec2 u_format_dims;
    uniform vec2 u_image_res;
    """,
    replace_first=True,
    replace_all=False
)

actor.add_shader_replacement(
    'vertex',
    '//VTK::Camera::Dec',
    """
    //VTK::Camera::Dec
    uniform mat4 VCDCMatrix;
    """
)

# Scale the Model Coordinates BEFORE clipping matrices are applied
actor.add_shader_replacement(
    'vertex',
    '//VTK::PositionVC::Impl',
    """
    // NOTE: Their code
    //VTK::PositionVC::Impl
    // NOTE: My code
    // Pulse scale between 0.5 and 1.5
    // float scale = sin(u_time * 5.0) * 0.5 + 1.0;
    float scale = 1.0;

    // Scale raw model coordinates
    vec4 myVertexMC = vec4(vertexMC.xyz * scale, vertexMC.w);
    // vec4 myVertexMC = vertexMC * scale;

    // Apply VTK's standard matrices
    vertexVCVSOutput = MCVCMatrix * myVertexMC;
    // gl_Position = MCDCMatrix * myVertexMC; // Clip space
    float z_depth = vertexVCVSOutput.z; // positive depth
    float x = vertexVCVSOutput.x / z_depth;
    float y = vertexVCVSOutput.y / z_depth;
    float rSquared = x * x + y * y;
    float k1 = u_distortion_coeffs[0]*sin(2.0*u_time);
    float k2 = u_distortion_coeffs[1]*sin(u_time);
    float p1 = u_distortion_coeffs[2];
    float p2 = u_distortion_coeffs[3];
    float radial = 1.0 + k1*rSquared + k2*rSquared*rSquared;
    float new_x = x * radial + 2*p1*x*y + p2*(rSquared + 2*x*x);
    float new_y = y * radial + 2*p2*x*y + p1*(rSquared + 2*y*y);
    // gl_Position = vec4(new_x * gl_Position.w, new_y * gl_Position.w, gl_Position.z, gl_Position.w);
    mat4 VCDCMatrix = MCDCMatrix * inverse(MCVCMatrix);
    gl_Position = VCDCMatrix * vec4(new_x * vertexVCVSOutput.z, new_y * vertexVCVSOutput.z, vertexVCVSOutput.zw);
    """,
    replace_first=True, 
    replace_all=False
)

uniforms = actor.GetShaderProperty().GetVertexCustomUniforms()
uniforms.SetUniform4f("u_distortion_coeffs", [2.9, 0.7, 0.0, 0.0])
uniforms.SetUniformMatrix4x4("VCDCMatrix", [1.0]*16)
start_time = time.time()
pl.show(interactive_update=True)



while True:
    elapsed = time.time() - start_time
    
    # Push the float directly to the existing u_time uniform
    uniforms.SetUniformf("u_time", elapsed)
    
    pl.update()
