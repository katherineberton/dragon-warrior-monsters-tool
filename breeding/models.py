from __future__ import annotations

from tortoise import fields
import base_models
import constants
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monsters.models import Monster


class BreedingPlan(base_models.BaseModel):
    """A plan with a target monster species for users to assign their monsters to."""
    target: Monster = fields.ForeignKeyField('monsters.Monster', related_name='breeding_plans')
    target_level: int | None = fields.IntField(null=True)

    def get_shortest_path(self):
        """From a user's current set of monsters, assigned or unassigned, get the shortest combination of monsters required to achieve it."""
        # This algorithm is going to be somethin else

class BreedingEvent(base_models.BaseModel):
    """A breeding pair initiated to achieve a breeding plan."""
    male: Monster = fields.ForeignKeyField('monsters.Monster', related_name='breeding_plans') # reverse relationship breeding_steps
    female: Monster = fields.ForeignKeyField('monsters.Monster', related_name='breeding_plans')# reverse relationship breeding_steps
    pedigree: constants.MonsterGenders = fields.SmallIntEnumField(constants.MonsterGenders)

    @property
    def pedigree_id(self):
        return self.female_id if self.pedigree == constants.MonsterGenders.FEMALE else self.male_id