class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range (1, new_floor):
            if new_floor < self.number_of_floors:
                print(i)
            else:
                print('Such floor does not exist')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Name: {self.name}, number of floors: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))