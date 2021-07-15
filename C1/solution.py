import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)


    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            if len(body_whl.split('x')) != 3:
                raise ValueError
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])
        except ValueError:
            self.body_length = 0.
            self.body_width = 0.
            self.body_height = 0.

    def get_body_volume(self):
        volume = self.body_height * self.body_width * self.body_length
        return volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def read(filename):
    with open(filename) as file:
        cars = []
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            # print('Hz - ', row)
            if len(row) == 0:
                break
            if row[0] == 'car' and not row[4] and not row[6]:
                if len(row[1]) != 0 and row[2].isdigit() and check_photo(row[3]) and check_carrying(row[5]):
                    # print(row)
                    cars.append(Car(brand=row[1], passenger_seats_count=row[2], photo_file_name=row[3],
                                    carrying=row[5]))
            if row[0] == 'truck' and not row[2] and not row[6]:
                if len(row[1]) != 0 and check_photo(row[3]) and check_carrying(row[5]) \
                        and (len(row[4].split('x')) == 3) or not len(row[4]):
                    # print(row)
                    cars.append(Truck(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                      body_whl=row[4]))
            if row[0] == 'spec_machine' and not row[2] and not row[4]:
                if len(row[1]) != 0 and check_photo(row[3]) and check_carrying(row[5]) and len(row[6]):
                    # print(row)
                    cars.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                            extra=row[6]))
            else:
                continue
    return cars


def check_carrying(carry):
    try:
        float(carry)
    except (AssertionError, ValueError):
        return
    else:
        return 1


def check_photo(photo):
    if not len(photo):
        return
    ind = os.path.splitext(photo)[-1]
    if ind not in ('.jpg', '.jpeg', '.png', '.gif'):
        return
    return 1


def get_car_list(csv_filename):
    if os.stat(csv_filename).st_size == 0:
        return
    return read(csv_filename)

#
# cars = get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
# for car in cars:
#     print(car)
#