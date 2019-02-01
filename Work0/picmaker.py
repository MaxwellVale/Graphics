file = open("newImage.ppm", 'w')

file.write("P3 600 600 255 \n")

for x in range(600):
    for y in range(600):
        r = 255
        b = int(x / 600. * 255)
        g = 255 - b

        file.write(str(r) + ' ' + str(b) + ' ' + str(g) + ' ')

file.close()
