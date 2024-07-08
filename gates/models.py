from __future__ import annotations
import enum
from tortoise import fields
import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monsters.models import Monster


class CatchabilityType(enum.IntEnum):
    ALWAYS = 1
    NEVER = 2
    SUBJECT_TO_TREATS = 3

class Gate(models.BaseModel):
    """A travelers gate through which monsters can be fought and collected."""
    name: str = fields.CharField(max_length=255)
    slug: str = fields.CharField(max_length=255)
    levels: int = fields.IntField(default=4)
    location: str = fields.TextField()
    boss_catchablility: CatchabilityType = fields.SmallIntField(CatchabilityType, default=CatchabilityType.ALWAYS.value)


class MonsterGateMembership(models.BaseModel):
    """Gates and levels in which a particular monster species can be caught in the wild."""
    monster: Monster = fields.ForeignKeyField('monsters.Monster')
    gate: Gate = fields.ForeignKeyField('gates.Gate')