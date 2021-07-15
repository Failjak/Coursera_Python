import tempfile
import os.path
import uuid


class File:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w+'):
                pass

    def __iter__(self):
        with open(self.filename, 'r') as _file:
            lines = _file.readlines()
        return iter(lines)

    def __next__(self):
        return next(self)

    def __add__(self, other):
        new_filename = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        new_file = type(self)(new_filename)
        new_file.write(self.read() + other.read())
        return new_file

    def read(self):
        with open(self.filename, 'r') as _file:
            return _file.read()

    def write(self, line):
        with open(self.filename, 'w') as _file:
            _file.write(line)

    def __str__(self):
        return self.filename


# file1 = File('test_for_week4.txt')
# file2 = File('test_for_week4_2.txt')
# file = file1 + file2
# print(file.read())

# path_to_file = 'some_file'
# print(os.path.exists(path_to_file))
# file_obj = File(path_to_file)
# print(os.path.exists(path_to_file))
#
# print(ascii(file_obj.read()))
# file_obj.write('some text')
# print(file_obj.read())
#
# file_obj.write('other text')
# print(file_obj.read())
#
# file_obj_1 = File(path_to_file + '_1')
# file_obj_2 = File(path_to_file + '_2')
# file_obj_1.write('line 1\n')
# file_obj_2.write('line 2\n')
# new_file_obj = file_obj_1 + file_obj_2
# print(isinstance(new_file_obj, File))
# print(new_file_obj)
# for line in new_file_obj:
#     print(ascii(line))

