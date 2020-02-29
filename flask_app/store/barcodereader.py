from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2

def decode(bc) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(bc)
    # Print results
    for obj in decodedObjects:
        barNum = (obj.data).decode('utf-8')
        print('Type : ', obj.type)
        print('Data : ', barNum)
    return decodedObjects


# Main
def barcodereader(filename):
    # Read image
    bc = cv2.imread(filename)
    decodedObjects = decode(bc)
