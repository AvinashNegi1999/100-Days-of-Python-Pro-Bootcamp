# Uncomment this part to extract colors from an image using colorgram
# import colorgram
# rgb_colors = []
# Extract 30 dominant colors from the given image path
# colors = colorgram.extract(r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 018\sample.jpg", 30)
# for color in colors:
#     r = color.rgb.r  # Red component
#     g = color.rgb.g  # Green component
#     b = color.rgb.b  # Blue component
#     new_color = (r, g, b)  # Create RGB tuple
#     rgb_colors.append(new_color)  # Add to list
# print(rgb_colors)  # Output the list of extracted colors

import turtle as t
import random

# Create turtle object and configure screen
tim = t.Turtle()
t.colormode(255)         # Use RGB color values up to 255
tim.penup()              # Don't draw lines between movements
tim.speed("fastest")     # Draw as fast as possible
tim.hideturtle()         # Hide turtle cursor for clean output

# Predefined color palette (can be extracted using colorgram)
color_list = [
    (252, 251, 248), (245, 251, 250), (253, 249, 252), (242, 245, 248), (139, 80, 53), 
    (185, 163, 125), (138, 166, 176), (60, 111, 134), (17, 42, 73), (139, 62, 88), 
    (162, 153, 44), (66, 119, 101), (147, 182, 171), (215, 210, 107), (76, 34, 29), 
    (69, 151, 163), (115, 39, 32), (96, 145, 119), (177, 148, 162), (74, 30, 35), 
    (168, 99, 127), (33, 56, 105), (104, 123, 165), (107, 40, 49), (175, 106, 90), 
    (209, 181, 194), (21, 96, 86), (169, 202, 196), (9, 97, 112), (220, 178, 172)
]

# Set the starting position for painting (bottom-left corner)
tim.setheading(225)   # Turn diagonally
tim.forward(300)      # Move back to bottom-left
tim.setheading(0)     # Face right

# Draw 10x10 dot painting using the color list
num_dots = 100
for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))  # Draw colored dot
    tim.forward(50)  # Move forward to space next dot

    # Move up to next row after every 10 dots
    if dot_count % 10 == 0:
        tim.setheading(90)   # Face up
        tim.forward(50)      # Move to next row
        tim.setheading(180)  # Face left
        tim.forward(500)     # Return to row start
        tim.setheading(0)    # Face right

# Keep window open until user clicks
screen = t.Screen()
screen.exitonclick()
