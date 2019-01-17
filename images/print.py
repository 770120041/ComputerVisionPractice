import cv2


def read_image(IMG_NAME):
    print(IMG_NAME)
    img = cv2.imread(IMG_NAME,0)
    return img

IMG_NAME = 'crayons.bmp'

mosaic_img = read_image( IMG_NAME)# YOUR CODE HERE
print(mosaic_img.shape)





