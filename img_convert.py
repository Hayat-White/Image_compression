from PIL import Image
import numpy as np
import math

user_file = input("What file would you like to convert:")
img = Image.open(user_file)
pixels = np.array(img)
### Change file to blackwhite and save image
column,row = img.size
blackwhite = [[0 for _ in range(row)] for _ in range(column)]
row_count = 0
column_count = 0
for y in range(row):
    for x in range(column):
        if ".PNG" in user_file:
            red, green, blue, _ = pixels[y][x]
        elif ".jpg" in user_file:
            red, green, blue = pixels[y][x]
        cell = math.floor(0.299 * red + 0.587 * green + 0.114 * blue)
        numberstr = str(cell)
        numberstr = numberstr[:-1] + "0"
        cell = int(numberstr)
        totalred = (2 * int(red)) - int(green) - int(blue)
        totalblue = (2 * int(blue)) - int(red) - int(green)
        totalgreen = (2 * int(green)) - int(red) - int(blue)
        if( totalred > 30): #red led by a lot
            cell += 1
        if( totalgreen > 30): #green led by a lot
            cell += 2
        if( totalblue > 30): #blue led by a lot
            cell += 7
            if cell > 255:
                cell -= 10
        # if( x==303 and y == 183):
        #     print(red, green, blue)
        #     print("red - blue + red - green: ",totalred)
        #     print("green - red + green - blue: ",totalgreen)
        #     print("blue - green + blue - red:",totalblue) 
        #     print("totalred: ",totalred,"totalblue:",totalblue,"totalgreen: ",totalgreen)
        #     print("cell - 1 % 10 :", (cell -1) % 10, "abs(totalgreen - totalblue):", abs(totalgreen - totalblue))
        if( (cell - 1) % 10 == 0 and int(green) > 40 and int(blue) > 100): # move red to pink
            cell += 3 # makes four
        if( (cell - 9) % 10 == 0 and int(red) < 120 and int(blue) > 130 and int(blue) - int(green) > 20):
            cell -= 4 # makes five
        if( (cell - 1) % 10 == 0 and int(green) > 120 and int(blue) < 70):
            cell += 5 # makes six

        blackwhite[x][y] = cell  # Assign the computed grayscale value
convertblackwhite_array = np.array(blackwhite, dtype=np.uint8)
convertblackwhite_img = Image.fromarray(convertblackwhite_array.T, mode="L")
convert_filename = user_file[:-4] + "_converted.PNG"
convertblackwhite_img.save(convert_filename)
del blackwhite, convertblackwhite_array, row_count, column_count
##########################################################################
### Open Blackwhite convert to change back into color
blackwhite_img = Image.open(convert_filename)
blackwhite_pixels = np.array(blackwhite_img)


##color_channel = blackwhite_pixels would create pointer, messes with modification later
red_channel = blackwhite_pixels.copy()
green_channel = blackwhite_pixels.copy()
blue_channel = blackwhite_pixels.copy()

for y in range(row):
    for x in range(column):
        value = blackwhite_pixels[y][x]

        if value % 10 == 1: #red
            red_channel[y][x] = np.clip(red_channel[y][x] * 3.33, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 0.25, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 0.25, 0, 255)

        elif value % 10 == 2: #green
            red_channel[y][x] = np.clip(red_channel[y][x] * 0.01, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 3.75, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 0.01, 0, 255)

        elif value % 10 == 3: #yellow
            red_channel[y][x] = np.clip(red_channel[y][x] * 1.25, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 1.25, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 0, 0, 255)
        
        elif value % 10 == 4: #pink
            red_channel[y][x] = np.clip(red_channel[y][x] * 3.33, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 0.90, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 0.90, 0, 255)

        elif value % 10 == 5: #light blue
            red_channel[y][x] = np.clip(red_channel[y][x] * 0.33, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 1, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 8, 0, 255)

        elif value % 10 == 6: #orange
            red_channel[y][x] = np.clip(red_channel[y][x] * 3.33, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 1, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 0.5, 0, 255)

        elif value % 10 == 7: #blue
            red_channel[y][x] = np.clip(red_channel[y][x] * 1, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 1, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] * 8, 0, 255)

        elif value % 10 == 8: #magenta
            red_channel[y][x] = np.clip(red_channel[y][x] / 0.45, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] * 0.10, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] / 0.45, 0, 255)

        elif value % 10 == 9: #cyan
            red_channel[y][x] = np.clip(red_channel[y][x] * 0.10, 0, 255)
            green_channel[y][x] = np.clip(green_channel[y][x] / 0.45, 0, 255)
            blue_channel[y][x] = np.clip(blue_channel[y][x] / 0.45, 0, 255)

        elif value % 10 == 0: #white
            red_channel[y][x] = blackwhite_pixels[y][x]
            green_channel[y][x] = blackwhite_pixels[y][x]
            blue_channel[y][x] = blackwhite_pixels[y][x]


color_pixels = np.stack((red_channel, green_channel, blue_channel), axis=-1).astype(np.uint8)
color_img = Image.fromarray(color_pixels, mode="RGB")
reconvert_filename = user_file[:-4] + "_reconverted_weighted.PNG"
color_img.save(reconvert_filename)

#################################
# print("First row of entries:")
# row_count = 0
# for row in pixels: # Reads in RGBA values [ (r)0 (g)0 (b)0 (alpha Channel(opaqueness))255 ]
#     if row_count == 0:
#         print(row)
#         print("Number of Entries:", len(row)) #number of entries
#     row_count+=1
# print("Number of Rows:",row_count)
# print("Format:", img.format)
# print("Size:", img.size)
# print("Mode:", img.mode)
#################################