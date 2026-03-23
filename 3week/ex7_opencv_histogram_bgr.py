import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lena.png')

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title("BGR Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.xlim([0, 256])
    plt.show()

    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
