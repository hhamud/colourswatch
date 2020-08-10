from PIL import Image
import numpy as np
import math





class IColourSwatchDebug():
    
    def __init__(self, width, height, topLeftColour, topRightColour, bottomLeftColour=None, bottomRightColour=None):
        self.width = width

        if type(width) is not int:
            raise TypeError("Sorry, pixel width of {} is not an integer value. Please input an integer value".format(width))
    

        if width <= 0:
            raise ValueError("Sorry, pixel width value of {} must be greater than 0.".format(width))

       
        self.height = height

        if type(height) is not int:
            raise TypeError("Sorry, pixel height of {} is not an integer value. Please input an integer value".format(height))

        if height <= 0:
            raise ValueError("Sorry, pixel heigh value of {} must be greater than 0.".format(height))


        if height == 1 and width == 1:
            raise ValueError("Width and Height cannot be both 1 pixel, Please input a greater range of values")


        self.topLeftColour = topLeftColour

        if type(topLeftColour) is not int:
            raise TypeError("Sorry, top left colour value of {} is not an integer value. Please input an integer value".format(topLeftColour))

        if topLeftColour < 0:
            raise ValueError("Sorry, top left colour value of {} must be greater than or equal to 0.".format(topLeftColour))

        if topLeftColour > 65535:
            raise ValueError("Sorry, top left colour value of {} must be less than 65536.".format(topLeftColour))



        self.topRightColour = topRightColour

        if type(topRightColour) is not int:
            raise TypeError("Sorry, top right colour value of {} is not an integer value. Please input an integer value".format(topRightColour))

        if topRightColour < 0:
            raise ValueError("Sorry, top right colour value of {} must be greater than or equal to 0.".format(topRightColour))

        if topRightColour > 65535:
            raise ValueError("Sorry, top right colour value of {} must be less than 65536.".format(topRightColour))


        self.bottomLeftColour = bottomLeftColour
        self.bottomRightColour = bottomRightColour


        if bottomLeftColour is not None and bottomRightColour is None:
            raise ValueError("bottom right colour is missing. Please input a value for bottom right colour")


      



      
    

      

      
       

    def TopLeft_RGB565_TO_RGB888(self):
        R = math.trunc( self.topLeftColour / 2048 )
        G = math.trunc( (self.topLeftColour % 2048) / 32 )
        B = self.topLeftColour % 32

        r = (R)*8
        g = (G)*4
        b = (B)*8
     

        RGB888 = np.array([r,g,b])

       

        return RGB888

    def TopRight_RGB565_TO_RGB888(self):
        R = math.trunc( self.topRightColour / 2048 )
        G = math.trunc( (self.topRightColour % 2048 ) / 32 )
        B = self.topRightColour % 32

      

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = np.array([r,g,b])

        

        return RGB888


    def BottomLeft_RGB565_TO_RGB888(self):
        R = math.trunc( self.bottomLeftColour / 2048 )
        G = math.trunc( (self.bottomLeftColour % 2048 ) / 32 )
        B = self.bottomLeftColour % 32

        

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = np.array([r,g,b])

        

        return RGB888

    def BottomRight_RGB565_TO_RGB888(self):
        R = math.trunc( self.bottomRightColour / 2048 )
        G = math.trunc( (self.bottomRightColour % 2048 ) / 32 )
        B = self.bottomRightColour % 32

        

        r = (R)*8 
        g = (G)*4 
        b = (B)*8 

        RGB888 = np.array([r,g,b])

    

        return RGB888



    def createColourSwatch(self):
        pixel_width = self.width
        pixel_height = self.height
        numpy_array = np.zeros([pixel_height, pixel_width, 3], dtype=np.uint8)
        Top_left_array = self.TopLeft_RGB565_TO_RGB888()
        Top_right_array = self.TopRight_RGB565_TO_RGB888()

        if (self.bottomLeftColour and self.bottomRightColour) is not None :

            if type(self.bottomLeftColour) is not int:
                raise TypeError("Sorry, bottom left colour value of {} is not an integer value. Please input an integer value".format(self.bottomLeftColour))

            if self.bottomLeftColour < 0:
                raise ValueError("Sorry, bottom left colour value of {} must be greater than or equal to 0.".format(self.bottomLeftColour))

            if self.bottomLeftColour > 65535:
                raise ValueError("Sorry, bottom left colour value of {} must be less than 65536.".format(self.bottomLeftColour))


            if type(self.bottomRightColour) is not int:
                raise TypeError("Sorry, bottom right value of {} is not an integer value. Please input an integer value".format(self.bottomRightColour))

            if self.bottomRightColour  < 0:
                raise ValueError("Sorry, bottom right colour value of {} must be greater than or equal to 0.".format(self.bottomRightColour))

            if self.bottomRightColour > 65535:
                raise ValueError("Sorry, bottom right colour value of {} must be less than 65536.".format(self.bottomRightColour))



            Bottom_left_array = self.BottomLeft_RGB565_TO_RGB888()
            Bottom_right_array = self.BottomRight_RGB565_TO_RGB888()
            for i in range(0, pixel_height):
                for j in range(0, pixel_width):
                    numpy_array[i:i+1,j:j+1] = Top_left_array * (1-(i/(pixel_height-1)))*(1-(j/(pixel_width-1))) + Bottom_left_array * (i/(pixel_height-1)) * (1-(j/(pixel_width-1))) + Top_right_array * (1-(i/(pixel_height-1))) * (j/(pixel_width-1)) + Bottom_right_array * (i/(pixel_height-1)) * (j/(pixel_width-1))
                  
        else:
            for i in range(0, pixel_width):
                numpy_array[:,i:i+1] = Top_left_array * (1-(i/(pixel_width-1))) + Top_right_array * (1-(i/(pixel_width-1))) 



        numpy_image = Image.fromarray(numpy_array)
        numpy_image.save('test.png')
        return numpy_array
      
       
        






