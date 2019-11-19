import sys
import os
from PIL import Image

# Grab first and second arguments
try:
    input_directory = os.getcwd() + '\\' + sys.argv[1]
    output_directory = sys.argv[2]
except IndexError as err:
    print(f'You need to provide the input and output directories. {err}')
    sys.exit(1)

# Creating new directory
try:
    os.mkdir(output_directory)
except OSError:
    print('Directory already exists.')

# Loop input directory, convert images to png and saving them
for folders, subfolders, files in os.walk(input_directory):
    for file in files:
        filename, extension = file.split('.')
        
        img = Image.open(f'./Pokedex/{file}')
        img.save(f'{output_directory}/{filename}.png', 'png')
