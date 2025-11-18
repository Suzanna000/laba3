import os
from pathlib import Path


class FileManager:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.filepath = Path(filename)

    def create(self, content: str = "") -> bool:
        if self.filepath.exists():
            print(f"Файл '{self.filename}' уже существует.")
            return False

        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Файл '{self.filename}' успешно создан.")
            return True
        except IOError as e:
            print(f"Ошибка при создании файла: {e}")
            return False

    def read(self) -> str | None:
        if not self.filepath.exists():
            print(f"Файл '{self.filename}' не существует.")
            return None

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        except IOError as e:
            print(f"Ошибка при чтении файла: {e}")
            return None

    def write(self, content: str, append: bool = False) -> bool:
        mode = "a" if append else "w"
        action = "добавлено" if append else "записано"

        try:
            with open(self.filepath, mode, encoding="utf-8") as file:
                file.write(content)
            print(f"Содержимое успешно {action} в '{self.filename}'.")
            return True
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")
            return False

    def delete(self) -> bool:
        if not self.filepath.exists():
            print(f"Файл '{self.filename}' не существует.")
            return False

        try:
            self.filepath.unlink()
            print(f"Файл '{self.filename}' успешно удален.")
            return True
        except OSError as e:
            print(f"Ошибка при удалении файла: {e}")
            return False

    def exists(self) -> bool:
        return self.filepath.exists()

    def get_size(self) -> int | None:
        if not self.filepath.exists():
            print(f"Файл '{self.filename}' не существует.")
            return None

        return self.filepath.stat().st_size

    def get_info(self) -> dict | None:
        if not self.filepath.exists():
            print(f"Файл '{self.filename}' не существует.")
            return None

        try:
            stat_info = self.filepath.stat()
            return {
                "имя": self.filename,
                "размер_байт": stat_info.st_size,
                "существует": True,
                "абсолютный_путь": str(self.filepath.absolute()),
            }
        except OSError as e:
            print(f"Ошибка при получении информации: {e}")
            return None


if __name__ == "__main__":
    print("1. Создание файла:")
    fm = FileManager("demo.txt")
    fm.create("Привет, мир!\n")

    print("\n2. Проверка существования файла:")
    print(f"Файл существует: {fm.exists()}")

    print("\n3. Чтение содержимого файла:")
    content = fm.read()
    print(f"Содержимое: {content}")

    print("\n4. Перезапись содержимого файла:")
    fm.write("Новое содержимое!\n")
    print(f"Новое содержимое: {fm.read()}")

    print("\n5. Добавление содержимого в файл:")
    fm.write("Добавленная строка.\n", append=True)
    print(f"После добавления:\n{fm.read()}")

    print("\n6. Информация о файле:")
    info = fm.get_info()
    if info:
        for key, value in info.items():
            print(f"> {key}: {value}")

    print("\n7. Размер файла:")
    size = fm.get_size()
    print(f"Размер: {size} байт")

    print("\n8. Удаление файла:")
    fm.delete()
    print(f"Файл существует: {fm.exists()}")