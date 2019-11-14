import sys
from parse_input import get_fractal_type, parse_input_mandelbrot


if __name__ == "__main__":
    argv = sys.argv[1:]
    fractal_type = get_fractal_type(argv)
    if fractal_type == 'mandelbrot':
        options = parse_input_mandelbrot(argv)
        print(options)
