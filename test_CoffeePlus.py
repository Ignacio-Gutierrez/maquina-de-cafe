from Coffee_Plus import MasterCoffeeMachine

import unittest

class CoffeeMachineTest(unittest.TestCase):

    def test_initial_not_coin(self):
        machine = MasterCoffeeMachine()
        self.assertEqual(machine.resources['coin'], 0)
        self.assertEqual(machine.Drink_Maker(0), 'Inserte una moneda')

    def test_insert_coin(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        self.assertEqual(machine.resources['coin'], 1)

    def test_insert_coffee_second_time(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coffee', 1000)
        machine.add_resource('coffee', 1000)
        self.assertEqual(machine.resources['coffee'], 500+1000+1000)
    
    def test_insert_milk_tea_sugar(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('milk', 1000)
        machine.add_resource('milk', 500)
        machine.add_resource('tea', 150)
        machine.add_resource('tea', 300)
        machine.add_resource('sugar', 200)
        self.assertEqual(machine.resources['milk'], 1000+500+2000)
        self.assertEqual(machine.resources['tea'], 150+300+250)
        self.assertEqual(machine.resources['sugar'], 250+200)

    def test_not_water(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('water', -6500) 
        self.assertEqual(machine.Drink_Maker(0), 'No hay agua') 
        self.assertEqual(machine.resources['water'], 6500-6500)

    def test_not_coffee(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('coffee', -500) 
        machine.chose_sugar(1)
        self.assertEqual(machine.Drink_Maker(1), 'No hay café') 
        self.assertEqual(machine.resources['coffee'], 500-500)

    def test_not_sugar(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('sugar', -250)
        machine.chose_sugar(1)
        self.assertEqual(machine.Drink_Maker(1), 'No hay azucar') 
        self.assertEqual(machine.resources['sugar'], 250-250)

    def test_not_milk(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('milk', -2000)
        machine.chose_sugar(1) 
        self.assertEqual(machine.Drink_Maker(3), 'No hay leche') 
        self.assertEqual(machine.resources['milk'], 2000-2000)

    def test_not_chocolate(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('chocolate', -20) 
        machine.chose_sugar(1)
        self.assertEqual(machine.Drink_Maker(5), 'No hay chocolate') 
        self.assertEqual(machine.resources['chocolate'], 20-20)

    def test_not_tea(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('tea', -250) 
        machine.chose_sugar(1)
        self.assertEqual(machine.Drink_Maker(6), 'No hay té') 
        self.assertEqual(machine.resources['tea'], 250-250)

    def test_get_cafe_alone(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.chose_sugar(1)
        self.assertEqual(machine.Drink_Maker(1), 'Haciendo Café Simple')
        self.assertEqual(machine.resources['water'], 6500-200)
        self.assertEqual(machine.resources['coffee'], 500-7)
        self.assertEqual(machine.resources['sugar'], 250-1)
        self.assertEqual(machine.resources['coin'], 1-1)

    def test_get_cafe_double(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.chose_sugar(2)
        self.assertEqual(machine.Drink_Maker(2), 'Haciendo Café Doble')
        self.assertEqual(machine.resources['water'], 6500-200)
        self.assertEqual(machine.resources['coffee'], 500-14)
        self.assertEqual(machine.resources['sugar'], 250-2)
        self.assertEqual(machine.resources['coin'], 1-1)

    def test_get_coffee_milk_ok(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.add_resource('water', 500)    
        machine.chose_sugar(3)
        self.assertEqual(machine.Drink_Maker(3), 'Haciendo Café con Leche')
        self.assertEqual(machine.resources['water'], 6500+500-150)
        self.assertEqual(machine.resources['coffee'], 500-7)
        self.assertEqual(machine.resources['sugar'], 250-3)
        self.assertEqual(machine.resources['milk'], 2000-50)
        self.assertEqual(machine.resources['coin'], 1-1)

    def test_get_coffee_milk_double_ok(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.chose_sugar(3)
        self.assertEqual(machine.Drink_Maker(4), 'Haciendo Café Doble con Leche')
        self.assertEqual(machine.resources['water'], 6500-150)
        self.assertEqual(machine.resources['coffee'], 500-14)
        self.assertEqual(machine.resources['sugar'], 250-3)
        self.assertEqual(machine.resources['milk'], 2000-50)
        self.assertEqual(machine.resources['coin'], 1-1)

    def test_get_capuccino_ok(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.chose_sugar(5)
        self.assertEqual(machine.Drink_Maker(5), 'Haciendo Capuchino')
        self.assertEqual(machine.resources['water'], 6500)
        self.assertEqual(machine.resources['coffee'], 500-14)
        self.assertEqual(machine.resources['sugar'], 250-5)
        self.assertEqual(machine.resources['chocolate'], 20-1)
        self.assertEqual(machine.resources['milk'], 2000-200)
        self.assertEqual(machine.resources['coin'], 1-1)

    def test_get_tea_simple_ok(self):
        machine = MasterCoffeeMachine()
        machine.add_resource('coin', 1)
        machine.chose_sugar(5)
        self.assertEqual(machine.Drink_Maker(6), 'Haciendo Té')
        self.assertEqual(machine.resources['water'], 6500-200)
        self.assertEqual(machine.resources['tea'], 250-20)
        self.assertEqual(machine.resources['sugar'], 250-5)
        self.assertEqual(machine.resources['coin'], 1-1)

if __name__ == "__main__":
    unittest.main()