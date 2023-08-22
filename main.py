from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value


class Name:
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.__value = None
        self.value = phone

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        if self.is_validate_phone(phone) == False:
            raise AttributeError("Number is not Valid!")

    def is_validate_phone(self, phone_for_validation):
        new_phone = (
                    phone_for_validation.strip()
                    .replace("+", "")
                    .replace("(", "")
                    .replace(")", "")
                    .replace("-", "")
                    .replace(" ", "")
                )
        if new_phone.isdigit():
            self.__value = new_phone
            return True
        return False

class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except ValueError:
            raise 'Invalid date! Date format should be: dd.mm.YYYY'



class Record:
    def __init__(self, name, phones, birthday=None):
        self.name = name
        self.phones = [phones]
        self.birthday = birthday

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def days_to_birthday(self):
        print(self, self.birthday)
        if self.birthday == None:
            return "Дата рождения не задана"

        b_now = datetime.now()
        a = self.birthday.birthday

        print(self.birthday)
        b_d = datetime(b_now.year, self.birthday.birthday.month, self.birthday.birthday.day + 1)

        diff = b_d - b_now

        if diff.days < 0:
            bd_new = datetime(b_now.year + 1, self.birthday.birthday.month, self.birthday.birthday.day)
            difference = bd_new - b_now
            return difference.days
        return


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get[value]

    def iterator(self, count_data):
        my_IterAddressBook_list = IterAddressBook(count_data)
        for ran in my_IterAddressBook_list:
            print(ran, end=' ')


class IterAddressBook:
    def __init__(self, count_data):
        self.iter = -1
        self.count_data = count_data

    def __iter__(self):
        return self
    def __next__(self):
        self.iter += 1
        if self.iter < self.count_data:
            return ab.data[list(ab.data.keys())[self.iter]]
        else:
            raise StopIteration


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('+   (   ) 1234567890')
    bd = Birthday('01.01.1999')
    rec = Record(name, phone, bd)
    ab = AddressBook()
    ab.add_record(rec)

    name = Name('Mary')
    phone = Phone('+   (   ) 453534534534')
    bd = Birthday('01.01.1970')
    rec = Record(name, phone, bd)
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].birthday, Birthday)
    # print(rec.days_to_birthday())
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print(ab.data)
    print(ab.iterator(1))
    print(ab.iterator(2))

    print('All Ok)')
