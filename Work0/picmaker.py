file = open("newImage.ppm", 'r')

file.write("P3 500 500 255 \n")

for w in range(500):
    for h in range(500):
        r = 255
        b = w % 256
        g = h % 256
        file.write(str(r) + ' ' + str(b) + ' ' + str(g) + ' ')

file.close()
