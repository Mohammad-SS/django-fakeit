import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


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

