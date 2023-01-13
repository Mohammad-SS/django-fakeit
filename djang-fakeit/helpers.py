import random


def rand_int_factory(cls, value: int | range | None, max: int, min: int, name="Value"):
    if type(value) == int:
        min_value = value
        max_value = value
    elif type(value) == range:
        min_value = value[0]
        max_value = value[-1]
    else:
        min_value = min
        max_value = max

    assert max_value > min_value, f"Max {name} cant be higher than min {name}"
    assert min_value >= min, f"{name} can't be lower than {min}"
    assert max_value <= max, f"{name} can't be higher than {max}"

    return random.randint(min_value, max_value)