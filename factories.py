class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Circle: draw() method")

class Square(Shape):
    def draw(self):
        print("Square: draw() method")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Usage
factory = ShapeFactory()

circle = factory.create_shape('circle')
circle.draw()

square = factory.create_shape('square')
square.draw()
