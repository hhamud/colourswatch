from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="ColourSwatches",
    version="1.0",
    author='Hamza Hamud',
    description='Python commandline tool to create colour pixel gradients',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'fire',
        'pillow',
    ],
    entry_points='''
        [console_scripts]
        colourswatch=Colour_Swatches.colourswatches:main
         '''
         )