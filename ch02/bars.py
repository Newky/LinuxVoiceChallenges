import csv, contextlib, math, random, sys, time, turtle

turtle.colormode(255)


@contextlib.contextmanager
def return_to_pos(tur):
    heading = tur.heading()
    pos = tur.pos()
    yield
    jump_to(tur, pos[0], pos[1])
    tur.setheading(heading)


@contextlib.contextmanager
def set_random_color(tur):
    current_color = tur.pencolor()
    random_color = lambda : (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tur.pencolor(random_color())
    yield
    tur.pencolor(current_color)


@contextlib.contextmanager
def change_orientation_do_something(tur, right_to_left=True):
    orientation = 1 if right_to_left else -1
    tur.right(90 * orientation)
    yield
    tur.left(90 * orientation)


def draw_tick(tur, label=None):
    with change_orientation_do_something(tur):
        tur.bk(2)
        tur.fd(4)
        tur.bk(2)

    if label:
       tur.write(label, align="left")


def draw_axis(tur, length, unit_size=5, ticks=True, labels=None, ticks_in_middle=True):
    jump_size = length / unit_size
    f1, f2 = (unit_size/2, ) * 2 if ticks_in_middle else (unit_size, 0)
    for i in xrange(jump_size):
        tur.forward(f1)
        if ticks:
            if not labels:
                draw_tick(tur)
            else:
                draw_tick(tur, labels[i])
        tur.forward(f2)


def draw_bar(tur, length=100, width=30, separator=5):
    with set_random_color(tur):
        tur.forward(separator)
        with change_orientation_do_something(tur, right_to_left=False):
            tur.forward(length)
        tur.forward(width)
        with change_orientation_do_something(tur):
            tur.forward(length)
        tur.forward(separator)


def jump_to(tur, x, y):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()


if __name__ == "__main__":
    csvfile = csv.reader(sys.stdin)
    lines = [row for row in csvfile]
    headers, lines = lines[0], lines[1:]
    maximum_y_val = max([long(l[1]) for l in lines])
    ranges = [float(l[1])/long(maximum_y_val) for l in lines]

    turs = [turtle.Turtle() for i in xrange(3)]
    [tur.shape("turtle") for tur in turs]

    max_x, max_y = turtle.screensize()
    start_x, start_y, seperator, y_ticks = -(max_x - 120), -(max_y - 50), 5, 5
    y_labels = [ (maximum_y_val/5) * i for i in xrange(1, 6) ]

    [jump_to(tur, start_x, start_y) for tur in turs]

    with return_to_pos(turs[0]):
        turs[0].left(90)
        draw_axis(turs[0], max_y, unit_size=(max_y/5), labels=y_labels, ticks_in_middle=False)

    with return_to_pos(turs[1]):
        draw_axis(turs[1], max_x, unit_size=(max_x/len(ranges)), labels=map(lambda l: l[0], lines))

    for r in ranges: draw_bar(turs[2], length=float(max_y)*r, width=(max_x/len(ranges)-5*2))

    [tur.hideturtle() for tur in turs]
    turtle.exitonclick()
