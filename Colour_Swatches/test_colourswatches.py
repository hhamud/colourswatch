import unittest
from . import colourswatches
from PIL import Image
import numpy as np


class TestColours(unittest.TestCase):
    
    def test_width_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6.2,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,"asdsadsa",2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10, False,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,complex(6,5), 2016, 0)

    def test_height_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6.5,6,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug("asdsadsa",10 ,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(True, 6,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(complex(6,5),6, 2016, 0)

    def test_topleftcolour_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6,2016.5, 0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10, 10,"asdsadsa",0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6, 6,True,0)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6, complex(6,5), 0)

    def test_toprightcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6,2016,0.5)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,10 ,2016,"asdsadsa")
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10, 6,2016,True)
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,6, 2016, complex(6,5))

    def test_bottomleftcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6,2016,0, 6.5, 6).createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,10 ,2016,0, "asdsadsa",10).createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10, 6,2016,0, True, 10).createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,6, 2016, 10,complex(6,5),10).createColourSwatch()

    def test_bottomrightcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(6,6,2016,0, 6, 6.5).createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,10 ,2016,0, 10,"asdsadsa").createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10, 6,2016,0, 10, True).createColourSwatch()
        with self.assertRaises(TypeError):
            colourswatches.IColourSwatchDebug(10,6, 2016, 10,10,complex(6,5)).createColourSwatch()



    def test_negative_values(self):
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(-6,6,1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,-6,1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,-1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,1,-2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,1,2, -1, 2).createColourSwatch()
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,1,2, 1, -2).createColourSwatch()


    def test_past_limit_values_for_colours(self):
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,1000000000,0)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,2016,1000000000)
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,2016,0, 1000000000, 0).createColourSwatch()
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,2016,0, 0, 1000000000).createColourSwatch()

    def test_color_must_have_two_or_four_values(self):
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(6,6,2016,0,0).createColourSwatch()
    

    def test_double_single_pixel(self):      
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(1,1,2016,0)
         

    def test_zero_double_pixel(self):
        with self.assertRaises(ValueError):
            colourswatches.IColourSwatchDebug(0,0, 2016, 0)

    def test_colour_swatch_algo_all(self):
        example = colourswatches.IColourSwatchDebug(6,6,2016,0,0,2016).createColourSwatch()
        image = Image.open("test.png")
        a = np.asarray(image)
        np.testing.assert_array_equal(a,example)

    
    def test_colour_swatch_algo_top(self):
        example = colourswatches.IColourSwatchDebug(6,6,2016,0).createColourSwatch()
        image = Image.open("test.png")
        a = np.asarray(image)
        np.testing.assert_array_equal(a,example)  


        
        

            
            
        
              
              




