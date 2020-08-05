from PIL import Image
import numpy as np
import itertools





class IColourSwatchDebug():
    
    def __init__(self, width, height, topLeftColour, topRightColour, BottomLeftColour=None, bottomRightColour=None):
        self.width = width
        self.height = height
        self.topLeftColour = topLeftColour
        self.topRightColour = topRightColour
        self.BottomLeftColour = BottomLeftColour
        self.bottomRightColour = bottomRightColour

    def RGB565_TO_RGB888(self):
        #RGB = (R*65536)+(G*256)+B 
        #RGB565 = (R*64*32) + (G *32) + B
        B = self.topLeftColour - R * 64 * 32 - G * 32
        G = (self.topLeftColour - B - R * 32 * 64)/32
        R = (self.topLeftColour - G*32 - B)/(64*32)

        gradient_array = []
        for i in range(0, self.width+1):
            gradient_value = self.topLeftColour - i * (self.topLeftColour/self.width)
            gradient_array.append(gradient_value)
        print(gradient_array)
            

            



    def createColourSwatch(self):
        #user inputs number
        #do linear interpolation between the numbers
        #
        #convert from RGB565 to RGB_default
        #interpolate from the gradient 
        numpy_array = np.zeros([self.height, self.width, 3], dtype=np.uint8)
        numpy_array[:,:100] = self.topLeftColour
        numpy_array[:,100:] = self.topRightColour
        numpy_image = Image.fromarray(numpy_array)
        numpy_image.save('test.png')






c1 = IColourSwatchDebug(6,1,65535, 0)
c1.RGB565_TO_RGB888()