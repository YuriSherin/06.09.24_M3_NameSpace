# Задача "Счётчик вызовов"

def count_calls():
    """Функция подсчитывает количество вызовов остальных функций, изменяя значение глобальной переменной calls"""
    global calls    # Объявление, что функция работает с глобальной переменной
    calls += 1      # Увеличиваем счетчик вызовов на 1

def string_info(str_):
    """Функция принимает строку и возвращает кортеж с указанием длины строки, строку в верхнем и нижнем регистре"""
    count_calls()                                   # Увеличиваем счетчик вызовов
    return len(str_), str_.upper(), str_.lower()    # Возвращаем кортеж

def is_contains(str_, list_):
    """Функция принимает строку и список и возвращает True, если такая строка есть в списке или False,
    если строка в списке отсутствует. Регистром строки можно пренебречь"""
    count_calls()                                   # Увеличиваем счетчик вызовов
    result = False                                  # Результат выполнения функции
    list_lower = [s.lower() for s in list_]         # Переводим все строки списка в нижний регистр
    if str_.lower() in list_lower:                  # Если строка найдена в списке
        result = True                               # Изменим результат выполнения функции
    return result                                   # Возвращаем результат

calls = 0   # Глобальная переменная

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
