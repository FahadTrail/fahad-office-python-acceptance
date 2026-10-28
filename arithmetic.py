"""Synthetic arithmetic helpers used only for an isolated acceptance drill."""


def add(left, right):
    return left + right


def clamp(value, lower, upper):
    """Clamp *value* to be within the inclusive range [lower, upper].

    Raises:
        ValueError: If *lower* is greater than *upper*.
    """
    if lower > upper:
        raise ValueError("lower bound must not be greater than upper bound")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
