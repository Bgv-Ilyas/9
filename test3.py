#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    # Создаем словарь, где ключами являются числа, а значениями - строки
    original_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

    # Используем метод items() для получения объекта dict_items
    dict_items_object = original_dict.items()

    # Создаем новый словарь, "обратный" исходному
    reversed_dict = {value: key for key, value in dict_items_object}

    # Выводим исходный и новый словари
    print("Исходный словарь:", original_dict)
    print("Новый словарь (обратный исходному):", reversed_dict)

