# I. Напишите класс PublicTransport
# Экземпляр класса создается из следующих атрибутов:
#   1. brand - Марка транспорта
#   2. ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя
#   3. year - Год выпуска
#   4. color - Цвет
#   5. max_speed - Максимальная скорость
# У класса должно быть СВОЙСТВО info, которое выводит на печать информацию о:
# марке, цвете, годе выпуска и мощности двигателя
#
# II. Напишите класс Bus унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. passengers - кол-во пассажиров
#   2. ПРИВАТНЫЙ (private) атрибут park - Парк приписки автобуса
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# Добавить свойство park, которое будет возвращать значение park
# а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999
#
# III. Напишите класс Tram унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. ПРИВАТНЫЙ (private) атрибут route - маршрут трамвая
#   2. path - длина маршрута
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# У класса должно быть СВОЙСТВО how_long, которое вычисляет время прохождения маршрута по формуле max_speed/(4*path)

class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        return f'{self.brand}, {self.color}, {self.year} года выпуска, мощность двигателя {self._engine_power} л.с.'


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        return self.__park

    @park.setter
    def park(self, value):
        assert 1000 <= value <= 9999, 'Номер парка должен быть от 1000 до 9999'
        self.__park = value


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.path = path
        self._fare = fare
        self.__route = route

    @property
    def how_long(self):
        return self.max_speed / (4 * self.path)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
transport = PublicTransport('Автомобиль', 500, 2040, 'Фиолетовый', 300)
first_bus = Bus('ЛиАЗ', 210, 2015, 'Зеленый', 100, 70, 1232, 32)
second_bus = Bus('VOLGABUS', 320, 2019, 'Желтый', 110, 39, 1111, 32)
first_tram = Tram('71-931M', 125, 2010, 'Красный', 75, 5, 15, 32)
second_tram = Tram('71-409-1', 240, 2018, 'Белый', 85, 7, 17, 32)

assert isinstance(type(transport).info, property), 'В классе PublicTransport, info - не свойство класса'
assert transport._engine_power, 'В классе PublicTransport, engine_power не защищенный атрибут'
assert first_bus._Bus__park, 'В классе Bus, park не приватный атрибут'
assert second_bus._fare, 'В классе Bus, fare не защищенный атрибут'
assert first_tram._fare, 'В классе Tram, fare не защищенный атрибут'
assert second_tram._Tram__route, 'В классе Tram, route не приватный атрибут'
assert isinstance(type(first_tram).how_long, property), 'В классе Tram, how_long - не свойство класса'
assert first_tram.how_long == 1.25, 'В классе Tram, how_long неверно вычисляется'
assert isinstance(type(second_bus).park, property), 'В классе Bus, park - не свойство класса'
try:
    second_bus.park = 999
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
try:
    second_bus.park = 1234
    print('Проверка на правильность диапазона пройдена')
except AssertionError:
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
try:
    second_bus.park = 10000
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
print('Всё ок')
