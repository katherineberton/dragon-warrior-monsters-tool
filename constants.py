from enum import IntEnum

class MonsterClasses(IntEnum):
    SLIME = 1
    DRAGON = 2
    BEAST = 3
    BIRD = 4
    PLANT = 5
    BUG = 6
    DEVIL = 7
    ZOMBIE = 8
    MATERIAL = 9
    BOSS = 10

class StatTypes(IntEnum):
    HP = 1
    MP = 2
    ATK = 3
    DEF = 4
    AGL = 5
    INT = 6
    WLD = 7

class MonsterGenders(IntEnum):
    FEMALE = 1
    MALE = 2