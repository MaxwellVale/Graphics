from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

# parse_file( 'newScript', edges, polygons, csystems, screen, color )
c = 50
r1 = 10
r2 = 20
num = 0
while num < 50:
    add_torus(polygons, c, c, c, r1, r2, 20)
    c += 10
    num += 1
draw_polygons(polygons, screen, color)
display(screen)
save_extension(screen, "moreGal.png")
