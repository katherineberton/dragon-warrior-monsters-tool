"""Travelers gate definitions and data for Dragon Warrior Monsters."""

import enum
from typing import NamedTuple

from monsters.constants import MonsterSpecies, Species


class Joins(enum.IntEnum):
    """Whether or not a boss at the end of a travelers gate will join your party."""

    YES = 1
    NO = 2
    MAYBE = 3  # With sufficient treats


class TravelersGate(NamedTuple):
    """A travelers gate in the kingdom."""

    name: str
    slug: str
    location: str
    boss: list[Species]
    joins_type: Joins
    layers: int
    monsters: list[Species]


class TravelersGates:
    """All travelers gates in the kingdom."""

    BEGINNING = TravelersGate(
        name="Gate of Beginning",
        slug="beginning",
        location="Dungeon - Room of Beginner",
        layers=4,
        boss=[MonsterSpecies.HEALER],
        joins_type=Joins.YES,
        monsters=[MonsterSpecies.SLIME, MonsterSpecies.DRACKY, MonsterSpecies.ANTEATER],
    )
    VILLAGER = TravelersGate(
        name="Gate of Villager",
        slug="villager",
        location="Dungeon - Room of Villager and Talisman",
        layers=4,
        boss=[MonsterSpecies.DRAGON],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.STUBSUCK,
            MonsterSpecies.GOHOPPER,
            MonsterSpecies.ANTEATER,
            MonsterSpecies.PICKY,
            MonsterSpecies.GREMLIN,
            MonsterSpecies.PILLOWRAT,
        ],
    )
    TALISMAN = TravelersGate(
        name="Gate of Talisman",
        slug="talisman",
        location="Dungeon - Room of Villager and Talisman",
        layers=5,
        boss=[MonsterSpecies.GOLEM],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.SPOOKY,
            MonsterSpecies.ARMYANT,
            MonsterSpecies.ANTEATER,
            MonsterSpecies.MINIDRAK,
            MonsterSpecies.GOOPI,
            MonsterSpecies.PICKY,
        ],
    )
    MEMORIES = TravelersGate(
        name="Gate of Memories",
        slug="memories",
        location="Dungeon - Room of Memories and Bewilder",
        layers=4,
        boss=[MonsterSpecies.MADCAT],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.GOOPI,
            MonsterSpecies.PILLOWRAT,
            MonsterSpecies.DRAGONKID,
            MonsterSpecies.CATAPILA,
            MonsterSpecies.PICKY,
            MonsterSpecies.FAIRYRAT,
            MonsterSpecies.SPOTSLIME,
        ],
    )
    BEWILDER = TravelersGate(
        name="Gate of Bewilder",
        slug="bewilder",
        location="Dungeon - Room of Memories and Bewilder",
        layers=5,
        boss=[MonsterSpecies.FACETREE],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.MINIDRAK,
            MonsterSpecies.BIGROOST,
            MonsterSpecies.DRAGONKID,
            MonsterSpecies.SPOTSLIME,
            MonsterSpecies.EVILSEED,
            MonsterSpecies.DEMONITE,
            MonsterSpecies.CRESTPENT,
        ],
    )
    PEACE = TravelersGate(
        name="Gate of Peace",
        slug="peace",
        location="Dungeon - Room of Peace and Bravery",
        layers=7,
        boss=[MonsterSpecies.FANGSLIME],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.BIGROOST,
            MonsterSpecies.SPOTSLIME,
            MonsterSpecies.COILBIRD,
            MonsterSpecies.CRESTPENT,
            MonsterSpecies.DRAGONKID,
            MonsterSpecies.BONESLAVE,
            MonsterSpecies.ALMIRAJ,
            MonsterSpecies.HORK,
            MonsterSpecies.BULLBIRD,
        ],
    )
    BRAVERY = TravelersGate(
        name="Gate of Bravery",
        slug="bravery",
        location="Dungeon - Room of Peace and Bravery",
        layers=8,
        boss=[MonsterSpecies.BIGEYE],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.DEMONITE,
            MonsterSpecies.BEANMAN,
            MonsterSpecies.ONEEYECLOWN,
            MonsterSpecies.FLORAMAN,
            MonsterSpecies.SABREMAN,
            MonsterSpecies.GIANTWORM,
            MonsterSpecies.BULLBIRD,
        ],
    )
    STRENGTH = TravelersGate(
        name="Gate of Strength",
        slug="strength",
        location="Dungeon - Room of Strength and Anger",
        layers=10,
        boss=[MonsterSpecies.STONEMAN],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.MUDDOLL,
            MonsterSpecies.TREESLIME,
            MonsterSpecies.SKULRIDER,
            MonsterSpecies.FAIRYDRAK,
            MonsterSpecies.WINGTREE,
            MonsterSpecies.DRAKSLIME,
        ],
    )
    ANGER = TravelersGate(
        name="Gate of Anger",
        slug="anger",
        location="Dungeon - Room of Strength and Anger",
        layers=10,
        boss=[MonsterSpecies.BATTLEREX],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.GIANTWORM,
            MonsterSpecies.GIANTSLUG,
            MonsterSpecies.POISONGON,
            MonsterSpecies.CATFLY,
            MonsterSpecies.EYEDER,
            MonsterSpecies.PUTREPUP,
            MonsterSpecies.DRAKSLIME,
        ],
    )
    JOY = TravelersGate(
        name="Gate of Joy",
        slug="joy",
        location="Dungeon - Room of Joy and Wisdom",
        layers=13,
        boss=[MonsterSpecies.FUNKYBIRD],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.SNAILY,
            MonsterSpecies.SACCER,
            MonsterSpecies.GULPPLE,
            MonsterSpecies.MADPECKER,
            MonsterSpecies.EYEBALL,
            MonsterSpecies.BABBLE,
            MonsterSpecies.MUMMY,
        ],
    )
    WISDOM = TravelersGate(
        name="Gate of Wisdom",
        slug="wisdom",
        location="Dungeon - Room of Joy and Wisdom",
        layers=14,
        boss=[MonsterSpecies.SKYDRAGON],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.FACER,
            MonsterSpecies.TONGUELLA,
            MonsterSpecies.FLORAJAY,
            MonsterSpecies.PTERANOD,
            MonsterSpecies.ARMORPEDE,
        ],
    )
    HAPPINESS = TravelersGate(
        name="Gate of Happiness",
        slug="happiness",
        location="Dungeon - Room of Happiness and Temptation",
        layers=17,
        boss=[MonsterSpecies.JAMIRUS],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.ONIONO,
            MonsterSpecies.GOPHECADA,
            MonsterSpecies.PIXY,
            MonsterSpecies.GASGON,
            MonsterSpecies.DEADNITE,
            MonsterSpecies.STUBBIRD,
            MonsterSpecies.SPIKYBOY,
        ],
    )
    TEMPTATION = TravelersGate(
        name="Gate of Temptation",
        slug="temptation",
        location="Dungeon - Room of Happiness and Temptation",
        layers=19,
        boss=[MonsterSpecies.SERVANT],
        joins_type=Joins.MAYBE,
        monsters=[
            MonsterSpecies.SPIKYBOY,
            MonsterSpecies.KINGCOBRA,
            MonsterSpecies.MOMMONJA,
            MonsterSpecies.SLIMENITE,
            MonsterSpecies.STAGBUG,
            MonsterSpecies.MISTYWING,
            MonsterSpecies.DARKEYE,
        ],
    )
    LABYRINTH = TravelersGate(
        name="Gate of Labyrinth",
        slug="labyrinth",
        location="Dungeon - Room of Labyrinth and Judgment",
        layers=22,
        boss=[MonsterSpecies.DRAGON],
        joins_type=Joins.MAYBE,
        monsters=[
            MonsterSpecies.ROCKSLIME,
            MonsterSpecies.CHAMELGON,
            MonsterSpecies.CACTIBALL,
            MonsterSpecies.TAILEATER,
            MonsterSpecies.GISMO,
            MonsterSpecies.DUCKKITE,
            MonsterSpecies.CACTIBALL,
            MonsterSpecies.AGDEVIL,
            MonsterSpecies.WINDMERGE,
        ],
    )
    JUDGMENT = TravelersGate(
        name="Gate of Judgment",
        slug="judgment",
        location="Dungeon - Room of Labyrinth and Judgment",
        layers=24,
        boss=[MonsterSpecies.AKUBAR],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.WEEDBUG,
            MonsterSpecies.HAMMERMAN,
            MonsterSpecies.MADGOOSE,
            MonsterSpecies.TREEBOY,
            MonsterSpecies.SPOTKING,
            MonsterSpecies.DROLL,
            MonsterSpecies.LIZARDFLY,
            MonsterSpecies.GIANTMOTH,
            MonsterSpecies.SPOTKING,
        ],
    )
    REFLECTION = TravelersGate(
        name="Gate of Reflection",
        slug="reflection",
        location="Dungeon - Room of Reflection",
        layers=28,
        boss=[MonsterSpecies.DURRAN],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.EVILBEAST,
            MonsterSpecies.SHADOW,
            MonsterSpecies.EVILWAND,
            MonsterSpecies.SLIMEBORG,
            MonsterSpecies.LIZARDMAN,
            MonsterSpecies.GRIZZLY,
            MonsterSpecies.WYVERN,
            MonsterSpecies.FIREWEED,
            MonsterSpecies.MADHORNET,
            MonsterSpecies.LIONEX,
            MonsterSpecies.ROTRAVEN,
            MonsterSpecies.GRIZZLY,
            MonsterSpecies.JEWELBAG,
        ],
    )
    BAZAAR = TravelersGate(
        name="Bazaar Gate",
        slug="bazaar",
        location="Bazaar - consumes monster with fire",
        layers=8,
        boss=[MonsterSpecies.MADKNIGHT],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.FAIRYRAT,
            MonsterSpecies.BIGROOST,
            MonsterSpecies.SPOTSLIME,
            MonsterSpecies.CRESTPENT,
            MonsterSpecies.DRAGONKID,
            MonsterSpecies.CATAPILA,
            MonsterSpecies.BEANMAN,
            MonsterSpecies.DEMONITE,
            MonsterSpecies.HORK,
            MonsterSpecies.ONEEYECLOWN,
        ],
    )
    WELL = TravelersGate(
        name="Well Gate",
        slug="well",
        location="Well - consumes monster with electric",
        layers=11,
        boss=[MonsterSpecies.GIGANTES],
        joins_type=Joins.MAYBE,
        monsters=[
            MonsterSpecies.BONESLAVE,
            MonsterSpecies.ALMIRAJ,
            MonsterSpecies.FLORAMAN,
            MonsterSpecies.GIANTSLUG,
            MonsterSpecies.TREESLIME,
            MonsterSpecies.GIANTWORM,
            MonsterSpecies.BULLBIRD,
            MonsterSpecies.MUDDOLL,
            MonsterSpecies.SABREMAN,
            MonsterSpecies.METALY,
        ],
    )
    MONSTER_FARM = TravelersGate(
        name="Monster Farm Gate",
        slug="monster_farm",
        location="Monster Farm - first earthquake",
        layers=11,
        boss=[MonsterSpecies.COPYCAT],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.FAIRYDRAK,
            MonsterSpecies.BUTTERFLY,
            MonsterSpecies.MADRAVEN,
            MonsterSpecies.SKULLROO,
            MonsterSpecies.MUDRON,
            MonsterSpecies.DRAKSLIME,
        ],
    )
    GOOPI_1 = TravelersGate(
        name="Goopi's Gate #1",
        slug="goopi_1",
        location="Goopi's Gate - first earthquake",
        layers=15,
        boss=[MonsterSpecies.DIGSTER],
        joins_type=Joins.YES,
        monsters=[
            MonsterSpecies.WINGSLIME,
            MonsterSpecies.MADCANDLE,
            MonsterSpecies.MEDUSAEYE,
            MonsterSpecies.MADGOPHER,
            MonsterSpecies.SLABBIT,
            MonsterSpecies.WINDBEAST,
            MonsterSpecies.GASGON,
        ],
    )
    MEDAL_MAN = TravelersGate(
        name="Medal Man's Gate",
        slug="medal_man",
        location="Medal Man's room - 19 tinymedals",
        layers=18,
        boss=[MonsterSpecies.KINGSLIME, MonsterSpecies.LIPSY, MonsterSpecies.TOADSTOOL],
        joins_type=Joins.MAYBE,
        monsters=[
            MonsterSpecies.NITEWHIP,
            MonsterSpecies.BOXSLIME,
            MonsterSpecies.GISMO,
            MonsterSpecies.ORC,
            MonsterSpecies.ROGUENITE,
            MonsterSpecies.REAPER,
        ],
    )
    LIBRARY = TravelersGate(
        name="Library Gate",
        slug="library",
        location="Library - collect 100 monsters",
        layers=24,
        boss=[MonsterSpecies.OROCHI],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.ARCDEMON,
            MonsterSpecies.AMBERWEED,
            MonsterSpecies.ARMYCRAB,
            MonsterSpecies.MADSPIRIT,
            MonsterSpecies.CURSELAMP,
            MonsterSpecies.WILDAPE,
            MonsterSpecies.TORTRAGON,
            MonsterSpecies.LANDOWL,
        ],
    )
    AMBITION = TravelersGate(
        name="Gate of Ambition",
        slug="ambition",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.DRACOLORD1],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.GOHOPPER,
            MonsterSpecies.ARMYANT,
            MonsterSpecies.CATAPILA,
            MonsterSpecies.GIANTWORM,
            MonsterSpecies.GIANTSLUG,
            MonsterSpecies.EYEDER,
            MonsterSpecies.BUTTERFLY,
            MonsterSpecies.ARMORPEDE,
            MonsterSpecies.GOPHECADA,
            MonsterSpecies.STAGBUG,
            MonsterSpecies.TAILEATER,
            MonsterSpecies.WEEDBUG,
            MonsterSpecies.DROLL,
            MonsterSpecies.GIANTMOTH,
            MonsterSpecies.ARMYCRAB,
            MonsterSpecies.MADHORNET,
        ],
    )
    DEMOLITION = TravelersGate(
        name="Gate of Demolition",
        slug="demolition",
        location="Family Gates - win the starry night tournament",
        layers=28,
        boss=[MonsterSpecies.HARGON],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.STUBSUCK,
            MonsterSpecies.EVILSEED,
            MonsterSpecies.BEANMAN,
            MonsterSpecies.FLORAMAN,
            MonsterSpecies.WINGTREE,
            MonsterSpecies.GULPPLE,
            MonsterSpecies.MADPLANT,
            MonsterSpecies.ONIONO,
            MonsterSpecies.CACTIBALL,
            MonsterSpecies.TREEBOY,
            MonsterSpecies.AMBERWEED,
            MonsterSpecies.FIREWEED,
            MonsterSpecies.MANEATER,
            MonsterSpecies.DANCEVEGI,
            MonsterSpecies.SNAPPER,
        ],
    )
    MASTERMIND = TravelersGate(
        name="Gate of Mastermind",
        slug="mastermind",
        location="Family Gates - win the starry night tournament",
        layers=26,
        boss=[MonsterSpecies.BARAMOS],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.DRACKY,
            MonsterSpecies.PICKY,
            MonsterSpecies.BIGROOST,
            MonsterSpecies.BULLBIRD,
            MonsterSpecies.MADRAVEN,
            MonsterSpecies.MADPECKER,
            MonsterSpecies.FLORAJAY,
            MonsterSpecies.STUBBIRD,
            MonsterSpecies.MISTYWING,
            MonsterSpecies.DUCKKITE,
            MonsterSpecies.MADGOOSE,
            MonsterSpecies.LANDOWL,
            MonsterSpecies.WYVERN,
            MonsterSpecies.MADCONDOR,
            MonsterSpecies.ZAPBIRD,
            MonsterSpecies.WHIPBIRD,
        ],
    )
    CONTROL = TravelersGate(
        name="Gate of Control",
        slug="control",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.ZOMA],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.SLIME,
            MonsterSpecies.SPOTSLIME,
            MonsterSpecies.METALY,
            MonsterSpecies.TREESLIME,
            MonsterSpecies.DRAKSLIME,
            MonsterSpecies.SNAILY,
            MonsterSpecies.BABBLE,
            MonsterSpecies.WINGSLIME,
            MonsterSpecies.SLABBIT,
            MonsterSpecies.SLIMENITE,
            MonsterSpecies.BOXSLIME,
            MonsterSpecies.ROCKSLIME,
            MonsterSpecies.SPOTKING,
            MonsterSpecies.SLIMEBORG,
            MonsterSpecies.METABBLE,
        ],
    )
    EXTINCTION = TravelersGate(
        name="Gate of Extinction",
        slug="extinction",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.PIZZARO],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.GREMLIN,
            MonsterSpecies.DEMONITE,
            MonsterSpecies.ONEEYECLOWN,
            MonsterSpecies.SKULRIDER,
            MonsterSpecies.EYEBALL,
            MonsterSpecies.MEDUSAEYE,
            MonsterSpecies.PIXY,
            MonsterSpecies.DARKEYE,
            MonsterSpecies.ORC,
            MonsterSpecies.AGDEVIL,
            MonsterSpecies.ARCDEMON,
            MonsterSpecies.EVILBEAST,
            MonsterSpecies.LIONEX,
            MonsterSpecies.GRENDAL,
            MonsterSpecies.OGRE,
            MonsterSpecies.GOATHORN,
        ],
    )
    SLEEP = TravelersGate(
        name="Gate of Sleep",
        slug="sleep",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.ESTERK],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.SPOOKY,
            MonsterSpecies.HORK,
            MonsterSpecies.BONESLAVE,
            MonsterSpecies.PUTREPUP,
            MonsterSpecies.MUDRON,
            MonsterSpecies.MUMMY,
            MonsterSpecies.DEADNITE,
            MonsterSpecies.NITEWHIP,
            MonsterSpecies.REAPER,
            MonsterSpecies.WINDMERGE,
            MonsterSpecies.MADSPIRIT,
            MonsterSpecies.SHADOW,
            MonsterSpecies.ROTRAVEN,
            MonsterSpecies.DARKCRAB,
            MonsterSpecies.SKULLGON,
            MonsterSpecies.SKELETOR,
            MonsterSpecies.DEADNOBLE,
        ],
    )
    GOOPI_2 = TravelersGate(
        name="2nd Goopi's Gate",
        slug="goopi_2",
        location="Family Gates - win the starry night tournament",
        layers=26,
        boss=[MonsterSpecies.MUDOU],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.PILLOWRAT,
            MonsterSpecies.FAIRYRAT,
            MonsterSpecies.ALMIRAJ,
            MonsterSpecies.CATFLY,
            MonsterSpecies.SKULLROO,
            MonsterSpecies.SACCER,
            MonsterSpecies.TONGUELLA,
            MonsterSpecies.MADGOPHER,
            MonsterSpecies.WINDBEAST,
            MonsterSpecies.MOMMONJA,
            MonsterSpecies.GOATEGON,
            MonsterSpecies.HAMMERMAN,
            MonsterSpecies.WILDAPE,
            MonsterSpecies.GRIZZLY,
            MonsterSpecies.SUPERTEN,
            MonsterSpecies.YETI,
            MonsterSpecies.IRONTURT,
            MonsterSpecies.GULPBEAST,
            MonsterSpecies.TRUMPETER,
            MonsterSpecies.UNICORN,
        ],
    )
    BAZAAR_2 = TravelersGate(
        name="2nd Bazaar Gate",
        slug="bazaar_2",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.MIRUDRAAS1],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.GOOPI,
            MonsterSpecies.SABREMAN,
            MonsterSpecies.COILBIRD,
            MonsterSpecies.MUDDOLL,
            MonsterSpecies.FACER,
            MonsterSpecies.MADCANDLE,
            MonsterSpecies.SPIKYBOY,
            MonsterSpecies.ROGUENITE,
            MonsterSpecies.GISMO,
            MonsterSpecies.CURSELAMP,
            MonsterSpecies.EVILWAND,
            MonsterSpecies.JEWELBAG,
            MonsterSpecies.MADMIRROR,
            MonsterSpecies.VOODOLL,
            MonsterSpecies.BALZAK,
            MonsterSpecies.METALDRAK,
            MonsterSpecies.ROBOSTER,
            MonsterSpecies.BOMBCRAG,
        ],
    )
    GRANDPA = TravelersGate(
        name="Grandpa's Gate",
        slug="grandpa",
        location="Family Gates - win the starry night tournament",
        layers=29,
        boss=[MonsterSpecies.DEATHMORE1],
        joins_type=Joins.NO,
        monsters=[
            MonsterSpecies.MINIDRAK,
            MonsterSpecies.DRAGONKID,
            MonsterSpecies.CRESTPENT,
            MonsterSpecies.POISONGON,
            MonsterSpecies.FAIRYDRAK,
            MonsterSpecies.PTERANOD,
            MonsterSpecies.GASGON,
            MonsterSpecies.KINGCOBRA,
            MonsterSpecies.CHAMELGON,
            MonsterSpecies.LIZARDFLY,
            MonsterSpecies.TORTRAGON,
            MonsterSpecies.LIZARDMAN,
            MonsterSpecies.SWORDGON,
            MonsterSpecies.WINGSNAKE,
            MonsterSpecies.RAYBURN,
            MonsterSpecies.SPIKEROUS,
            MonsterSpecies.MADDRAGON,
            MonsterSpecies.ANDREAL,
            MonsterSpecies.GREATDRAK,
        ],
    )

    @property
    def all(self) -> list[TravelersGate]:
        """Return all TravelersGate instances defined on this class."""
        return [
            gate
            for gate in self.__class__.__dict__.values()
            if isinstance(gate, TravelersGate)
        ]

    def get_by_monster(self, species_id: int) -> list[TravelersGate]:
        """Return gates that include the given monster species."""
        return [gate for gate in self.all if species_id in [monster.id for monster in gate.monsters]]
