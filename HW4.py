class Date:
    def __init__(self, day: int, month: int, year: int):
        if not 32 > day > 0:
            raise TypeError("DAY ERROR")
        if not 13 > month > 0:
            raise TypeError("MONTH ERROR")
        if not 10000 > year > 999:
            raise TypeError("YEAR ERROR")

        self._day = day
        self._month = month
        self._year = year

    def __str__(self):  # toString
        return f"{self._day}/{self._month}/{self._year}"

    def __sub__(self, other):
        number_of_days = 0
        if isinstance(other, Date):
            flag = True
            d = self
            if self > other:
                d = other
                other = self
            while flag:
                d = d.getNextDay()
                number_of_days += 1
                if d == other:
                    flag = False
        return number_of_days

    def isValid(self):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            day_count_for_month[2] = 29
        return 1 <= self._month <= 12 and 1 <= self._day <= day_count_for_month[self._month]

    def getNextDay(self):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            day_count_for_month[2] = 29
        if day_count_for_month[self._month] > self._day:
            return Date(self._day + 1, self._month, self._year)
        if day_count_for_month[self._month] < self._day + 1 and self._month < 12:
            return Date(1, self._month + 1, self._year)
        else:
            return Date(1, 1, self._year + 1)

    def getNextDays(self, day_to_add):
        d = self
        for x in range(day_to_add):
            d = d.getNextDay()
        return d

    def __eq__(self, other) -> bool:
        if isinstance(other, Date):
            return self._day == other._day and self._month == other._month and self._year == other._year

    def __ne__(self, other) -> bool:
        if isinstance(other, Date):
            return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, Date):
            return self._year > other._year or (self._year == other._year and self._month > other._month) or \
                   (self._year == other._year and self._month == other._month and self._day > other._day)

    def __lt__(self, other) -> bool:
        if isinstance(other, Date):
            return self._year < other._year or (self._year == other._year and self._month < other._month) or \
                   (self._year == other._year and self._month == other._month and self._day < other._day)

    def __ge__(self, other) -> bool:
        if isinstance(other, Date):
            return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other) -> bool:
        if isinstance(other, Date):
            return self.__lt__(other) or self.__eq__(other)


d1 = Date(7, 12, 2000)
d2 = Date(17, 12, 2000)
print(d1 < d2)
print(d1)
print(d2)
print(d1.isValid())
print(d2.isValid())
print(d1.getNextDay())
print(d2.getNextDay())
print(d1.getNextDays(23))
print(d2.getNextDays(23))
print(d2 > d1)
print(d2 < d1)
print(d2 == d1)
print(d2 != d1)
print(d2 <= d1)
print(d2 >= d1)
