## defining starting location (cannot be all 0.0 or else the calculations always yield 0)
x, y, z = 0.1, 0.0, 0.0

## defining constants (Lorenz's values)
a, b, c = 10, 28, 8/3

def setup():
    size(800, 600)
    background(0)

def draw():

    global x, y, z, a, b, c

    dt = 0.01                       ## time step for each frame
    dx = (a * (y - x)) * dt         ## change in x over time
    dy = (x * (b - z) - y) * dt     ## change in y over time
    dz = (x * y - c * z) * dt       ## change in z over time

    # adding change in x, y, and z
    x = x + dx
    y = y + dy
    z = z + dz

    stroke(255)                  ## set stroke color to white
    translate(width/2, height/2) ## move drawing pointer to center of screen
    scale(5)                     ## scale up the stroke size
    point(x, y)                  ## draw a point at x, y
