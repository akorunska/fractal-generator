import sys
from parse_input import get_fractal_type, parse_input_mandelbrot_julia
from render_fractal import render_mandelbrot, render_julia
from PIL import Image
import numpy as np
import io


def output_result(options, pixels):
    np_result_array = np.asarray(pixels)
    img = Image.fromarray(np_result_array, "RGB")

    if options['print_to_stdout']:
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        print(imgByteArr)
    else:
        img.save(options['output_filename'])


if __name__ == "__main__":
    argv = sys.argv[1:]
    fractal_type = get_fractal_type(argv)

    if fractal_type == 'mandelbrot':
        options = parse_input_mandelbrot_julia(argv)
        pixels = render_mandelbrot(options)
    elif fractal_type == 'julia':
        options = parse_input_mandelbrot_julia(argv)
        pixels = render_julia(options)
    else:
        sys.exit(2)
    output_result(options, pixels)
