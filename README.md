# fractal-generator

This is a command-line tool for creating pictures of fractals.

### setting up and running
You have to have python v3.6.8+ installed beforehand.
It would also be nice to have virtualenv installed as well, but it's not necessary.

Create env and install requirements:
```
python3 -m virtualenv -p $(which python3) env/
source env/bin/activate
pip install -r requirements.txt
```

### usage

```
python fractal_generator.py -f mandelbrot  -a 500 -b 500 -x -4 -y 0 -z 14.0 -p 2 -c \#5f9e9a -o my_mandelbrot.png
python fractal_generator.py -f mandelbrot  -a 500 -b 500 -x -9 -y -7 -z 20.0 -p 2 -c \#f025aa -o my_mandelbrot.png

```
Will render mandelbrot fractal and save is as my_mandelbrot.png.
You are welcome to play around with the parameters and see where it leads you.

_made by @akorunska with love_