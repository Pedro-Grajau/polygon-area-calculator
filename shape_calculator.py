class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * self.height + 2 * self.width

  def get_picture(self):
    shape = ""
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    for i in range(self.height):
      shape += "*" * self.width + "\n"
    return shape

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def set_height(self, height):
    self.height = height

  def set_width(self, width):
    self.width = width

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()
    
class Square(Rectangle):
  def __init__(self, width):
    super().__init__(width, width)

  def __str__(self):
    return f'Square(side={self.width})'
  
  def set_side(self, side):
    self.width = side
    self.height = side
