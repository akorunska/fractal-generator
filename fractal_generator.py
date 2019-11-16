import sys
from parse_input import get_fractal_type, parse_input_mandelbrot, parse_input_julia
from render_fractal import render_mandelbrot, render_julia

if __name__ == "__main__":
    argv = sys.argv[1:]
    fractal_type = get_fractal_type(argv)
    if fractal_type == 'mandelbrot':
        options = parse_input_mandelbrot(argv)
        render_mandelbrot(options)
    if fractal_type == 'julia':
        options = parse_input_julia(argv)
        render_julia(options)
