import random


class Field:  # создание класаа
    def __init__(self, size, ships):  # конструктор класса
        self.size = size
        self.ships_alive = ships
        self.grid = []  # атрибуты
        for i in range(size):  # цикл где i бегает по size
            self.grid.append(
                [None] * size)  # создает список списков состоящих из none([[none, none, none...], [none, ...], ...]))

    def display(self, show_ships=True):  # метод который выводит корабли на экран
        letters = 'ABCDEFGHIJ'  # строка состоящая из букв
        space = '    '  # отступ для расстояния между буквами
        for letter in letters:  # цикл где letter(1буква )бегает по letters
            space += letter + ' '  # пробел после каждой буквы
        print(space)  # вывод расстояния между буквами
        for i, row in enumerate(self.grid):  # цикл где i - index(цифра) и row - строка ноликов и квадратиков
            display_row = ""  # пробел
            for cell in row:  # цикл где cell - ячейка бегает по row
                if cell is None or (
                        cell is not None and not show_ships):  # проверка на то, что ячейка пустая или(ячейка не пустая и не занята кораблем)
                    display_row += "O "  # в случае проверки добавляем 0
                else:
                    display_row += "■ "  # если проверка не выполнена добавляем ■
            if i + 1 != 10:  # проверка на цифру если нету 10 цифр то добавляем 1 цифру с пробелом
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)  # иначе без пробела


class BattleshipGame:  # создание второго класса
    def __init__(self):  # конструктор класса
        self.size = 10
        self.ships = 15  # атрибуты

        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)  # это тоже атрибуты

    def place_ships_randomly(self, field, num_ships):  # метод который расставляет корабли случайно
        for _ in range(num_ships):  # цикл где перебираем все корабли
            placed = False  # расстановка не расстановленна
            while not placed:  # цикл пока не расставлены корабли
                coords = (
                random.randint(0, self.size - 1), random.randint(0, self.size - 1))  # выбор случайных координат
                if self.is_valid_ship_placement(field,
                                                coords):  # проверка можем ли мы поставить корабль на случайные координаты
                    field.grid[coords[0]][coords[1]] = "S"  # ставим корабль на эти координаты
                    placed = True  # расстановка тру

    def is_valid_ship_placement(self, field, coords,
                                ship_length=1, ):  # метод для проверки возможности поставить корабль
        x, y = coords  # атрибут

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def player_turn(self, x, y):  # метод хода игрока

        x = "ABCDEFGHIJ".index(x)  # вычисление кооринат по x(буквы)
        y -= 1  # цифры

        if self.computer_field.grid[y][x] == "S":  # проверка если в этой клетке у компьютера есть корабль
            print("Вы попали!") # мы попали
            self.computer_field.grid[y][x] = "X" # заменяем корабль на крестик в этих координатах
            self.computer_field.ships_alive -= 1 # вычитаем 1 живой корабль у компбютера
            return True # возвращяем тру
        else: # иначе
            print("Промах!") # промах
            return False # возвращяем фолс

    def computer_turn(self): # метод хода компьютера
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1) # выбираем рандомные корды для выстрела(хода)
        if self.player_field.grid[y][x] == "S": # проверка на наличие корабля в клетке
            print("Компьютер попал!") # компьютер попал
            self.player_field.grid[y][x] = "X" # заменяем корабль на крестик в случае попадания
            self.player_field.ships_alive -= 1 # вычитаем 1 живой корабль у игрока
        else: # иначе
            print("Компьютер промахнулся!") # промах

    def play(self): # метод начала игры
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships) # случайная расстановка(комп) передаем поле компа и кол-во кораблей
        self.computer_field.display(show_ships=True) # отоброжаем поле

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships) # случайная расстановка игрока передаем поле и вол-во кораблей
        self.player_field.display(show_ships=True) # отоброжаем поле игрока

        while True: # бесконечный цикл
            x, y = input('Введите координату x:'), int(input('Введите координату y: ')) # игрок вводит координаты для выстрела
            self.player_turn(x, y) # делаем ход
            if self.computer_field.ships_alive == 0: # проверяем кол-во живых кораблей компа
                print("Вы победили! Все корабли компьютера потоплены")
                break # выход из цикла
            self.computer_turn() # ход компьютера
            if self.player_field.ships_alive == 0: # проверка на кол-во живых кораблей игрока
                print("Вы проиграли! Все ваши корабли потоплены")
                break # выход из цикла


game = BattleshipGame() # создаем обьект класса
game.play() # запускаем игру
