from __future__ import annotations
import enum
from tortoise import fields

import base_models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from base_models import User
    from breeding.models import BreedingPlan
    from gates.models import Gate

class MonsterGenders(enum.IntEnum):
    FEMALE = 1
    MALE = 2

class MonsterClasses(enum.IntEnum):
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

class Monster(base_models.BaseModel):
    """Real monsters in the game. Monsters become "real" if a user catches them or if they are the catchable boss of a travelers gate."""
    category: MonsterSpecies = fields.ForeignKeyField('monsters.MonsterSpecies', related_name="monsters")
    user: User | None = fields.ForeignKeyField('models.User', related_name="monsters", null=True)
    name: str | None = fields.CharField(max_length=255, null=True)
    gender: MonsterGenders = fields.SmallIntEnumField(MonsterGenders, default=MonsterGenders.FEMALE)
    level: int | None = fields.IntField(null=True)
    bred: bool = fields.BooleanField(default=False)
    breeding_level: int | None = fields.IntField(null=True)
    breeding_plan: BreedingPlan | None = fields.ForeignKeyField('breeding.BreedingPlan', related_name="monsters", null=True)
    stats: MonsterStat = fields.OneToOneField('monsters.MonsterStat', related_name="monster", null=True)
    boss_of: Gate | None = fields.ForeignKeyField('gates.Gate', related_name="boss")


class MonsterSpecies(base_models.BaseModel):
    """Monster species."""
    name: str = fields.CharField(max_length=255)
    slug: str = fields.CharField(max_length=255)
    monster_class: MonsterClasses = fields.SmallIntEnumField(MonsterClasses, default=MonsterClasses.SLIME)


class MonsterStat(base_models.BaseModel):
    health_points: int = fields.IntField(default=0)
    mana_points: int = fields.IntField(default=0)
    attack: int = fields.IntField(default=0)
    defense: int = fields.IntField(default=0)
    agility: int = fields.IntField(default=0)
    defense: int = fields.IntField(default=0)
    intelligence: int = fields.IntField(default=0)
    wild: int = fields.IntField(default=0)