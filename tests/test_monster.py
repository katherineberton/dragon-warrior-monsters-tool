"""Tests for the Monster class."""

from src.monsters import Monster


def test_monster_creation():
    """Test basic monster creation."""
    monster = Monster(
        name="Slime",
        hp=10,
        max_hp=10,
        mp=5,
        max_mp=5,
        attack=5,
        defense=3,
        agility=2,
        intelligence=1,
    )

    assert monster.name == "Slime"
    assert monster.hp == 10
    assert monster.max_hp == 10
    assert monster.mp == 5
    assert monster.max_mp == 5
    assert monster.attack == 5
    assert monster.defense == 3
    assert monster.agility == 2
    assert monster.intelligence == 1
    assert monster.skills == []


def test_monster_damage():
    """Test monster damage mechanics."""
    monster = Monster(
        name="Slime",
        hp=10,
        max_hp=10,
    )

    monster.take_damage(5)
    assert monster.hp == 5
    assert monster.is_alive()

    monster.take_damage(10)
    assert monster.hp == 0
    assert not monster.is_alive()


def test_monster_healing():
    """Test monster healing mechanics."""
    monster = Monster(
        name="Slime",
        hp=5,
        max_hp=10,
    )

    monster.heal(3)
    assert monster.hp == 8

    monster.heal(5)
    assert monster.hp == 10  # Should not exceed max_hp


def test_monster_mp_usage():
    """Test monster MP usage."""
    monster = Monster(
        name="Slime",
        mp=10,
        max_mp=10,
    )

    assert monster.use_mp(5)
    assert monster.mp == 5

    assert not monster.use_mp(10)  # Not enough MP
    assert monster.mp == 5  # MP should not change
