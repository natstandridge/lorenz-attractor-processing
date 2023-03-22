def setup():
    global a, b, c, x, y, z, points

    ## defining starting location (cannot be all 0.0 or else the calculations always yield 0)
    x, y, z = 0.1, 0.0, 0.0

    ## defining constants (Lorenz's values)
    a, b, c = 10, 28, 8/3

    points = []
    size(1920, 1080)
    background(0)

def draw():
    global x, y, z, a, b, c, points

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

    background(0) ## draw background again cover points from last frame
        
    for i in points:
        point(i[0], i[1]) ## draw a point at x, y for each point in list

        if len(points) > 250: ## trail off points after this number
            points.pop(0)

    points.append([x, y])

