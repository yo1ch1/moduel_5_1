class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        for floor_number in range(1, new_floor+1):
            if new_floor < self.numbers_of_floors or new_floor < 1:
                print(floor_number)
            else:
                print('"Такого этажа не существует"')
                break



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


