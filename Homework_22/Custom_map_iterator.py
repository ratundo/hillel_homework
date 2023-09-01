"""
custom map (iterator), приймає dict і приймає 2 функції.
   першу фунцію застосовуємо до ключів а другу до значень.
   map(dict, func1, funct2)
  (func1(key), func2(value))

"""


class CustomMap:
    def __init__(self, input_dict, key_func, value_func):
        self.input_dict = input_dict
        self.key_func = key_func
        self.value_func = value_func
        self.keys = list(input_dict.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.input_dict[key]
            transformed_key = self.key_func(key)
            transformed_value = self.value_func(value)
            self.index += 1
            return transformed_key, transformed_value
        else:
            raise StopIteration()

