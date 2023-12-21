"""Discriptor"""

class Number_of_house:
    """Number of house discriptor"""

    def __init__(self, min_value: int, max_value: int):
        """Initialization"""
        self.min = min_value
        self.max = max_value

    def __set_name__(self, owner, name):
        """The name setter"""
        self.name = name

    def __get__(self, instance, owner):
        """Getter"""
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError("Not found value!")

    def __set__(self, instance, value):
        """Setter"""
        if isinstance(value, int) and self.min <= value <= self.max:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your value!")


class Street:
    """Street discription"""

    def __init__(self, min_length: int, max_length: int):
        """Initialization"""
        self.min = min_length
        self.max = max_length

    def __set_name__(self, owner, name):
        """The name setter"""
        self.name = name

    def __get__(self, instance, owner):
        """Getter"""
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError("Not found value!")

    def __set__(self, instance, value):
        """Setter"""
        if isinstance(value, int) and self.min <= value <= self.max:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your value!")

class Amount_of_products:
    """Products discription"""

    def __init__(self, min_value: int, max_value: int):
        """Initialization"""
        self.min = min_value
        self.max = max_value

    def __set_name__(self, owner, name):
        """The name setter"""
        self.name = name

    def __get__(self, instance, owner):
        """Getter"""
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError("Not found value!")

    def __set__(self, instance, value):
        """Setter"""
        if isinstance(value, int) and self.min <= value <= self.max:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your value!")

class Magazine:
    number_of_house = Number_of_house(1,1000)
    street = Street(10,30)
    amount_of_products = Amount_of_products(10**2, 10**7)

    def __init__(self, name, number_of_house, street, amount_of_products):
        self.name = name
        self.number_of_house = number_of_house
        self.street = street
        self.amount_of_products = amount_of_products

    def __str__(self):
        return f"Magazine with title {self.name} on street {self.street} house of {self.number_of_house} have products {self.amount_of_products}"

