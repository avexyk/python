# Todas las pruebas tienen que estar en una clase
import unittest
from shopping_cart import Item, ShoppingCart,NotExistsItemError

class TestShoppingCart(unittest.TestCase):

  API_VERSION = 17

  # Acciones antes de que una prueba unitaria sea ejecutada
  def setUp(self):
    print('setUp antes de la prueba')
    self.pan = Item('Pan', 7.0)
    self.jugo = Item('Jugo', 5.0)
    self.shopping_cart = ShoppingCart()
    self.shopping_cart.add_item(self.pan)

  # Ejecución después de cada prueba unitaria
  def tearDown(self):
    print('tearDown después de la prueba')

  # Las pruebas unitarias tienen que ser métodos
  def test_cinco_mas_cinco_igual_diez(self):
    assert 5 + 5 == 10

  # def test_nombre_igual_pan(self):
  #   item = Item("Manzana", 12.0)
  #   self.assertEqual(item.name, "Manzana")

  # def test_nombre_diferente_manzana(self):
  #   item = Item("Pan blanco", 15.0)
  #   self.assertNotEqual(item.name, "Manzana")

  def test_nombre_igual_pan(self):
    # Compara dos valores
    # ==
    self.assertEqual(self.pan.name, "Pan")

  def test_nombre_diferente_manzana(self):
    self.assertNotEqual(self.jugo.name, "Juego")

  def test_contiene_productos(self):
    self.assertTrue(self.shopping_cart.contains_items())

  def test_no_contiene_productos(self):
    self.shopping_cart.remove_item(self.pan)
    self.assertFalse(self.shopping_cart.contains_items())

  def test_obtener_producto_pan(self):
    item = self.shopping_cart.get_item(self.pan)
    # Si dos objetos son el mismo objeto
    # Compara dos objetos
    # is
    self.assertIs(item, self.pan)
    self.assertIsNot(item, self.jugo)

  def test_excepcion_get_jugo(self):
    with self.assertRaises(NotExistsItemError):
      self.shopping_cart.get_item(self.jugo)

  def test_total_con_un_producto(self):
    total = self.shopping_cart.total()
    # Mayor
    self.assertGreater(total, 0)
    self.assertLess(total, self.pan.price + 1.0)
    self.assertEqual(total, self.pan.price
    )

  def test_codigo_pan(self):
    self.assertRegex(self.pan.code(), self.pan.name)

  def test_fail(self):
    # Si los hacer no cubren las necesidades
    if 3 > 4:
      self.fail("Dos no es mayor a tres")

  # Saltar pruebas(lo sabe el programador)
  @unittest.skip("Razones para saltar esta prueba")
  def test_prueba_skip(self):
    pass

  # Saltar pruebas(no lo sabe el programador)
  @unittest.skipIf(API_VERSION < 18, "Versión obsoleta")
  def test_prueba_condicional(self):
    pass

   # Saltar pruebas(no lo sabe el programador a falso)
  @unittest.skipUnless(False, "Evaluación a falso")
  def test_prueba_falso(self):
    pass

if __name__ == '__main__':
  unittest.main()