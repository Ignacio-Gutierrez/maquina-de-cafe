class MasterCoffeeMachine:

    def __init__(self):
        self.resources = {
            'coin': 0,
            'sugar': 250,
            'water': 6500,
            'coffee': 500,
            'milk': 2000,
            'chocolate': 20,
            'tea': 250,
        }
        self.recipies = {
            'coffee_alone': {
                'coffee': 7,
                'water': 200,
            },
            'coffee_double': {
                'coffee': 14,
                'water': 200,
            },
            'coffee_milk': {
                'coffee': 7,
                'water': 150,
                'milk': 50,
            },
            'coffee_milk_double': {
                'coffee': 14,
                'water': 150,
                'milk': 50,
            },
            'capuccino': {
                'coffee': 14,
                'chocolate': 1,
                'milk': 200
            },
            'tea_simple': {
                'tea': 20,
                'water': 200,
            },
        }

    def add_resource(self, type, amount):
        self.resources[type] += amount

    def chose_drink(self, election):
        self.election = election

    def chose_sugar(self, put_sugar):
        self.put_sugar = put_sugar

    def Drink_Maker(self, election):

        if self.resources['coin'] == 0:
            return 'Inserte una moneda'
        if self.resources['water'] < 200:
            return 'No hay agua'
        if self.resources['sugar'] < self.put_sugar:
            return 'No hay azucar'
        if election == 1:
            if self.resources['coffee'] < 7:
                return 'No hay café'
            else:
                self.resources['coffee'] -= 7
                self.resources['water'] -= 200
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Café Simple'
        if election == 2:
            if self.resources['coffee'] < 14:
                return 'No hay café'   
            else:
                self.resources['coffee'] -= 14  
                self.resources['water'] -= 200
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Café Doble'
        if election == 3:
            if self.resources['coffee'] < 7:
                return 'No hay café'
            if self.resources['milk'] < 50:
                return 'No hay leche'
            else:
                self.resources['coffee'] -= 7
                self.resources['milk'] -= 50
                self.resources['water'] -= 150
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Café con Leche'
        if election == 4:
            if self.resources['coffee'] < 14:
                return 'No hay café'
            if self.resources['milk'] < 50:
                return 'No hay leche'
            else:
                self.resources['coffee'] -= 14
                self.resources['milk'] -= 50
                self.resources['water'] -= 150
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Café Doble con Leche'
        if election == 5:
            if self.resources['coffee'] < 14:
                return 'No hay café'
            if self.resources['milk'] < 200:
                return 'No hay leche'
            if self.resources['chocolate'] < 1:
                return 'No hay chocolate'
            else:
                self.resources['coffee'] -= 14
                self.resources['milk'] -= 200
                self.resources['chocolate'] -= 1
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Capuchino'
        if election == 6:
            if self.resources['tea'] < 20:
                return 'No hay té'
            else:
                self.resources['tea'] -= 20
                self.resources['water'] -= 200
                self.resources['sugar'] -= self.put_sugar
                self.resources['coin'] -= 1
                return 'Haciendo Té' 