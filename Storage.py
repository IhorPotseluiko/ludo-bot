class Storage:
    values = {}

    def get(self, key):
        return self.values.get(key)

    def set(self, key, value):
        self.values[key] = value

    def keys(self):
        return list(self.values.keys())

    def items(self):
        return list(self.values.items())

    def check(self):
        return self.values

class Array:
    _array = []

    def get(self):
        return self._array

    def count(self, x):
        return self._array.count(x)

    def set(self, values):
        return self._array.append(values)

    def clear(self):
        return self._array.clear()