from PIL import Image
import numpy as np





class IColourSwatchDebug():
    
    def __init__(self, width, height, topLeftColour, topRightColour, BottomLeftColour=None, bottomRightColour=None):
        self.width = width
        self.height = height
        self.topLeftColour = topLeftColour
        self.topRightColour = topRightColour
        self.BottomLeftColour = BottomLeftColour
        self.bottomRightColour = bottomRightColour

    def RGB565_TO_RGB888(self):
        pass



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



RBGA = [255, 255, 255]



c1 = IColourSwatchDebug(200,1,65535, 0)
c1.createColourSwatch()