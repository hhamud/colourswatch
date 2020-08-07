from PIL import Image
import numpy as np
import itertools
import math





class IColourSwatchDebug():
    
    def __init__(self, width, height, topLeftColour=None, topRightColour=None, BottomLeftColour=None, bottomRightColour=None):
        self.width = width
        self.height = height
        self.topLeftColour = topLeftColour
        self.topRightColour = topRightColour
        self.BottomLeftColour = BottomLeftColour
        self.bottomRightColour = bottomRightColour

    def TopLeft_RGB565_TO_RGB888(self):
        R = math.trunc( self.topLeftColour / 2048 )
        G = math.trunc( (self.topLeftColour % 2048) / 32 )
        B = self.topLeftColour % 32

        r = (R)*8
        g = (G)*4 
        b = (B)*8
     

        RGB888 = [r,g,b]

       

        return RGB888

    def TopRight_RGB565_TO_RGB888(self):
        R = math.trunc( self.topRightColour / 2048 )
        G = math.trunc( (self.topRightColour % 2048 ) / 32 )
        B = self.topRightColour % 32

      

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = [r,g,b]

        

        return RGB888


    def BottomLeft_RGB565_TO_RGB888(self):
        R = math.trunc( self.BottomLeftColour / 2048 )
        G = math.trunc( (self.BottomLeftColour % 2048 ) / 32 )
        B = self.BottomLeftColour % 32

        

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = [r,g,b]

        

        return RGB888

    def BottomRight_RGB565_TO_RGB888(self):
        R = math.trunc( self.bottomRightColour / 2048 )
        G = math.trunc( (self.bottomRightColour % 2048 ) / 32 )
        B = self.bottomRightColour % 32

        

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = [r,g,b]

    

        return RGB888



    def createColourSwatch(self):
        pixel_width = self.width
        numpy_array = np.zeros([self.height, self.width, 3], dtype=np.uint8)
        Top_left_array = np.array(self.TopLeft_RGB565_TO_RGB888())
        Top_right_array = np.array(self.TopRight_RGB565_TO_RGB888())
        Bottom_left_array = np.array(self.BottomLeft_RGB565_TO_RGB888())
        Bottom_right_array = np.array(self.BottomRight_RGB565_TO_RGB888())



        for i in range(0, pixel_width):
            pixel_width = self.width
            numpy_array[i:,:] = Bottom_left_array + (i/(pixel_width-1))*(Bottom_right_array-Bottom_left_array)
            numpy_array[:,i:] = Top_left_array + (i/(pixel_width-1))*(Top_right_array-Top_left_array)
        

        numpy_image = Image.fromarray(numpy_array)
        numpy_image.save('test2.png')
        print(numpy_array)
        






if __name__ == "__main__":
    c1 = IColourSwatchDebug(6,6,65535, 0, 0, 65535)
    c1.createColourSwatch()
    


