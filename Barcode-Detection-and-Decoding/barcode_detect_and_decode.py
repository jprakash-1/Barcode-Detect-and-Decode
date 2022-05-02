from pyzbar import pyzbar
import cv2
from datetime import datetime
import os

folder = "data/missing barcode/"
f = open("Results/barcodeOutput.txt", "a")
for filename in os.listdir(folder):
    image = cv2.imread(folder+filename)
    # 
    barcodes = pyzbar.decode(image)

    path = "Results/output" + str(filename)
    f.write(f'Barcode output of image: {folder + filename} \n \n')
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        text = "{} ( {} )".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

        f.write("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))

    image = cv2.resize(image, (1080, 720))
    # cv2.imshow("Image", image)
    cv2.imwrite(path,image)
    # cv2.waitKey(0)