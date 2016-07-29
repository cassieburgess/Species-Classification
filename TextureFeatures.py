from PIL import Image 
from skimage.feature import greycomatrix, greycoprops

im = Image.open("P1110863.jpg").convert("L")
im.show()
glcm = greycomatrix(im, [10], [0])
matrix = greycoprops(glcm, 'dissimilarity')
