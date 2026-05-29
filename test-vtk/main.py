import vtkmodules.all as vtk  # pyright: ignore[reportMissingImports]


print('VTK Version:', vtk.vtkVersion.GetVTKVersion())
image = vtk.vtkImageData()
alg = vtk.vtkCellSizeFilter()
alg.SetInputDataObject(image)
alg.SetComputeVertexCount(True)
alg.Update()
