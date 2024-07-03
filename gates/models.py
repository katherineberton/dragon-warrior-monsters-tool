from __future__ import annotations

from tortoise import fields

import base_models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monsters.models import Monster


class Gate(base_models.BaseModel):
    """A travelers gate through which monsters can be fought and collected."""
    name: str = fields.CharField(max_length=255)
    levels: int = fields.IntField(default=4)
    location: str = fields.TextField()
    boss: Monster | None = fields.OneToOneField('monsters.Monster', related_name="gate", null=True)


class MonsterGateMembership(base_models.BaseModel):
    """Gates and levels in which a particular monster species can be caught in the wild."""
    monster: Monster = fields.ForeignKeyField('monsters.Monster')
    gate: Gate = fields.ForeignKeyField('gates.Gate')
    levels: str = fields.CharField(max_length=255)