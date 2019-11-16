import getopt, sys

possible_options = "hf:a:b:x:y:i:j:z:p:c:o:"
possible_flags = ['output_to_stdout=', ]
fractal_types = ['mandelbrot', 'julia']


def print_help():
    print('please specify the fractal type')
    print('fractal_generator.py -f <fractal_type>')
    print('possible fractal types: ', fractal_types)
    sys.exit(2)


def get_fractal_type(argv):
    fractal_type = ""

    opts = {}
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
            help()
        elif opt == "-f":
            fractal_type = arg
            if fractal_type not in fractal_types:
                print_help()
    return fractal_type
