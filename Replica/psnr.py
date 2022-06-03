import cv2
import math
import numpy as np

def psnr1(img1, img2):
    # compute mse
    # mse = np.mean((img1-img2)**2)
    mse = np.mean((img1 / 1.0 - img2 / 1.0) ** 2)
    # compute psnr
    if mse < 1e-10:
        return 100
    psnr1 = 20 * math.log10(255 / math.sqrt(mse))
    return psnr1


def psnr2(img1, img2):
    mse = np.mean((img1 / 255.0 - img2 / 255.0) ** 2)
    if mse < 1e-10:
        return 100
    psnr2 = 20 * math.log10(1 / math.sqrt(mse))
    return psnr2

sum_psnr = 0.
for i in range(7):


    imag1 = cv2.imread("img_path\" + "%03d" %i + ".png")
    # print("imag1.shap: {}".format(imag1.shape))
    imag2 = cv2.imread("predictions\rgb_" + str(510 + i * 8) + ".png")
    # print("imag1.shap: {}".format(imag2.shape))
    image_size = (640, 480)  
    imag1 = cv2.resize(imag1, image_size, interpolation=cv2.INTER_CUBIC)
    imag1 = cv2.cvtColor(imag1, cv2.COLOR_BGR2GRAY)
    imag2 = cv2.resize(imag2, image_size, interpolation=cv2.INTER_CUBIC)
    imag2 = cv2.cvtColor(imag2, cv2.COLOR_BGR2GRAY)
    res1 = psnr1(imag1, imag2)
    sum_psnr = sum_psnr + res1
    print("res1:", res1)
    res2 = psnr2(imag1, imag2)
    print("res2:", res2)

psnr = sum_psnr / 7.
print("ave_psnr:", psnr)
