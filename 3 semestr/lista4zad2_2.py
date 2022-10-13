"""
@sources: https://stackoverflow.com/questions/49588440/convert-jpg-images-to-dcm-images-using-python-script
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

# odczytanie obrazu w skali szarości
img = cv2.imread('moon.jpg', 0)

# projektowanie filtra Butterwortha
# czyli cyfrowego filtra dolnoprzepustowego
#------------------------------------------------------
def butterworth_filter(shape, n=0, D0=60):
    '''
    n = 2; # order value can change this value accordingly 
    D0 = 60; # cut-off frequency can change this value accordingly 
    '''
    M, N = shape
    # inicjacja wypełnienia filtra zerami
    H = np.zeros((M, N))

    # przepuszczenie "wyzerowanego" obrazu przez filtr
    for u in range(0, M):
        for v in range(0, N):
            # euklidesowa odległość od punktu D(u,v) do srodka
            D_uv = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
            # okreslenie maski filtrujacej 
            H[u, v] = 1/(1 + (D0/D_uv)**(2*n))
    return H
#-----------------------------------------------------

# ROZMYCIE OBRAZU
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
phase_spectrumR = np.angle(fshift)
magnitude_spectrum = 20*np.log(np.abs(fshift))
 
# wywolanie Filtra Butterworth 
H = butterworth_filter(img.shape)
# splot między obrazem przekształconym a maską
G = H * fshift
# wynik
result = np.abs(np.fft.ifft2(np.fft.ifftshift((G))))

#generacja obrazów
plt.subplot(222)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(221)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('magnitude spectrum')
plt.axis('off')

plt.subplot(223)
plt.imshow(H, "gray") 
plt.title("Butterworth Filter")
plt.axis('off')

plt.subplot(224)
plt.imshow(result, "gray") 
plt.title("Result")
plt.axis('off')

plt.show()

