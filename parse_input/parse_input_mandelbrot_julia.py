import getopt, sys
from .get_fractal_type import possible_options, possible_flags


def print_help():
    print('fractal_generator.py -f mandelbrot -a <picture_height> -b <picture_width> -x <x_point> -y <y_point> '
          '-z <zoom> -p <power> -c <color> -o <output_filename> --output_to_stdout=false')
    sys.exit(2)


def str_to_boolean(v):
  return v.lower() in ("yes", "true", "t", "1")


def parse_input_mandelbrot_julia(argv):
    options = {
        'fractal_type': 'mandelbrot',
        'height': 0,
        'width': 0,
        'x': -1,
        'y': -1,
        # i_pos and j_pos are only user for julia
        'i_pos': 0,
        'j_pos': 0,
        'zoom': 0,
        'power': 0,
        "color": "",
        'print_to_stdout': False,
        'output_filename': "fractal.png"
    }

    # opts = {}
    try:
        opts, args = getopt.getopt(
            argv,
            possible_options,
            possible_flags,
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
        elif opt == '--output_to_stdout':
            options['print_to_stdout'] = str_to_boolean(arg)
    # todo: validate the options
    return options
