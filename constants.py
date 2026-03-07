"""Shared game constants (stat types, genders, etc.)."""

from enum import IntEnum


class StatTypes(IntEnum):
    """Stat type identifiers."""

    HP = 1
    MP = 2
    ATK = 3
    DEF = 4
    AGL = 5
    INT = 6
    WLD = 7


class MonsterGenders(IntEnum):
    """Monster gender identifiers."""

    FEMALE = 1
    MALE = 2
