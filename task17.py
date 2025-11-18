from typing import List, Dict, Any, Optional, Callable


class Table:
    def __init__(self, name: str, columns: List[str]) -> None:
        self.name = name
        self.columns = columns
        self.rows: List[Dict[str, Any]] = []
        self._id_counter = 1

    def insert(self, **kwargs) -> int:
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f"Неизвестная колонка: {key}")

        row = {'id': self._id_counter}
        for column in self.columns:
            row[column] = kwargs.get(column, None)

        self.rows.append(row)
        self._id_counter += 1

        return row['id']

    def select(
        self,
        where: Optional[Callable[[Dict[str, Any]], bool]] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        result = self.rows
        if where is not None:
            result = [row for row in result if where(row)]

        if order_by is not None:
            if order_by not in self.columns and order_by != 'id':
                raise ValueError(f"Неизвестная колонка для сортировки: {order_by}")
            result = sorted(result, key=lambda row: row.get(order_by, 0))

        if limit is not None:
            result = result[:limit]

        return result

    def update(
        self,
        where: Callable[[Dict[str, Any]], bool],
        **kwargs
    ) -> int:
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f"Неизвестная колонка: {key}")

        updated_count = 0
        for row in self.rows:
            if where(row):
                row.update(kwargs)
                updated_count += 1

        return updated_count

    def delete(self, where: Callable[[Dict[str, Any]], bool]) -> int:
        initial_count = len(self.rows)
        self.rows = [row for row in self.rows if not where(row)]
        return initial_count - len(self.rows)

    def count(self) -> int:
        return len(self.rows)

    def __repr__(self) -> str:
        return f"Table(name='{self.name}', rows={len(self.rows)})"


def print_table(table: Table, title: str = "") -> None:
    if title:
        print(f"{title:^60}")

    if not table.rows:
        print("Таблица пуста!")
        return

    headers = ['id'] + table.columns
    print(" | ".join(f"{h:^10}" for h in headers))
    print("-" * (13 * len(headers)))

    for row in table.rows:
        values = [str(row[h]) for h in headers]
        print(" | ".join(f"{v:^10}" for v in values))


if __name__ == "__main__":
    users = Table("users", ["name", "email", "age", "city"])
    print(f"Создана таблица: {users}")

    print("\nINSERT - добавление записей:")
    user_id_1 = users.insert(name="Алиса", email="alice@example.com", age=25, city="Москва")
    user_id_2 = users.insert(name="Боб", email="bob@example.com", age=30, city="СПб")
    user_id_3 = users.insert(name="Виктор", email="victor@example.com", age=22, city="Москва")
    print(f"Добавлено 3 пользователя (ID: {user_id_1}, {user_id_2}, {user_id_3})")

    print_table(users, "Исходные данные")

    print("\nSELECT - выбор всех записей:")
    all_users = users.select()
    print(f"Всего записей: {len(all_users)}")

    print("\nSELECT WHERE - фильтрация по условию:")
    moscow_users = users.select(where=lambda u: u['city'] == 'Москва')
    print(f"Пользователи из Москвы: {len(moscow_users)}")
    print_table(Table("moscow", ["name", "email", "age", "city"]), "Москва")
    for row in moscow_users:
        print(f"> {row['name']}: {row['age']} лет, {row['email']}")

    print("\nSELECT ORDER BY LIMIT - сортировка и ограничение:")
    top_users = users.select(order_by='age', limit=2)
    print(f"2 самых молодых пользователя:")
    for row in top_users:
        print(f"> {row['name']}: {row['age']} лет")

    print("\nUPDATE - обновление данных:")
    updated = users.update(
        where=lambda u: u['name'] == 'Боб',
        age=31,
        city='Казань'
    )
    print(f"Обновлено записей: {updated}")
    print_table(users, "После UPDATE")

    print("\nDELETE - удаление записей:")
    deleted = users.delete(where=lambda u: u['age'] < 23)
    print(f"Удалено записей: {deleted}")
    print_table(users, "После DELETE")

    print("\nИТОГИ:")
    print(f"Осталось записей: {users.count()}")
    print(f"Средний возраст: {sum(u['age'] for u in users.rows) / users.count():.1f}")

    print("\nОБРАБОТКА ОШИБОК:")
    try:
        users.insert(name="Тест", unknown_column="значение")
    except ValueError as e:
        print(f"Поймана ошибка: {e}")
