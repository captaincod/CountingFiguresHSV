import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage.measure import label, regionprops


def hsv_scale(float_color):
    hsv_color = float_color * 360
    if hsv_color < 30 or hsv_color > 320:
        return 'красный'
    elif hsv_color < 50:
        return 'оранжевый'
    elif hsv_color < 70:
        return 'желтый'
    elif hsv_color < 140:
        return 'зеленый'
    elif hsv_color < 200:
        return 'голубой'
    elif hsv_color < 260:
        return 'синий'
    elif hsv_color < 290:
        return 'фиолетовый'
    else:
        return 'розовый'


def print_colors(arr):
    for obj_color in arr:
        colors[obj_color] += 1
    out = ''
    for color in colors:
        out += '\t' + str(color) + ' : ' + str(colors[color]) + '\n'
        colors[color] = 0
    return out


image = plt.imread('balls_and_rects.png')
image_to_hsv = color.rgb2hsv(image)
binary = np.sum(image, 2)
binary[binary > 0] = 1
labeled = label(binary)
regs = regionprops(labeled)

out_file = open('output.txt', 'w')

out_file.write(f'Всего объектов на изображении: {np.max(labeled)}\n')

rectangles = []
circles = []

for region in regs:
    object_color = image_to_hsv[int(region.centroid[0]), int(region.centroid[1])][0]
    if object_color == 'красный':
        plt.imshow(region.image)

    if region.extent == 1.0:
        rectangles.append(hsv_scale(object_color.round(3)))
    else:
        circles.append(hsv_scale(object_color.round(3)))

out_file.write(f'Количество прямоугольников: {len(rectangles)}\n')
out_file.write(f'Количество кругов: {len(circles)}\n')

colors = {'красный': 0, 'оранжевый': 0, 'желтый': 0, 'зеленый': 0, 'голубой': 0, 'синий': 0, 'фиолетовый': 0,
          'розовый': 0}


out_file.write(f'Цвета прямоугольников:\n')
out_file.write(print_colors(rectangles))
out_file.write(f'Цвета кругов:\n')
out_file.write(print_colors(circles))

out_file.close()

"""
plt.figure(figsize=(50, 50))
plt.imshow(image_to_hsv)
plt.savefig('imageHSV.png')
plt.show()
"""
