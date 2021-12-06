import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self,x1, y1, width, height, color):
        self.width = width
        self.height = height
        super(Box, self).__init__(x1, y1, color)

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        self.fillcolor = fillcolor
        super(BoxFilled, self).__init__(x1, y1, width, height, color)

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        self.radius = radius
        super(Circle, self).__init__(x1, y1, color)

    def draw_action(self):
        turtle.circle(self.radius)


class CircledFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        self.fillcolor = fillcolor
        super(CircledFilled, self).__init__(x1, y1, radius, color)

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


def main():
    b = Box(100,110,50,40,"red")

    print(b.x)
    print(b.y)
    print(b.width)
    print(b.height)
    print(b.color)

    b.draw()

    c = Box(-100, 100, 50, 20, "blue")
    c.draw()


    d = BoxFilled(1,2,3,4,"blue", "red")
    print(d.x)
    print(d.y)
    print(d.width)
    print(d.height)
    print(d.color)
    print(d.fillcolor)

    e = BoxFilled(1, 2, 100, 200, "red", "Blue")
    e.draw()

    f = Circle(29, 233, 40, 'black')
    f.draw()

    g = CircledFilled(40, 100, 40, "green", 'yellow')
    g.draw()


    turtle.done()



main()