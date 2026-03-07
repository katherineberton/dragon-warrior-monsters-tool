"""Breeding mechanics for dragon warrior monsters."""

from typing import overload

from breeding.constants import Recipe, Recipes
from monsters.constants import MonsterFamily, Species


def get_breeding_result(
    pedigree: Species,
    mate: Species,
) -> Species:
    """Get the result of a breeding event."""
    species_species_result = _get_recipes(pedigree, mate)
    if species_species_result:
        return species_species_result[0].result

    species_family_result = _get_recipes(pedigree, mate.family)
    if species_family_result:
        return species_family_result[0].result

    family_species_result = _get_recipes(pedigree.family, mate)
    if family_species_result:
        return family_species_result[0].result

    family_family_result = _get_recipes(pedigree.family, mate.family)
    if family_family_result:
        return family_family_result[0].result

    return pedigree


def _get_recipes(
    pedigree: Species | MonsterFamily,
    mate: Species | MonsterFamily,
) -> list[Recipe]:
    """Get the breeding recipes for the given pedigree and mate."""
    if isinstance(pedigree, Species) and isinstance(mate, Species):
        return _get_species_species_recipe(pedigree, mate)
    if isinstance(pedigree, Species) and isinstance(mate, MonsterFamily):
        return _get_species_family_recipe(pedigree, mate)
    if isinstance(pedigree, MonsterFamily) and isinstance(mate, Species):
        return _get_family_species_recipe(pedigree, mate)
    if isinstance(pedigree, MonsterFamily) and isinstance(mate, MonsterFamily):
        return _get_family_family_recipe(pedigree, mate)
    return []


@overload
def _get_breeding_partner(partner: Species) -> int: ...
@overload
def _get_breeding_partner(partner: MonsterFamily) -> MonsterFamily: ...
def _get_breeding_partner(partner: Species | MonsterFamily) -> int | MonsterFamily:
    if isinstance(partner, MonsterFamily):
        return partner
    return partner.id


recipes = Recipes()


def _get_species_species_recipe(
    pedigree: Species,
    mate: Species,
) -> list[Recipe]:
    """Given a pedigree and a mate, check the breeding rules to see if there is a species/species recipe for the combination."""
    recipes_by_pedigree = recipes.get(
        role="pedigree",
        species_id=_get_breeding_partner(pedigree),
    )
    return recipes.get(
        role="mate",
        species_id=_get_breeding_partner(mate),
        recipes=recipes_by_pedigree,
    )


def _get_species_family_recipe(
    pedigree: Species,
    mate: MonsterFamily,
) -> list[Recipe]:
    """Given a pedigree and a mate, check the breeding rules to see if there is a recipe for the combination of the pedigree's species and the mate's family."""
    recipes_by_pedigree = recipes.get(
        role="pedigree",
        species_id=_get_breeding_partner(pedigree),
    )
    return recipes.get(
        role="mate",
        family=_get_breeding_partner(mate),
        recipes=recipes_by_pedigree,
    )


def _get_family_species_recipe(
    pedigree: MonsterFamily,
    mate: Species,
) -> list[Recipe]:
    """Given a pedigree and a mate, check the breeding rules to see if there is a recipe for the combination of the pedigree's family and the mate's species."""
    recipes_by_pedigree = recipes.get(
        role="pedigree",
        family=_get_breeding_partner(pedigree),
    )
    return recipes.get(
        role="mate",
        species_id=_get_breeding_partner(mate),
        recipes=recipes_by_pedigree,
    )


def _get_family_family_recipe(
    pedigree: MonsterFamily,
    mate: MonsterFamily,
) -> list[Recipe]:
    """Given a pedigree and a mate, check the breeding rules to see if there is a recipe for the combination of the pedigree's family and the mate's family."""
    recipes_by_pedigree = recipes.get(
        role="pedigree",
        family=_get_breeding_partner(pedigree),
    )
    return recipes.get(
        role="mate",
        family=_get_breeding_partner(mate),
        recipes=recipes_by_pedigree,
    )
