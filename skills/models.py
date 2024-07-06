from __future__ import annotations

from tortoise import fields
import base_models
import constants
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monsters.models import MonsterSpecies



class Skill(base_models.BaseModel):
    """The details and effect of a special attack."""
    name: str = fields.CharField(max_length=255)
    slug: str = fields.CharField(max_length=255)
    base_level: Skill = fields.ForeignKeyField('skills.Skill', related_name='higher_levels')
    level: int = fields.IntField(default=1)
    required_monster_level: int = fields.IntField()
    description: str | None = fields.TextField(null=True)
    combination: Skill | None = fields.ForeignKeyField('skills.Skill', related_name='combined_skills')



class SkillStatRequirement(base_models.BaseModel):
    """A stat requirement that a monster must have before it can learn a skill."""
    skill: Skill = fields.ForeignKeyField('skills.Skill', related_name='skill_stat_requirements')
    stat: constants.StatTypes = fields.SmallIntEnumField(constants.StatTypes)
    score: int = fields.IntField(default=1)


class SpeciesSkill(base_models.BaseModel):
    """A special attack automatically learned by a species."""
    monster_species: MonsterSpecies = fields.ForeignKeyField('models.MonsterSpecies', related_name='species_skills')
    skill: Skill = fields.ForeignKeyField('skills.Skill', related_name="species_skills")
