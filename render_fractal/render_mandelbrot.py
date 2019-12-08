import math
import numpy as np


def render_mandelbrot(options):
    height = options['height']
    width = options['width']
    zoom = options['zoom']
    scale = 5.0
    while zoom:
        scale -= 0.1 * scale
        zoom -= 1
    x_offset = options['x'] * 0.1 * scale
    y_offset = options['y'] * 0.1 * scale
    pow = options['power']
    color = options['color']
    lim = int(50 * math.pow(math.log(10 / scale, 10), 1.2))
    if lim < 1000:
        lim = 1000
    pixels = np.zeros((height, width, 3), 'uint8')

    (rr, gg, bb) = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

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
            if n == lim:
                pixels[i][j][0] = 0
                pixels[i][j][1] = 0
                pixels[i][j][2] = 0


            else:
                 pixels[i][j][0] = rr
                 pixels[i][j][1] = gg
                 pixels[i][j][2] = int((lim - n) / lim * 100 * bb)

    return pixels
