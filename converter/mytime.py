import re

class MyTime:
    def __init__(self, hours=0, minutes=0, reprStr=''):  # Конструктор
        self.hours = 0
        self.minutes = 0
        if reprStr == '':
            self.__set_fields(hours, minutes)
        elif re.match('\d{1,2}:\d{1,2}', reprStr):
            parts = reprStr.split(':')
            self.__set_fields(hours=parts[0], minutes=parts[1])

    def __set_fields(self, hours=0, minutes=0):
        self.hours = int(hours) + int(minutes) // 60
        self.minutes = int(minutes) % 60

    def setTimeFromMinutes(self, minutes):
        self.hours = int(minutes) // 60
        self.minutes = minutes - self.hours * 60

    def toMinutes(self):
        return self.hours * 60 + self.minutes

    def __add__(self, other):
        rezult = MyTime()
        rezult.setTimeFromMinutes(self.toMinutes() + other.toMinutes())
        return rezult

    def __repr__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'
