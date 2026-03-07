"""Tests for breeding.utils."""

from breeding.utils import get_breeding_result
from monsters.constants import MonsterSpecies


def test_slime_and_dragon_breed_drakslime() -> None:
    """Slime family + Dragon family yields Drakslime."""
    result = get_breeding_result(
        pedigree=MonsterSpecies.SLIME,
        mate=MonsterSpecies.DRAGON,
    )
    assert result == MonsterSpecies.DRAKSLIME
