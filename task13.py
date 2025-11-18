class Product:
    def __init__(self, name: str, price: float, quantity: int = 1) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (
            f"{self.name} - {self.price:.2f}₽ "
            f"(кол-во: {self.quantity}, итого: {self.get_total_price():.2f}₽)"
        )

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Cart:
    def __init__(self) -> None:
        self._items: list[Product] = []

    def add_product(self, product: Product) -> None:
        for item in self._items:
            if item.name == product.name:
                item.quantity += product.quantity
                return

        self._items.append(product)

    def remove_product(self, product_name: str) -> bool:
        for i, item in enumerate(self._items):
            if item.name == product_name:
                self._items.pop(i)
                return True
        return False

    def get_total_price(self) -> float:
        return sum(product.get_total_price() for product in self._items)

    def get_item_count(self) -> int:
        return sum(product.quantity for product in self._items)

    def clear(self) -> None:
        self._items.clear()

    def get_products(self) -> list[Product]:
        return self._items.copy()

    def __str__(self) -> str:
        if not self._items:
            return "Корзина пуста"

        items_str = "\n".join(f"  {i + 1}. {product}" for i, product in enumerate(self._items))
        return (
            f"Содержимое корзины:\n{items_str}\n"
            f"Всего товаров: {self.get_item_count()} шт.\n"
            f"Сумма заказа: {self.get_total_price():.2f}₽"
        )


if __name__ == "__main__":
    print("\n1. Создание товаров:")
    apple = Product("Яблоко", 50.0, 5)
    banana = Product("Банан", 35.0, 3)
    orange = Product("Апельсин", 60.0, 2)

    print(f"> {apple}")
    print(f"> {banana}")
    print(f"> {orange}")

    print("\n2. Создание корзины и добавление товаров:")
    cart = Cart()
    print(f"Начальное состояние: {cart}")

    print("\nДобавляем товары в корзину")
    cart.add_product(apple)
    cart.add_product(banana)
    cart.add_product(orange)
    print(cart)

    print("\n3. Добавление еще одного товара (Яблоко):")
    extra_apple = Product("Яблоко", 50.0, 2)
    print(f"Добавляем: {extra_apple}")
    cart.add_product(extra_apple)
    print(cart)

    print("\n4. Удаление товара из корзины:")
    removed = cart.remove_product("Банан")
    print(f"Товар 'Банан' удален: {removed}")
    print(cart)

    print("\n5. Попытка удаления несуществующего товара:")
    removed = cart.remove_product("Груша")
    print(f"Товар 'Груша' удален: {removed}")
    print(cart)

    print("\n6. Очистка корзины:")
    cart.clear()
    print(cart)
