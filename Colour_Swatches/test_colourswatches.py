import unittest
from . import colourswatches
from PIL import Image
import numpy as np


class TestColours(unittest.TestCase):
    
    def test_width_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6.2,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,"asdsadsa",2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10, False,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,complex(6,5), 2016, 0)

    def test_height_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6.5,6,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch("asdsadsa",10 ,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(True, 6,2016,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(complex(6,5),6, 2016, 0)

    def test_topleftcolour_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6,2016.5, 0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10, 10,"asdsadsa",0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6, 6,True,0)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6, complex(6,5), 0)

    def test_toprightcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6,2016,0.5)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,10 ,2016,"asdsadsa")
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10, 6,2016,True)
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,6, 2016, complex(6,5))

    def test_bottomleftcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6,2016,0, 6.5, 6).makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,10 ,2016,0, "asdsadsa",10).makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10, 6,2016,0, True, 10).makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,6, 2016, 10,complex(6,5),10).makeimage()

    def test_bottomrightcolour_pixel_is_not_integer(self):
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(6,6,2016,0, 6, 6.5).makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,10 ,2016,0, 10,"asdsadsa").makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10, 6,2016,0, 10, True).makeimage()
        with self.assertRaises(TypeError):
            colourswatches.createColourSwatch(10,6, 2016, 10,10,complex(6,5)).makeimage()



    def test_negative_values(self):
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(-6,6,1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,-6,1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,-1,2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,1,-2, 1, 2)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,1,2, -1, 2).makeimage()
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,1,2, 1, -2).makeimage()


    def test_past_limit_values_for_colours(self):
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,1000000000,0)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,2016,1000000000)
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,2016,0, 1000000000, 0).makeimage()
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,2016,0, 0, 1000000000).makeimage()

    def test_color_must_have_two_or_four_values(self):
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(6,6,2016,0,0).makeimage()
    

    def test_double_single_pixel(self):      
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(1,1,2016,0)
         

    def test_zero_double_pixel(self):
        with self.assertRaises(ValueError):
            colourswatches.createColourSwatch(0,0, 2016, 0)

    def test_colour_swatch_algo_all(self):
        example = colourswatches.createColourSwatch(6,6,65535,0,0,65535).makeimage()
        algo = colourswatches.createColourSwatch(6,6,65535,0,0,65535).array_algorithm()
        image = Image.open("655350.png")
        a = np.asarray(image)
        np.testing.assert_array_equal(a,algo)

    
    def test_colour_swatch_algo_top(self):
        colourswatches.createColourSwatch(6,6,2016,0).makeimage()
        algo = colourswatches.createColourSwatch(6,6,2016,0).array_algorithm()
        image = Image.open('20160.png')
        a = np.asarray(image)
        np.testing.assert_array_equal(a,algo)  


        
        

            
            
        
              
              




