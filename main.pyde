def setup():
    global x, y, z, a, b, c, points

    ## defining starting location (cannot be all 0.0 or else the calculations always yield 0)
    x, y, z = 0.1, 0.0, 0.0

    ## defining constants (Lorenz's values)
    a, b, c = 10, 28, 8/3

    points = []
    size(1000, 1000)
    background(0)

def draw():
    global x, y, z, a, b, c, points

    dt = 0.01                       ## time step for each frame
    dx = (a * (y - x)) * dt         ## change in x times time step (10 * (y - x)) * dt
    dy = (x * (b - z) - y) * dt     ## change in y times time step (x * (28 - z) - y) * dt
    dz = (x * y - c * z) * dt       ## change in z times time step (x * y - (8/3) * z) * dt

    # adding change in x, y, and z
    x = x + dx
    y = y + dy
    z = z + dz

    stroke(255)                  ## set stroke color to white
    translate(width/2, height/2) ## move drawing pointer to center of screen
    scale(12)                    ## scale up the stroke size

    background(0) ## draw background again cover points from last frame
        
    for i in points:      ## go through all points to draw them
        point(i[0], i[1]) ## draw a point at x, y for each point in list

        if len(points) > 750: ## trail off points after this number
            points.pop(0)

    points.append([x, y]) ## append point to points list so that they can be drawn in sequence and removed