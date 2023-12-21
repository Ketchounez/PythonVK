"""Metaclass """


class CustomMeta(type):
    """Metaclass"""

    def __new__(cls, name: str, bases: tuple, attrs: dict):
        def customs_atr(self, _name, _value):
            self.__dict__["custom_" + _name] = _value

        new_attrs = {}
        for attr, value in attrs.items():
            if not ("__" in attr):
                new_attrs["custom_" + attr] = value
            else:
                new_attrs[attr] = value

        new_attrs["__setattr__"] = customs_atr

        obj = super().__new__(cls, name, bases, new_attrs)

        return obj


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
