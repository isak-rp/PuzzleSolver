import cv2
import numpy as np

# Crear una imagen negra
img = np.zeros((200, 200, 3), dtype="uint8")

# Dibujar un círculo verde
cv2.circle(img, (100, 100), 50, (0, 255, 0), -1)

# Mostrar la ventana
cv2.imshow("Test OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
