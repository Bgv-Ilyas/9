#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    def add_flight(destinations):
        destination = input("Введите пункт назначения: ")
        flight_number = input("Введите номер рейса: ")
        plane_type = input("Введите тип самолета: ")

        flight_info = {
            'название пункта назначения': destination,
            'номер рейса': flight_number,
            'тип самолета': plane_type
        }

        destinations.append(flight_info)
        destinations.sort(key=lambda x: x['номер рейса'])
        print("Информация о рейсе добавлена.")

    def display_flights_by_destination(destinations):
        search_destination = input("Введите пункт назначения для поиска: ")
        matching_flights = [
            (flight['номер рейса'], flight['тип самолета'])
            for flight in destinations
            if flight['название пункта назначения'] == search_destination
        ]

        if matching_flights:
            print(f"Рейсы в пункт назначения '{search_destination}':")
            for flight_number, plane_type in matching_flights:
                print(f"Номер рейса: {flight_number}, Тип самолета: {plane_type}")
        else:
            print(f"Рейсов в пункт назначения '{search_destination}' не найдено.")

    # Пример использования
    destinations_list = []
    while True:
        print("\n1. Добавить рейс")
        print("2. Вывести рейсы по пункту назначения")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            add_flight(destinations_list)
        elif choice == '2':
            display_flights_by_destination(destinations_list)
        elif choice == '3':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
