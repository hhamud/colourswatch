

### How the programme functions:

The programme intakes the initial RGB565 values and then converts these into RGB888 for the python pillow image package to display, it then applies the algorithm to create the colour matrix and displays the final result as a png file. The algorithm takes the average of all the corners of the matrix to calculate what each pixel should display.



### How to run the programme:
colourswatch --help 

This calls the doc strings of the class and also gives you a basic example on how to run it

To run the package:

colourswatch makeimage  --width=WIDTH --height=HEIGHT --topleftcolour=TOPLEFTCOLOUR --toprightcolour=TOPRIGHTCOLOUR 

optional arguments:

--bottomleftcolour=BOTTOMLEFTCOLOUR
--bottomrightcolour=BOTTOMRIGHTCOLOUR


