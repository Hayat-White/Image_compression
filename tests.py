from PIL import Image
import numpy as np


user_file = input("What file would you like to convert:")
img = Image.open(user_file)
pixels = np.array(img)

#################################
print("First row of entries:")
row_count = 0
for row in pixels: # Reads in RGBA values [ (r)0 (g)0 (b)0 (alpha Channel(opaqueness))255 ]
    if row_count == 0:
        print(row)
        print("Number of Entries:", len(row)) #number of entries
    row_count+=1
print("Number of Rows:",row_count)
print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)
#################################