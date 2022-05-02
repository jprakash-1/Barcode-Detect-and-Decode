import cv2
import matplotlib.pyplot as plt 
import os

# Update folder path here to display image
folder_path = "./data/all barcode/"

print("All images containg the given folder")
for filename in os.listdir(folder_path):
    path = folder_path + filename
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(img)

plt.show()