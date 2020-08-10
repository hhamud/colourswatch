from PIL import Image
import numpy as np
import math
import fire 
from abc import ABC, abstractmethod






class IColourSwatchDebug(ABC):
    pass



class createColourSwatch(IColourSwatchDebug):
    
    def __init__(self, width, height, topleftcolour, toprightcolour, bottomleftcolour=None, bottomrightcolour=None):
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


        self.topleftcolour = topleftcolour

        if type(topleftcolour) is not int:
            raise TypeError("Sorry, top left colour value of {} is not an integer value. Please input an integer value".format(topleftcolour))

        if topleftcolour < 0:
            raise ValueError("Sorry, top left colour value of {} must be greater than or equal to 0.".format(topleftcolour))

        if topleftcolour > 65535:
            raise ValueError("Sorry, top left colour value of {} must be less than 65536.".format(topleftcolour))



        self.toprightcolour = toprightcolour

        if type(toprightcolour) is not int:
            raise TypeError("Sorry, top right colour value of {} is not an integer value. Please input an integer value".format(toprightcolour))

        if toprightcolour < 0:
            raise ValueError("Sorry, top right colour value of {} must be greater than or equal to 0.".format(toprightcolour))

        if toprightcolour > 65535:
            raise ValueError("Sorry, top right colour value of {} must be less than 65536.".format(toprightcolour))


        self.bottomleftcolour = bottomleftcolour
        self.bottomrightcolour = bottomrightcolour


        if bottomleftcolour is not None and bottomrightcolour is None:
            raise ValueError("bottom right colour is missing. Please input a value for bottom right colour")


   
    def RGB565_to_RGB888(self, topleftcolour=0, toprightcolour=0, bottomleftcolour=0, bottomrightcolour=0):
        k = topleftcolour or toprightcolour or bottomleftcolour or bottomrightcolour
        R = math.trunc( k / 2048 )
        G = math.trunc( ( k % 2048) / 32 )
        B = k % 32

        r = (R)*8
        g = (G)*4
        b = (B)*8
     

        RGB888 = np.array([r,g,b])

       

        return RGB888

       

    
    def colourswatch(self):
        pixel_width = self.width
        pixel_height = self.height
        numpy_array = np.zeros([pixel_height, pixel_width, 3], dtype=np.uint8)
        Top_left_array = self.RGB565_to_RGB888(self.topleftcolour)
        Top_right_array = self.RGB565_to_RGB888(self.toprightcolour)

        if (self.bottomleftcolour and self.bottomrightcolour) is not None :

            if type(self.bottomleftcolour) is not int:
                raise TypeError("Sorry, bottom left colour value of {} is not an integer value. Please input an integer value".format(self.bottomleftcolour))

            if self.bottomleftcolour < 0:
                raise ValueError("Sorry, bottom left colour value of {} must be greater than or equal to 0.".format(self.bottomleftcolour))

            if self.bottomleftcolour > 65535:
                raise ValueError("Sorry, bottom left colour value of {} must be less than 65536.".format(self.bottomleftcolour))


            if type(self.bottomrightcolour) is not int:
                raise TypeError("Sorry, bottom right value of {} is not an integer value. Please input an integer value".format(self.bottomrightcolour))

            if self.bottomrightcolour  < 0:
                raise ValueError("Sorry, bottom right colour value of {} must be greater than or equal to 0.".format(self.bottomrightcolour))

            if self.bottomrightcolour > 65535:
                raise ValueError("Sorry, bottom right colour value of {} must be less than 65536.".format(self.bottomrightcolour))



            Bottom_left_array = self.RGB565_to_RGB888(self.bottomleftcolour)
            Bottom_right_array = self.RGB565_to_RGB888(self.bottomrightcolour)
            for i in range(0, pixel_height):
                for j in range(0, pixel_width):
                    numpy_array[i:i+1,j:j+1] = Top_left_array * (1-(i/(pixel_height-1)))*(1-(j/(pixel_width-1))) + Bottom_left_array * (i/(pixel_height-1)) * (1-(j/(pixel_width-1))) + Top_right_array * (1-(i/(pixel_height-1))) * (j/(pixel_width-1)) + Bottom_right_array * (i/(pixel_height-1)) * (j/(pixel_width-1))
                    
        else:
            for i in range(0, pixel_width):
                numpy_array[:,i:i+1] = Top_left_array * (1-(i/(pixel_width-1))) + Top_right_array * (1-(i/(pixel_width-1))) 

        
        

        numpy_image = Image.fromarray(numpy_array)
        numpy_image.save('test.png')
        


def main():
    fire.Fire(createColourSwatch)
    
       
    




if __name__ == "__main__":
    c1 = createColourSwatch(6,6,65535,0,0,65535)
    c1.colourswatch()
   







