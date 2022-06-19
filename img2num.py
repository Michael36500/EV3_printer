import cv2
import numpy as np
# from datetime import datetime
import pyperclip
from tqdm import tqdm

path = "spiderman3.png"

############################################################################################################################################################
#!! pozor na orientaci, teď je normálně (hlavou vzhůru)

#####################
# DĚLÁM ARRAY ČÍSEL #
#####################
def Nums(path):
    out = []
    multiout = []
    arli = []

    img = cv2.imread(path, 0)
    img = cv2.flip(img, 1)
    
    img = (255-img)
    
    img = img.astype(np.uint8)

        # protože pro další blok potřebuji jednodimenziální pole, ale může se hodit více, tak dělám pole OUT (jedno) a MULTIOUT (multi)
    th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    # print(img)
    for line in tqdm(img):
        for sgm in line:
            if sgm == 255:
                sgm = 1
            arli.append (sgm)
            out.append(sgm)
        out.append(2)
        arli.append(2)
        multiout.append (arli)
        arli = []

    ############################
    # ZJEDNODUŠENÍ + ZRYCHLENÍ #
    ############################    

    inp = out

    out = []

    hled = 0    # hledané
    cis = 0   # počet stejných za sebou




    for pos in tqdm(inp):
        if pos == 2:
            out.append (cis)
            cis = 0
            out.append (-1)
            hled = 0
            continue


        if pos != hled:
            hled = 1 if hled == 0 else 0 
            out.append (cis)
            cis = 0

        cis = cis + 1


    out.append (cis)
    
    out = "robot = " + str(out) + "   #{}".format(path)

    return out

# print(Nums(path))

# copy in clipboarad
syntax = Nums(path)
pyperclip.copy(syntax)
# print(syntax)
print("Copied") 