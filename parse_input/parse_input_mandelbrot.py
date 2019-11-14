import getopt, sys
from .get_fractal_type import possible_options

def print_help():
    print('fractal_generator.py -f mandelbrot -a <picture_height> -b <picture_width> -x <x_point> -y <y_point> '
          '-z <zoom> -p <power> -d <depth> -c <color> -o <output_filename>')
    sys.exit(2)


def parse_input_mandelbrot(argv):
    options = {
        'fractal_type': 'mandelbrot',
        'height': 0,
        'width': 0,
        'x': -1,
        'y': -1,
        'zoom': 0,
        'power': 0,
        'depth': 0,
        "color": "",
        'output_filename': "fractal.png"
    }

    # opts = {}
    try:
        opts, args = getopt.getopt(
            argv,
            possible_options,
        )
    except getopt.GetoptError:
        print_help()

    for opt, arg in opts:
        if opt == '-h':
            print_help()
        elif opt == '-a':
            options['height'] = int(arg)
        elif opt == '-b':
            options['width'] = int(arg)
        elif opt == '-x':
            options['x'] = int(arg)
        elif opt == '-y':
            options['y'] = int(arg)
        elif opt == '-z':
            options['zoom'] = int(arg)
        elif opt == '-p':
            options['power'] = int(arg)
        elif opt == '-d':
            options['depth'] = int(arg)
        elif opt == '-c':
            options['color'] = arg
        elif opt == '-o':
            options['output_filename'] = int(arg)
    # todo: validate the options
    return options
