import getopt, sys
from .get_fractal_type import possible_options


def print_help():
    print('fractal_generator.py -f mandelbrot -a <picture_height> -b <picture_width> -x <x_point> -y <y_point> '
          '-z <zoom> -p <power> -c <color> -o <output_filename>')
    sys.exit(2)


def parse_input_julia(argv):
    options = {
        'fractal_type': 'mandelbrot',
        'height': 0,
        'width': 0,
        'x': -1,
        'y': -1,
        'i_pos': 0,
        'j_pos': 0,
        'zoom': 0,
        'power': 0,
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
            options['x'] = float(arg)
        elif opt == '-y':
            options['y'] = float(arg)
        elif opt == '-z':
            options['zoom'] = float(arg)
        elif opt == '-i':
            options['i_pos'] = int(arg)
        elif opt == '-j':
            options['j_pos'] = int(arg)
        elif opt == '-p':
            options['power'] = float(arg)
        elif opt == '-c':
            options['color'] = arg.lstrip('#')
        elif opt == '-o':
            options['output_filename'] = arg
    # todo: validate the options
    return options
