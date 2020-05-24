"""Pencil sketch effect."""


import os
import cv2


IMG = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "/image.jpg")
CARTOON_IMG = cv2.stylization(IMG, sigma_s=60, sigma_r=0.07)
cv2.namedWindow("Original Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Original Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Original Image", IMG)
cv2.waitKey()
cv2.namedWindow("Watercolor Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Watercolor Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Watercolor Image", CARTOON_IMG)
cv2.waitKey()
DST_GRAY, DST_COLOR = cv2.pencilSketch(IMG, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.namedWindow("Pencil Sketch (Grayscale) Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Pencil Sketch (Grayscale) Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Pencil Sketch (Grayscale) Image", DST_GRAY)
cv2.waitKey()
cv2.namedWindow("Pencil Sketch (Color) Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Pencil Sketch (Color) Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Pencil Sketch (Color) Image", DST_COLOR)
cv2.waitKey()
cv2.destroyAllWindows()
