calls = 0
def count_calls(): #Подсчитываем вызов остальных функций
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()#Принимает строку и возвращает кортеж
    tuple_length = len(string)
    tuple_up = string.upper()
    tuple_down = string.lower()
    return (tuple_length, tuple_up, tuple_down)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower() in [x.lower() for x in list_to_search]
    return string

print(string_info('Я рЕзуЛьтаТ програММы'))
print(is_contains('iii', ['fff', 'iii']))
print(string_info('MeoW'))
print(is_contains('Urban', ['urBAN', 'Not urban']))
print(calls)
