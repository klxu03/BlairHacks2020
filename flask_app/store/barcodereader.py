from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
from random import *

def decode(bc) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(bc)
    # Print results
    barNum = randint(0,1000000)
    for obj in decodedObjects:
        barNum = (obj.data).decode('utf-8')
    return barNum


# Main
def barcodereader(filename):
    # Read image
    bc = cv2.imread(filename)
    decodedObjects = decode(bc)
    return decodedObjects
