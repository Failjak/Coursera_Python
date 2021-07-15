import argparse
import json
import os
import tempfile

#
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    storage_data = dict()

    if os.path.isfile(storage_path):  # существует ли файл по этому пути
        if namespace.val:
            """
            Здесь же реализовать ввод в файл
            """
            if os.path.getsize(storage_path) != 0:  # если НЕпустой файл

                with open(storage_path, 'r') as f:  # считываем сожержимое текстовика
                    storage_data = json.load(f)

                with open(storage_path, 'w') as f:  # здесь будем редачить и записывать в текстовик снова
                    if namespace.key in storage_data:  # если такой ключ уже есть
                        val = storage_data[namespace.key]
                        storage_data.update({namespace.key: '{}, {}'.format(val, namespace.val)})
                    else:  # если ключа не было
                        storage_data[namespace.key] = namespace.val
                    json.dump(storage_data, f)
            else:  # если же файл пустой
                with open(storage_path, 'w') as f:
                    storage_data[namespace.key] = namespace.val
                    json.dump(storage_data, f)
        else:
            """
            Здесь реализовать вывод на экран для ключа
            """
            with open(storage_path, 'r') as f:
                storage_data = json.load(f)
                print(storage_data.get(namespace.key, None))
    else:
        with open(storage_path, 'w') as f:
            if namespace.val:
                storage_data[namespace.key] = namespace.val
                json.dump(storage_data, f)
            else:
                print(None)









