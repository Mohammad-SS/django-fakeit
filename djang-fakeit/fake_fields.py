import datetime
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import calendar
from . import helpers


class SimpleFakeField:
    repeating = True

    def __init__(self, repeating: bool = True):
        self.repeating = repeating


class FakeStringField(SimpleFakeField):
    length = 5
    allowed_chars = ["upper", "lower", "special", "numbers"]

    def __init__(self, length: int = 5, repeating: bool = True, allowed_chars: str | list = "__all__"):
        super(FakeStringField, self).__init__(repeating=repeating)
        self.length = length
        if type(allowed_chars) == list:
            for allowed_char in allowed_chars:
                if allowed_char in self.allowed_chars:
                    self.allowed_chars.remove(allowed_char)

    def generate(self):
        choices = self.get_choices()
        if self.repeating:
            return "".join(random.choice(choices) for i in range(self.length))
        else:
            return "".join(random.sample(choices, self.length))

    def get_choices(self):
        choices = ""
        if "lower" in self.allowed_chars:
            choices += ascii_lowercase
        if "upper" in self.allowed_chars:
            choices += ascii_uppercase
        if "special" in self.allowed_chars:
            choices += punctuation
        if "digits" in self.allowed_chars:
            choices += digits

        return choices


class FakeIntegerField(SimpleFakeField):

    def __init__(self, minimum: int = 0, maximum: int = 99):
        super(FakeIntegerField, self).__init__(repeating=True)
        self.minimum = minimum
        self.maximum = maximum

    def generate(self):
        return random.randint(self.minimum, self.maximum)


class FakeFloatField(SimpleFakeField):

    def __init__(self, minimum: float = 0.0, maximum: float = 99.99, depth: int = 2):
        super(FakeFloatField, self).__init__(repeating=True)
        self.depth = depth
        self.minimum = minimum
        self.maximum = maximum

    def generate(self):
        return round(random.uniform(self.minimum, self.maximum), self.depth)


class FakeDateTimeField(SimpleFakeField):

    def __init__(self, year: int | range, month: int | range, day: int | range, hour: int | range, minute: int | range,
                 second: int | range):
        super().__init__(repeating=True)
        self.year = self.set_year(year)
        self.month = self.set_month(month)
        self.day = self.set_day(day)
        self.hour = self.set_hour(hour)
        self.minute = self.set_minute(minute)
        self.second = self.set_second(second)

    def set_year(self, year: int | range | None):
        return helpers.rand_int_factory(value=year, max=3000, min=1800, name="year")

    def set_month(self, month: int | range | None):
        return helpers.rand_int_factory(value=month, max=12, min=0, name="month")

    def set_day(self, day: int | range | None):
        return helpers.rand_int_factory(value=day, max=calendar.monthrange(self.year, self.month)[1],
                                        min=calendar.monthrange(self.year, self.month)[0], name="day")

    def set_hour(self, hour: int | range | None):
        return helpers.rand_int_factory(value=hour, max=23, min=0, name="hour")

    def set_minute(self, minute: int | range | None):
        return helpers.rand_int_factory(value=minute, max=59, min=0, name="minute")

    def set_second(self, second):
        return helpers.rand_int_factory(value=second, max=59, min=0, name="second")

    def generate(self):
        return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute,
                                 second=self.second)


class FakeDateField(SimpleFakeField):

    def __init__(self, year: int | range, month: int | range, day: int | range):
        super().__init__(repeating=True)
        self.year = self.set_year(year)
        self.month = self.set_month(month)
        self.day = self.set_day(day)

    def set_year(self, year: int | range | None):
        return helpers.rand_int_factory(value=year, max=3000, min=1800, name="year")

    def set_month(self, month: int | range | None):
        return helpers.rand_int_factory(value=month, max=12, min=0, name="month")

    def set_day(self, day: int | range | None):
        return helpers.rand_int_factory(value=day, max=calendar.monthrange(self.year, self.month)[1],
                                        min=calendar.monthrange(self.year, self.month)[0], name="day")

    def generate(self):
        return datetime.date(year=self.year, month=self.month, day=self.day)


class FakeBooleanField(SimpleFakeField):

    def __init__(self):
        super().__init__(repeating=True)
        self.base_number = random.randint(0, 1)

    def generate(self):
        return bool(self.base_number)

