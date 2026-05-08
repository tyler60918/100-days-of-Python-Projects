import colorgram

rgb_colors = []
colors = colorgram.extract("./Final Project/image.png", 17)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
print(rgb_colors)
