from PIL import Image
import numpy as np
import itertools
import math





class IColourSwatchDebug():
    
    def __init__(self, width, height, topLeftColour, topRightColour, BottomLeftColour=None, bottomRightColour=None):
        self.width = width
        self.height = height
        self.topLeftColour = topLeftColour
        self.topRightColour = topRightColour
        self.BottomLeftColour = BottomLeftColour
        self.bottomRightColour = bottomRightColour

    def Left_RGB565_TO_RGB888(self):
        #RGB = (R*65536)+(G*256)+B 
        #RGB565 = (R*64*32) + (G *32) + B
        RL = math.trunc( self.topLeftColour / 2048 )
        GL = math.trunc( (self.topLeftColour % 2048) / 32 )
        BL = self.topLeftColour % 32

        print(RL, GL, BL)

        rL = (RL)*8
        gL= (GL)*4 
        bL = (BL)*8
     

        LRGB888 = [rL,gL,bL]

        print(LRGB888)

        return LRGB888

    def Right_RGB565_TO_RGB888(self):
        RR = math.trunc( self.topRightColour / 2048 )
        GR = math.trunc( (self.topRightColour % 2048 ) / 32 )
        BR = self.topRightColour % 32

        print(RR, GR, BR)

        rR = (RR)*8 
        gR= (GR)*4 
        bR = (BR)*8 

        RRGB888 = [rR,gR,bR]

        print(RRGB888)

        return RRGB888



    def createColourSwatch(self):
        #user inputs number
        #do linear interpolation between the numbers
        #
        #convert from RGB565 to RGB_default
        #interpolate from the gradient 
        splitter = self.width

        for i in range(0, splitter + 1):
            

        numpy_array = np.zeros([self.height, self.width, 3], dtype=np.uint8)
        numpy_array[:,:100] = self.Left_RGB565_TO_RGB888()
        numpy_array[:,100:] = self.Right_RGB565_TO_RGB888()


        numpy_image = Image.fromarray(numpy_array)
        numpy_image.save('test.png')






c1 = IColourSwatchDebug(200,100,2016, 0)
c1.createColourSwatch()
