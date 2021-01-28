import numpy as np
    
def main():
    img = np.random.rand(3,5)
    pic = Picture(img=img)
    print(img)
    print(pic.rotate_90_degrees())
    
class Picture(object):
    def __init__(self, img):
        self.img = img
        self.img_size1 = img.shape[0]
        self.img_size2 = img.shape[1]
    
    def rotate_90_degrees(self):
        img_rotated = np.zeros((self.img_size2, self.img_size1))
        for i in range(self.img_size1):
            for j in range(self.img_size2):
                img_rotated[j, self.img_size1 - i - 1] = self.img[i, j]
        return img_rotated
            
if __name__ == "__main__":
    main()