import cv2

def img_to_bin(path):
    img = cv2.imread(path)
    height, width = img.shape[0], img.shape[1]
    grid = []
    white = (255, 255, 255)
    for i in range(height):
        l = []
        for j in range(width):
            t = tuple(img[i, j])
            if t == white:
                l.append(0)
            else:
                l.append(1)
        grid.append(l)
    return grid, height, width