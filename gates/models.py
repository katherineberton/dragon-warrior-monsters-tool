from __future__ import annotations
import enum
from tortoise import fields
import base_models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monsters.models import Monster


class CatchableType(enum.IntEnum):
    ALWAYS = 1
    NEVER = 2
    SUBJECT_TO_TREATS = 3

class Gate(base_models.BaseModel):
    """A travelers gate through which monsters can be fought and collected."""
    name: str = fields.CharField(max_length=255)
    slug: str = fields.CharField(max_length=255)
    levels: int = fields.IntField(default=4)
    location: str = fields.TextField()
    catchable_boss: CatchableType = fields.SmallIntEnumField(CatchableType, default=CatchableType.ALWAYS)


class MonsterGateMembership(base_models.BaseModel):
    """Gates and levels in which a particular monster species can be caught in the wild."""
    monster: Monster = fields.ForeignKeyField('monsters.Monster')
    gate: Gate = fields.ForeignKeyField('gates.Gate')