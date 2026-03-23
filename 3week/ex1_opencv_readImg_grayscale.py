import cv2

image = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 읽을 수 없습니다. 경로를 확인하세요.")
else:
    cv2.imshow('Lenna Grayscale', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
