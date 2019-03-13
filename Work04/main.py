from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

# parse_file( 'script', edges, transform, screen, color )

add_curve(edges, 250, 100, 270, 175, 270, 250, 260, 325, 0.01, "bezier")
add_curve(edges, 250, 100, 230, 175, 230, 250, 240, 325, 0.01, "bezier")
add_circle(edges, 250, 340, 0, 20, 0.01)

add_curve(edges, 270, 270, 350, 420, 450, 475, 475, 450, 0.01, "bezier")
add_curve(edges, 475, 450, 470, 375, 460, 300, 400, 225, 0.01, "bezier")
add_curve(edges, 400, 225, 450, 175, 475, 125, 350, 75, 0.01, "bezier")
add_curve(edges, 350, 75, 285, 108, 280, 141, 265, 175, 0.01, "bezier")

add_curve(edges, 230, 270, 150, 420, 50, 475, 25, 450, 0.01, "bezier")
add_curve(edges, 25, 450, 30, 375, 40, 300, 100, 225, 0.01, "bezier")
add_curve(edges, 100, 225, 50, 175, 25, 125, 150, 75, 0.01, "bezier")
add_curve(edges, 150, 75, 215, 108, 220, 141, 235, 175, 0.01, "bezier")

add_curve(edges, 255, 360, 265, 400, 275, 430, 285, 420, 0.01, "bezier")
add_curve(edges, 245, 360, 235, 400, 225, 430, 215, 420, 0.01, "bezier")


draw_lines(edges, screen, color)

display(screen)
save_extension(screen, "curvy.png")
