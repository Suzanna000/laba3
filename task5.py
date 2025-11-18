class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def make_sound(self) -> None:
        print(f"{self.name} издает звук")

    def get_info(self) -> str:
        return f"{self.name}, возраст: {self.age} лет"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> None:
        print(f"{self.name} лает: Гав-гав!")

    def fetch(self) -> None:
        print(f"{self.name} принес мяч")

    def get_info(self) -> str:
        return f"{self.name} ({self.breed}), возраст: {self.age} лет"



if __name__ == "__main__":
    print("1. Создаем общее животное:")
    animal = Animal("Зверь", 5)
    print(f"Информация: {animal.get_info()}")
    animal.make_sound()

    print("\n2. Создаем собаку:")
    dog = Dog("Шарик", 3, "Лабрадор")
    print(f"Информация: {dog.get_info()}")
    dog.make_sound()
    dog.fetch()

    print("\n3. Проверка наследования:")
    print(f"Собака является Животным? {isinstance(dog, Animal)}")
    print(f"Собака является Собакой? {isinstance(dog, Dog)}")

    print("\n4. Полиморфизм:")
    animals: list = [animal, dog]
    for pet in animals:
        pet.make_sound()
