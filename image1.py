from skimage import data, io, filters

image = data.coins() # or any NumPy array!
edges = filters.sobel(image)
io.imshow(edges)
io.show()
