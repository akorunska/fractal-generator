import math
from PIL import Image
import numpy as np

def render_mandelbrot(options):
    height = options['height']
    width = options['width']
    scale = options['zoom']
    x_offset = options['x']
    y_offset = options['y']
    pow = options['power']
    color = options['color']
    lim = options['depth']
    pixels = [[0] * width] * height

    for i in range(height):
        for j in range(width):

            d = 2.0 * scale / width
            x = -scale + x_offset + j * d
            y = -scale * height / width + y_offset + i * d

            a = x
            b = y

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
            if n == 100:
                pixels[i][j] = 0
            else:
                pixels[i][j] = int((color ** 2) / (lim * (n + 1)))

    print(pixels)
    # np_result_array = np.asarray(pixels)
    # print(np_result_array)
    # img = Image.fromarray(np_result_array, "RGB")
    # if img.mode != 'RGB':
    #     img = img.convert('RGB')

    img = Image.fromarray(pixels, 'L')
    img.save('out.jpeg')