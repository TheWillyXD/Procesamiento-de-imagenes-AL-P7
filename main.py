import matplotlib.pyplot as plt
import numpy as np
from skimage import io

# Carga la imagen y normaliza los valores de píxeles a un rango de 0 a 1
image = io.imread("proyecto.jpg") / 255.0

# Crea una matriz de identidad anti-diagonal
anti_identidad = np.eye(image.shape[1])[::-1]

# Multiplica cada componente de color por la matriz de identidad anti-diagonal
img_red = np.matmul(image[:,:,0], anti_identidad)
plt.imsave("img_red.png", img_red, cmap='gray')
img_green = np.matmul(image[:,:,1], anti_identidad)
plt.imsave("img_green.png", img_green, cmap='gray')
img_blue = np.matmul(image[:,:,2], anti_identidad)
plt.imsave("img_blue.png", img_blue, cmap='gray')

# Crea una nueva imagen combinando los componentes de color procesados
reflex_img = np.zeros((image.shape[0], image.shape[1], image.shape[2]))
for c in range(image.shape[0]):
    for f in range(image.shape[1]):
        reflex_img[c, f, 0] = img_red[c, f]
        reflex_img[c, f, 1] = img_green[c, f]
        reflex_img[c, f, 2] = img_blue[c, f]

# Guarda la nueva imagen en un archivo
plt.imsave("img_reverse.png", reflex_img)

# Imprime las matrices resultantes de cada componente de color
print(img_red)
print(img_green)
print(img_blue)



