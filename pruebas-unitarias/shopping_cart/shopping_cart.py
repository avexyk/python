class NotExistsItemError(Exception):
  pass

class Item:

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def code(self):
    return "{}-123456789".format(self.name)

  # Método que no se usa
  # def __str__(self):
  #   return self.name

class ShoppingCart:

  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def contains_items(self):
    return len(self.items) > 0

  def remove_item(self, item):
    self.items.remove(item)

  def get_item(self, item):
    if item not in self.items:
      raise NotExistsItemError('Item does not exist')
    else:
      return self.items[ self.items.index(item) - 1 ]
  
  def total(self):
    return sum([ item.price for item in self.items ])

  # Método para prueba en reporte web
  def last(self):
    # Retorna ultimo elemento de la lista
    return self.items[-1]