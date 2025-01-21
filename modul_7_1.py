# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
class Product:
    def __init__(self, name, weight, category):
        self.name = name  # Название продукта (строка)
        self.weight = weight  # Общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category  # Категория товара (строка)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
# и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name  # Приватный атрибут для хранения имени файла

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products): # Эта строка объявляет метод add для какого-то класса. Метод принимает произвольное количество аргументов через синтаксис *products, который позволяет передавать любое число объектов типа Product.
        existing_products = self.get_products().split('\n')
        # вызывается метод get_products() у текущего экземпляра (self), а затем результат разбивается на строки с помощью метода split('\n'). Это означает, что результат работы get_products() содержит список продуктов, каждый из которых находится на новой строке.
        existing_names = [product.split(', ')[0].strip() for product in existing_products]
# В этой строке создается список имен существующих продуктов. Для каждого продукта из списка existing_products берется первая часть строки до запятой (например, 'Apple, $10' превращается в 'Apple') и удаляются лишние пробелы методом strip().
        with open(self.__file_name, 'a+') as file:
# Открытие файла в режиме 'a+' означает, что файл будет открыт для добавления данных (режим 'a') и чтения (плюс). Если файл не существует, он будет создан автоматически.
            for product in products:
                # для каждого product из products проверяем условие
                if product.name not in existing_names:
                #  если наименования продукта нет в existing_names то
                    file.write(f"{product}\n") #  записываем продукт
                else: # иначе пышем, что продукт уже есть
                    print(f"Продукт {product.name} уже есть в магазине.")

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())