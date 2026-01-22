'''Словари'''
def freddy(say):
    l = {
        "s": 10,
        "d": 20,
        "r": 12,
    }
    return l.values()
try:
    print(freddy("Hello"))
except IndentationError, ImportError, TypeError:
    print("Ошибка напишите другое")

'''
1.  l.keys() - # Получить все ключи - dict_keys(["s", "d", "r"])
2.  l.values() - #Получить все значения - dict_values([10, 20, 12])
3.  l.items() - # Получить пары (ключ-значение) - dict_items([(s", 10), ('d', 20), ('r', 12)])
4.  l.get("c") - # Безопасно получить значение - None (ошибки нет), l.get("c", 0) # 0 мы указали значение по умолчанию
5.  l.update(other_dict) - # Объединить словари - l.update({'c': 7}) = ДОбавляет в словарь все пары ключ-значения из другого словаря
6.  l.clear() - # Очистить словарь - l.clear()
7.  l.pop(key, default) - # Удалить ключ и вернуть значение - l.pop("s", None)
8.  l.popitem() - # Удалить и вернутьт последнюю пару - l.popitem()
9.  l.setdefault(key, default) - # Получить значение или установить по умолчанию - l.setdefault("v", 2)

'''