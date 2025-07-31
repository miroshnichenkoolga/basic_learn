class Car:
    def __init__(self, brand, model, year, color):
        self.brand=brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False

    def print_info(self):
        status = "Двигатель запущен" if self.engine_started else "Двигатель выключен"
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Статус: {status}")
        print("-"*30)

car1 = Car("Toyota", "Camry", 2020, "черный")
car2=Car("Мерседес", "x5", 2015, "белый жемчуг")

car1.print_info()
car1.start_engine()
car1.print_info()
car2.print_info()
car2.start_engine()
car2.print_info()
