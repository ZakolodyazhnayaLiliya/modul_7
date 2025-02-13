# Домашнее задание по теме "Позиционирование в файле"
# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.
# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
def custom_write(file_name, strings):
    # Открываем файл в режиме записи с кодировкой UTF-8
    with open(file_name, mode='w', encoding='utf-8') as file:
        strings_positions = {}

        # Проходимся по списку строк
        for i, string in enumerate(strings, start=1):
            #Синтаксис функции enumerate() выглядит следующим образом:

# Функция enumerate(iterable, start) принимает два параметра: iterable и start.
#iterable — это итерируемый объект (список, кортеж и т.д.), который будет возвращен в виде пронумерованного объекта (объекта enumerate)
#start — это начальный индекс для возвращаемого объекта enumerate. Значение по умолчанию равно 0, поэтому, если вы опустите этот параметр, в качестве первого индекса будет использоваться 0.
            # Сохраняем позицию текущей строки
            position = file.tell()

            # Записываем строку в файл с добавлением символа новой строки
            file.write(string + '\n')

            # Добавляем информацию о позиции строки в словарь
            strings_positions[(i, position)] = string

    return strings_positions


# Пример выполняемого кода:

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]

result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)