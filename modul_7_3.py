# Домашнее задание по теме "Оператор "with'
# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', '-']  # добавили дефис отдельно
        for filename in self.file_names:
            words = []
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    # Убираем знаки препинания и переводим все символы в нижний регистр
                    clean_line = ''.join(char.lower() for char in line if char not in punctuation)
                    # Разделяем строку на отдельные слова
                    words.extend(clean_line.split())
            all_words[filename] = words
        return all_words
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            try:
                index = words.index(word.lower())
                result[filename] = index+1
            except ValueError:
                pass

        return result

    # count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.
    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():  # Используем метод items() для прохода по всем парам ключ-значение
            result[filename] = words.count(word.lower())

        return result

# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
