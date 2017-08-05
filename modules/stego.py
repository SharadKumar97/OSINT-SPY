from __future__ import absolute_import,unicode_literals
from steganography.steganography import Steganography

def hideText(carrier_path,secret_text):
    try:
        path=carrier_path
        output_path="stego.png"
        text=secret_text
        Steganography.encode(path,output_path,text)
    except:
        print "Try Again"
def findText(steg_img):
    try:
        secret_text=Steganography.decode(steg_img)
        print "Hidden text found :: "+secret_text
    except:
        print "Try Again"


