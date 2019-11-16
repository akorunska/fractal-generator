import math
from PIL import Image
import numpy as np


def render_julia(options):
    height = options['height']
    width = options['width']
    zoom = options['zoom']
    scale = 5.0
    while zoom:
        scale -= 0.1 * scale
        zoom -= 1
    x_offset = options['x'] * 0.1 * scale
    y_offset = options['y'] * 0.1 * scale
    i_pos = options['i_pos']
    j_pos = options['j_pos']
    pow = options['power']
    color = options['color']
    lim = 50 * math.pow(math.log(10 / scale, 10), 1.2)
    if lim < 20:
        lim = 20
    pixels = np.zeros((height, width, 3), 'uint8')

    (r, g, b) = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    for i in range(height):
        for j in range(width):

            d = 2.0 * scale / width

            x = -scale + x_offset + j * d
            y = -scale * height / width + y_offset + i * d

            a = x
            b = y

           # x = -scale + (x_offset + i_pos) * d
           # y = -scale * height / width + (y_offset + j_pos) * d

            x = x_offset * d + (i_pos * 4.0 / width - 2.0)
            y = y_offset * d + (j_pos * 4.0 / width - 2.0)


            n = 0
            while n < lim:
                z = (math.sqrt(a**2 + b**2)) ** pow
                phi = math.atan2(b,a) * pow
                a = z * math.cos(phi)
                b = z * math.sin(phi)
                a += x
                b += y
                if a**2 + b**2 > 4:
                    break
                n += 1
            if n == lim:
                pixels[i][j][0] = 0
                pixels[i][j][1] = 0
                pixels[i][j][2] = 0

            else:
                pixels[i][j][0] = int(n / lim * r) % 256
                pixels[i][j][1] = int(n / lim * g) % 256
                pixels[i][j][2] = int(n / lim * b) % 256


    np_result_array = np.asarray(pixels)
    img = Image.fromarray(np_result_array, "RGB")

    img.save(options['output_filename'])