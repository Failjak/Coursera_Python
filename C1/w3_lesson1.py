class Counter:
    def __init__(self, original_list=None):
        self.countainer = original_list or {}

    def __getitem__(self, key):
        # поведение класса при обращении к индексу
        try:
            print(self.countainer[key])
        except KeyError:
            print('KeyNotFound')

    def __setitem__(self, key, value):
        # поведение при присваивании по индексу или ключу
        self.countainer[key] = value

    def __str__(self):
        return self.countainer.__str__()


probe = Counter({'1': 'Nekt', 2: 'im so sorry'})

probe[1] = 'hi'
print(probe)
