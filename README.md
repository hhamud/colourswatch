### To install the package

pip install git+ssh://git@github.com/hhamud/motilent_code_test.git



### what does this package contain:

The package contains:

1. colour gradient script
2. colour gradient tests
3. coverage folder of these tests
4. setup file
5. README
6. package info folder



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


