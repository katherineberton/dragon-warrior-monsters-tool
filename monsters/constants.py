"""Monster species, families, and related constants for Dragon Warrior Monsters."""

import enum
from typing import NamedTuple


class MonsterFamily(enum.IntEnum):
    """Monster family types."""

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


class Species(NamedTuple):
    """A monster species."""

    id: int
    name: str
    slug: str
    family: MonsterFamily


class MonsterSpecies:
    """All monster species."""

    DRAKSLIME = Species(
        id=1,
        name="Drakslime",
        slug="drakslime",
        family=MonsterFamily.SLIME,
    )
    SPOTSLIME = Species(
        id=2,
        name="Spotslime",
        slug="spotslime",
        family=MonsterFamily.SLIME,
    )
    WINGSLIME = Species(
        id=3,
        name="Wingslime",
        slug="wingslime",
        family=MonsterFamily.SLIME,
    )
    TREESLIME = Species(
        id=4,
        name="Treeslime",
        slug="treeslime",
        family=MonsterFamily.SLIME,
    )
    SNAILY = Species(
        id=5,
        name="Snaily",
        slug="snaily",
        family=MonsterFamily.SLIME,
    )
    SLIMENITE = Species(
        id=6,
        name="SlimeNite",
        slug="slimenite",
        family=MonsterFamily.SLIME,
    )
    BABBLE = Species(
        id=7,
        name="Babble",
        slug="babble",
        family=MonsterFamily.SLIME,
    )
    BOXSLIME = Species(
        id=8,
        name="BoxSlime",
        slug="boxslime",
        family=MonsterFamily.SLIME,
    )
    SLIME = Species(
        id=9,
        name="Slime",
        slug="slime",
        family=MonsterFamily.SLIME,
    )
    HEALER = Species(
        id=10,
        name="Healer",
        slug="healer",
        family=MonsterFamily.SLIME,
    )
    FANGSLIME = Species(
        id=11,
        name="FangSlime",
        slug="fangslime",
        family=MonsterFamily.SLIME,
    )
    ROCKSLIME = Species(
        id=12,
        name="RockSlime",
        slug="rockslime",
        family=MonsterFamily.SLIME,
    )
    SLIMEBORG = Species(
        id=13,
        name="SlimeBorg",
        slug="slimeborg",
        family=MonsterFamily.SLIME,
    )
    SLABBIT = Species(
        id=14,
        name="Slabbit",
        slug="slabbit",
        family=MonsterFamily.SLIME,
    )
    SPOTKING = Species(
        id=15,
        name="SpotKing",
        slug="spotking",
        family=MonsterFamily.SLIME,
    )
    KINGSLIME = Species(
        id=16,
        name="KingSlime",
        slug="kingslime",
        family=MonsterFamily.SLIME,
    )
    METALY = Species(
        id=17,
        name="Metaly",
        slug="metaly",
        family=MonsterFamily.SLIME,
    )
    METABBLE = Species(
        id=18,
        name="Metabble",
        slug="metabble",
        family=MonsterFamily.SLIME,
    )
    METALKING = Species(
        id=19,
        name="MetalKing",
        slug="metalking",
        family=MonsterFamily.SLIME,
    )
    GOLDSLIME = Species(
        id=20,
        name="GoldSlime",
        slug="goldslime",
        family=MonsterFamily.SLIME,
    )
    DRAGONKID = Species(
        id=21,
        name="DragonKid",
        slug="dragonkid",
        family=MonsterFamily.DRAGON,
    )
    TORTRAGON = Species(
        id=22,
        name="Tortragon",
        slug="tortragon",
        family=MonsterFamily.DRAGON,
    )
    PTERANOD = Species(
        id=23,
        name="Pteranod",
        slug="pteranod",
        family=MonsterFamily.DRAGON,
    )
    GASGON = Species(
        id=24,
        name="Gasgon",
        slug="gasgon",
        family=MonsterFamily.DRAGON,
    )
    FAIRYDRAK = Species(
        id=25,
        name="FairyDrak",
        slug="fairydrak",
        family=MonsterFamily.DRAGON,
    )
    LIZARDMAN = Species(
        id=26,
        name="LizardMan",
        slug="lizardman",
        family=MonsterFamily.DRAGON,
    )
    POISONGON = Species(
        id=27,
        name="Poisongon",
        slug="poisongon",
        family=MonsterFamily.DRAGON,
    )
    SWORDGON = Species(
        id=28,
        name="Swordgon",
        slug="swordgon",
        family=MonsterFamily.DRAGON,
    )
    DRAGON = Species(
        id=29,
        name="Dragon",
        slug="dragon",
        family=MonsterFamily.DRAGON,
    )
    MINIDRAK = Species(
        id=30,
        name="MiniDrak",
        slug="minidrak",
        family=MonsterFamily.DRAGON,
    )
    MADDRAGON = Species(
        id=31,
        name="MadDragon",
        slug="maddragon",
        family=MonsterFamily.DRAGON,
    )
    RAYBURN = Species(
        id=32,
        name="Rayburn",
        slug="rayburn",
        family=MonsterFamily.DRAGON,
    )
    CHAMELGON = Species(
        id=33,
        name="Chamelgon",
        slug="chamelgon",
        family=MonsterFamily.DRAGON,
    )
    LIZARDFLY = Species(
        id=34,
        name="LizardFly",
        slug="lizardfly",
        family=MonsterFamily.DRAGON,
    )
    ANDREAL = Species(
        id=35,
        name="Andreal",
        slug="andreal",
        family=MonsterFamily.DRAGON,
    )
    KINGCOBRA = Species(
        id=36,
        name="KingCobra",
        slug="kingcobra",
        family=MonsterFamily.DRAGON,
    )
    SPIKEROUS = Species(
        id=37,
        name="Spikerous",
        slug="spikerous",
        family=MonsterFamily.DRAGON,
    )
    GREATDRAK = Species(
        id=38,
        name="GreatDrak",
        slug="greatdrak",
        family=MonsterFamily.DRAGON,
    )
    CRESTPENT = Species(
        id=39,
        name="Crestpent",
        slug="crestpent",
        family=MonsterFamily.DRAGON,
    )
    WINGSNAKE = Species(
        id=40,
        name="WingSnake",
        slug="wingsnake",
        family=MonsterFamily.DRAGON,
    )
    COATOL = Species(
        id=41,
        name="Coatol",
        slug="coatol",
        family=MonsterFamily.DRAGON,
    )
    OROCHI = Species(
        id=42,
        name="Orochi",
        slug="orochi",
        family=MonsterFamily.DRAGON,
    )
    BATTLEREX = Species(
        id=43,
        name="BattleRex",
        slug="battlerex",
        family=MonsterFamily.DRAGON,
    )
    SKYDRAGON = Species(
        id=44,
        name="SkyDragon",
        slug="skydragon",
        family=MonsterFamily.DRAGON,
    )
    DIVINEGON = Species(
        id=45,
        name="Divinegon",
        slug="divinegon",
        family=MonsterFamily.DRAGON,
    )
    TONGUELLA = Species(
        id=46,
        name="Tonguella",
        slug="tonguella",
        family=MonsterFamily.BEAST,
    )
    ALMIRAJ = Species(
        id=47,
        name="Almiraj",
        slug="almiraj",
        family=MonsterFamily.BEAST,
    )
    CATFLY = Species(
        id=48,
        name="CatFly",
        slug="catfly",
        family=MonsterFamily.BEAST,
    )
    PILLOWRAT = Species(
        id=49,
        name="PillowRat",
        slug="pillowrat",
        family=MonsterFamily.BEAST,
    )
    SACCER = Species(
        id=50,
        name="Saccer",
        slug="saccer",
        family=MonsterFamily.BEAST,
    )
    GULPBEAST = Species(
        id=51,
        name="GulpBeast",
        slug="gulpbeast",
        family=MonsterFamily.BEAST,
    )
    SKULLROO = Species(
        id=52,
        name="Skullroo",
        slug="skullroo",
        family=MonsterFamily.BEAST,
    )
    WINDBEAST = Species(
        id=53,
        name="WindBeast",
        slug="windbeast",
        family=MonsterFamily.BEAST,
    )
    ANTEATER = Species(
        id=54,
        name="Anteater",
        slug="anteater",
        family=MonsterFamily.BEAST,
    )
    SUPERTEN = Species(
        id=55,
        name="SuperTen",
        slug="superten",
        family=MonsterFamily.BEAST,
    )
    IRONTURT = Species(
        id=56,
        name="IronTurt",
        slug="ironturt",
        family=MonsterFamily.BEAST,
    )
    MOMMONJA = Species(
        id=57,
        name="Mommonja",
        slug="mommonja",
        family=MonsterFamily.BEAST,
    )
    HAMMERMAN = Species(
        id=58,
        name="HammerMan",
        slug="hammerman",
        family=MonsterFamily.BEAST,
    )
    GRIZZLY = Species(
        id=59,
        name="Grizzly",
        slug="grizzly",
        family=MonsterFamily.BEAST,
    )
    YETI = Species(
        id=60,
        name="Yeti",
        slug="yeti",
        family=MonsterFamily.BEAST,
    )
    MADGOPHER = Species(
        id=61,
        name="MadGopher",
        slug="madgopher",
        family=MonsterFamily.BEAST,
    )
    FAIRYRAT = Species(
        id=62,
        name="FairyRat",
        slug="fairyrat",
        family=MonsterFamily.BEAST,
    )
    UNICORN = Species(
        id=63,
        name="Unicorn",
        slug="unicorn",
        family=MonsterFamily.BEAST,
    )
    GOATEGON = Species(
        id=64,
        name="Goategon",
        slug="goategon",
        family=MonsterFamily.BEAST,
    )
    WILDAPE = Species(
        id=65,
        name="WildApe",
        slug="wildape",
        family=MonsterFamily.BEAST,
    )
    TRUMPETER = Species(
        id=66,
        name="Trumpeter",
        slug="trumpeter",
        family=MonsterFamily.BEAST,
    )
    KINGLEO = Species(
        id=67,
        name="KingLeo",
        slug="kingleo",
        family=MonsterFamily.BEAST,
    )
    DARKHORN = Species(
        id=68,
        name="DarkHorn",
        slug="darkhorn",
        family=MonsterFamily.BEAST,
    )
    MADCAT = Species(
        id=69,
        name="MadCat",
        slug="madcat",
        family=MonsterFamily.BEAST,
    )
    BIGEYE = Species(
        id=70,
        name="BigEye",
        slug="bigeye",
        family=MonsterFamily.BEAST,
    )
    PICKY = Species(
        id=71,
        name="Picky",
        slug="picky",
        family=MonsterFamily.BIRD,
    )
    WYVERN = Species(
        id=72,
        name="Wyvern",
        slug="wyvern",
        family=MonsterFamily.BIRD,
    )
    BULLBIRD = Species(
        id=73,
        name="BullBird",
        slug="bullbird",
        family=MonsterFamily.BIRD,
    )
    FLORAJAY = Species(
        id=74,
        name="FloraJay",
        slug="florajay",
        family=MonsterFamily.BIRD,
    )
    DUCKKITE = Species(
        id=75,
        name="DuckKite",
        slug="duckkite",
        family=MonsterFamily.BIRD,
    )
    MADPECKER = Species(
        id=76,
        name="MadPecker",
        slug="madpecker",
        family=MonsterFamily.BIRD,
    )
    MADRAVEN = Species(
        id=77,
        name="MadRaven",
        slug="madraven",
        family=MonsterFamily.BIRD,
    )
    MISTYWING = Species(
        id=78,
        name="MistyWing",
        slug="mistywing",
        family=MonsterFamily.BIRD,
    )
    DRACKY = Species(
        id=79,
        name="Dracky",
        slug="dracky",
        family=MonsterFamily.BIRD,
    )
    BIGROOST = Species(
        id=80,
        name="BigRoost",
        slug="bigroost",
        family=MonsterFamily.BIRD,
    )
    STUBBIRD = Species(
        id=81,
        name="StubBird",
        slug="stubbird",
        family=MonsterFamily.BIRD,
    )
    LANDOWL = Species(
        id=82,
        name="LandOwl",
        slug="landowl",
        family=MonsterFamily.BIRD,
    )
    MADGOOSE = Species(
        id=83,
        name="MadGoose",
        slug="madgoose",
        family=MonsterFamily.BIRD,
    )
    MADCONDOR = Species(
        id=84,
        name="MadCondor",
        slug="madcondor",
        family=MonsterFamily.BIRD,
    )
    BLIZZARDY = Species(
        id=85,
        name="Blizzardy",
        slug="blizzardy",
        family=MonsterFamily.BIRD,
    )
    PHOENIX = Species(
        id=86,
        name="Phoenix",
        slug="phoenix",
        family=MonsterFamily.BIRD,
    )
    ZAPBIRD = Species(
        id=87,
        name="ZapBird",
        slug="zapbird",
        family=MonsterFamily.BIRD,
    )
    WHIPBIRD = Species(
        id=88,
        name="WhipBird",
        slug="whipbird",
        family=MonsterFamily.BIRD,
    )
    FUNKYBIRD = Species(
        id=89,
        name="FunkyBird",
        slug="funkybird",
        family=MonsterFamily.BIRD,
    )
    RAINHAWK = Species(
        id=90,
        name="RainHawk",
        slug="rainhawk",
        family=MonsterFamily.BIRD,
    )
    MADPLANT = Species(
        id=91,
        name="MadPlant",
        slug="madplant",
        family=MonsterFamily.PLANT,
    )
    FIREWEED = Species(
        id=92,
        name="fireWeed",
        slug="fireweed",
        family=MonsterFamily.PLANT,
    )
    FLORAMAN = Species(
        id=93,
        name="FloraMan",
        slug="floraman",
        family=MonsterFamily.PLANT,
    )
    WINGTREE = Species(
        id=94,
        name="WingTree",
        slug="wingtree",
        family=MonsterFamily.PLANT,
    )
    CACTIBALL = Species(
        id=95,
        name="CactiBall",
        slug="cactiball",
        family=MonsterFamily.PLANT,
    )
    GULPPLE = Species(
        id=96,
        name="Gulpple",
        slug="gulpple",
        family=MonsterFamily.PLANT,
    )
    TOADSTOOL = Species(
        id=97,
        name="Toadstool",
        slug="toadstool",
        family=MonsterFamily.PLANT,
    )
    AMBERWEED = Species(
        id=98,
        name="AmberWeed",
        slug="amberweed",
        family=MonsterFamily.PLANT,
    )
    STUBSUCK = Species(
        id=99,
        name="StubSuck",
        slug="stubsuck",
        family=MonsterFamily.PLANT,
    )
    ONIONO = Species(
        id=100,
        name="Oniono",
        slug="oniono",
        family=MonsterFamily.PLANT,
    )
    DANCEVEGI = Species(
        id=101,
        name="DanceVegi",
        slug="dancevegi",
        family=MonsterFamily.PLANT,
    )
    TREEBOY = Species(
        id=102,
        name="TreeBoy",
        slug="treeboy",
        family=MonsterFamily.PLANT,
    )
    FACETREE = Species(
        id=103,
        name="FaceTree",
        slug="facetree",
        family=MonsterFamily.PLANT,
    )
    HERBMAN = Species(
        id=104,
        name="HerbMan",
        slug="herbman",
        family=MonsterFamily.PLANT,
    )
    BEANMAN = Species(
        id=105,
        name="BeanMan",
        slug="beanman",
        family=MonsterFamily.PLANT,
    )
    EVILSEED = Species(
        id=106,
        name="EvilSeed",
        slug="evilseed",
        family=MonsterFamily.PLANT,
    )
    MANEATER = Species(
        id=107,
        name="ManEater",
        slug="maneater",
        family=MonsterFamily.PLANT,
    )
    SNAPPER = Species(
        id=108,
        name="Snapper",
        slug="snapper",
        family=MonsterFamily.PLANT,
    )
    ROSEVINE = Species(
        id=109,
        name="Rosevine",
        slug="rosevine",
        family=MonsterFamily.PLANT,
    )
    WATABOU = Species(
        id=110,
        name="Watabou",
        slug="watabou",
        family=MonsterFamily.PLANT,
    )
    GIANTSLUG = Species(
        id=111,
        name="GiantSlug",
        slug="giantslug",
        family=MonsterFamily.BUG,
    )
    CATAPILA = Species(
        id=112,
        name="CataPila",
        slug="catapila",
        family=MonsterFamily.BUG,
    )
    GOPHECADA = Species(
        id=113,
        name="GopheCada",
        slug="gophecada",
        family=MonsterFamily.BUG,
    )
    BUTTERFLY = Species(
        id=114,
        name="Butterfly",
        slug="butterfly",
        family=MonsterFamily.BUG,
    )
    WEEDBUG = Species(
        id=115,
        name="Weedbug",
        slug="weedbug",
        family=MonsterFamily.BUG,
    )
    GIANTWORM = Species(
        id=116,
        name="GiantWorm",
        slug="giantworm",
        family=MonsterFamily.BUG,
    )
    LIPSY = Species(
        id=117,
        name="Lipsy",
        slug="lipsy",
        family=MonsterFamily.BUG,
    )
    STAGBUG = Species(
        id=118,
        name="StagBug",
        slug="stagbug",
        family=MonsterFamily.BUG,
    )
    ARMYANT = Species(
        id=119,
        name="ArmyAnt",
        slug="armyant",
        family=MonsterFamily.BUG,
    )
    GOHOPPER = Species(
        id=120,
        name="Gohopper",
        slug="gohopper",
        family=MonsterFamily.BUG,
    )
    TAILEATER = Species(
        id=121,
        name="TailEater",
        slug="taileater",
        family=MonsterFamily.BUG,
    )
    ARMORPEDE = Species(
        id=122,
        name="ArmorPede",
        slug="armorpede",
        family=MonsterFamily.BUG,
    )
    EYEDER = Species(
        id=123,
        name="Eyeder",
        slug="eyeder",
        family=MonsterFamily.BUG,
    )
    GIANTMOTH = Species(
        id=124,
        name="GiantMoth",
        slug="giantmoth",
        family=MonsterFamily.BUG,
    )
    DROLL = Species(
        id=125,
        name="Droll",
        slug="droll",
        family=MonsterFamily.BUG,
    )
    ARMYCRAB = Species(
        id=126,
        name="ArmyCrab",
        slug="armycrab",
        family=MonsterFamily.BUG,
    )
    MADHORNET = Species(
        id=127,
        name="MadHornet",
        slug="madhornet",
        family=MonsterFamily.BUG,
    )
    HORNBEET = Species(
        id=128,
        name="HornBeet",
        slug="hornbeet",
        family=MonsterFamily.BUG,
    )
    ARMORPION = Species(
        id=129,
        name="Armorpion",
        slug="armorpion",
        family=MonsterFamily.BUG,
    )
    DIGSTER = Species(
        id=130,
        name="Digster",
        slug="digster",
        family=MonsterFamily.BUG,
    )
    PIXY = Species(
        id=131,
        name="Pixy",
        slug="pixy",
        family=MonsterFamily.DEVIL,
    )
    ARCDEMON = Species(
        id=132,
        name="ArcDemon",
        slug="arcdemon",
        family=MonsterFamily.DEVIL,
    )
    AGDEVIL = Species(
        id=133,
        name="AgDevil",
        slug="agdevil",
        family=MonsterFamily.DEVIL,
    )
    DEMONITE = Species(
        id=134,
        name="Demonite",
        slug="demonite",
        family=MonsterFamily.DEVIL,
    )
    DARKEYE = Species(
        id=135,
        name="DarkEye",
        slug="darkeye",
        family=MonsterFamily.DEVIL,
    )
    EYEBALL = Species(
        id=136,
        name="eyeBall",
        slug="eyeball",
        family=MonsterFamily.DEVIL,
    )
    SKULRIDER = Species(
        id=137,
        name="SkulRider",
        slug="skulrider",
        family=MonsterFamily.DEVIL,
    )
    EVILBEAST = Species(
        id=138,
        name="EvilBeast",
        slug="evilbeast",
        family=MonsterFamily.DEVIL,
    )
    ONEEYECLOWN = Species(
        id=139,
        name="1EyeClown",
        slug="1eyeclown",
        family=MonsterFamily.DEVIL,
    )
    GREMLIN = Species(
        id=140,
        name="Gremlin",
        slug="gremlin",
        family=MonsterFamily.DEVIL,
    )
    MEDUSAEYE = Species(
        id=141,
        name="MedusaEye",
        slug="medusaeye",
        family=MonsterFamily.DEVIL,
    )
    LIONEX = Species(
        id=142,
        name="Lionex",
        slug="lionex",
        family=MonsterFamily.DEVIL,
    )
    GOATHORN = Species(
        id=143,
        name="GoatHorn",
        slug="goathorn",
        family=MonsterFamily.DEVIL,
    )
    ORC = Species(
        id=144,
        name="Orc",
        slug="orc",
        family=MonsterFamily.DEVIL,
    )
    OGRE = Species(
        id=145,
        name="Ogre",
        slug="ogre",
        family=MonsterFamily.DEVIL,
    )
    GATEGUARD = Species(
        id=146,
        name="GateGuard",
        slug="gateguard",
        family=MonsterFamily.DEVIL,
    )
    CHOPCLOWN = Species(
        id=147,
        name="ChopClown",
        slug="chopclown",
        family=MonsterFamily.DEVIL,
    )
    GRENDAL = Species(
        id=148,
        name="Grendal",
        slug="grendal",
        family=MonsterFamily.DEVIL,
    )
    AKUBAR = Species(
        id=149,
        name="Akubar",
        slug="akubar",
        family=MonsterFamily.DEVIL,
    )
    MADKNIGHT = Species(
        id=150,
        name="MadKnight",
        slug="madknight",
        family=MonsterFamily.DEVIL,
    )
    GIGANTES = Species(
        id=151,
        name="Gigantes",
        slug="gigantes",
        family=MonsterFamily.DEVIL,
    )
    CENTASAUR = Species(
        id=152,
        name="Centasaur",
        slug="centasaur",
        family=MonsterFamily.DEVIL,
    )
    EVILARMOR = Species(
        id=153,
        name="EvilArmor",
        slug="evilarmor",
        family=MonsterFamily.DEVIL,
    )
    JAMIRUS = Species(
        id=154,
        name="Jamirus",
        slug="jamirus",
        family=MonsterFamily.DEVIL,
    )
    DURRAN = Species(
        id=155,
        name="Durran",
        slug="durran",
        family=MonsterFamily.DEVIL,
    )
    SPOOKY = Species(
        id=156,
        name="Spooky",
        slug="spooky",
        family=MonsterFamily.ZOMBIE,
    )
    SKULLGON = Species(
        id=157,
        name="Skullgon",
        slug="skullgon",
        family=MonsterFamily.ZOMBIE,
    )
    PUTREPUP = Species(
        id=158,
        name="Putrepup",
        slug="putrepup",
        family=MonsterFamily.ZOMBIE,
    )
    ROTRAVEN = Species(
        id=159,
        name="RotRaven",
        slug="rotraven",
        family=MonsterFamily.ZOMBIE,
    )
    MUMMY = Species(
        id=160,
        name="Mummy",
        slug="mummy",
        family=MonsterFamily.ZOMBIE,
    )
    DARKCRAB = Species(
        id=161,
        name="DarkCrab",
        slug="darkcrab",
        family=MonsterFamily.ZOMBIE,
    )
    DEADNITE = Species(
        id=162,
        name="DeadNite",
        slug="deadnite",
        family=MonsterFamily.ZOMBIE,
    )
    SHADOW = Species(
        id=163,
        name="Shadow",
        slug="shadow",
        family=MonsterFamily.ZOMBIE,
    )
    HORK = Species(
        id=164,
        name="Hork",
        slug="hork",
        family=MonsterFamily.ZOMBIE,
    )
    MUDRON = Species(
        id=165,
        name="Mudron",
        slug="mudron",
        family=MonsterFamily.ZOMBIE,
    )
    NITEWHIP = Species(
        id=166,
        name="NiteWhip",
        slug="nitewhip",
        family=MonsterFamily.ZOMBIE,
    )
    MADSPIRIT = Species(
        id=167,
        name="MadSpirit",
        slug="madspirit",
        family=MonsterFamily.ZOMBIE,
    )
    WINDMERGE = Species(
        id=168,
        name="WindMerge",
        slug="windmerge",
        family=MonsterFamily.ZOMBIE,
    )
    REAPER = Species(
        id=169,
        name="Reaper",
        slug="reaper",
        family=MonsterFamily.ZOMBIE,
    )
    DEADNOBLE = Species(
        id=170,
        name="DeadNoble",
        slug="deadnoble",
        family=MonsterFamily.ZOMBIE,
    )
    WHITEKING = Species(
        id=171,
        name="WhiteKing",
        slug="whiteking",
        family=MonsterFamily.ZOMBIE,
    )
    BONESLAVE = Species(
        id=172,
        name="BoneSlave",
        slug="boneslave",
        family=MonsterFamily.ZOMBIE,
    )
    SKELETOR = Species(
        id=173,
        name="Skeletor",
        slug="skeletor",
        family=MonsterFamily.ZOMBIE,
    )
    SERVANT = Species(
        id=174,
        name="Servant",
        slug="servant",
        family=MonsterFamily.ZOMBIE,
    )
    COPYCAT = Species(
        id=175,
        name="Copycat",
        slug="copycat",
        family=MonsterFamily.ZOMBIE,
    )
    JEWELBAG = Species(
        id=176,
        name="JewelBag",
        slug="jewelbag",
        family=MonsterFamily.MATERIAL,
    )
    EVILWAND = Species(
        id=177,
        name="EvilWand",
        slug="evilwand",
        family=MonsterFamily.MATERIAL,
    )
    MADCANDLE = Species(
        id=178,
        name="MadCandle",
        slug="madcandle",
        family=MonsterFamily.MATERIAL,
    )
    COILBIRD = Species(
        id=179,
        name="CoilBird",
        slug="coilbird",
        family=MonsterFamily.MATERIAL,
    )
    FACER = Species(
        id=180,
        name="Facer",
        slug="facer",
        family=MonsterFamily.MATERIAL,
    )
    SPIKYBOY = Species(
        id=181,
        name="SpikyBoy",
        slug="spikyboy",
        family=MonsterFamily.MATERIAL,
    )
    MADMIRROR = Species(
        id=182,
        name="MadMirror",
        slug="madmirror",
        family=MonsterFamily.MATERIAL,
    )
    ROGUENITE = Species(
        id=183,
        name="RogueNite",
        slug="roguenite",
        family=MonsterFamily.MATERIAL,
    )
    GOOPI = Species(
        id=184,
        name="Goopi",
        slug="goopi",
        family=MonsterFamily.MATERIAL,
    )
    VOODOLL = Species(
        id=185,
        name="Voodoll",
        slug="voodoll",
        family=MonsterFamily.MATERIAL,
    )
    METALDRAK = Species(
        id=186,
        name="MetalDrak",
        slug="metaldrak",
        family=MonsterFamily.MATERIAL,
    )
    BALZAK = Species(
        id=187,
        name="Balzak",
        slug="balzak",
        family=MonsterFamily.MATERIAL,
    )
    SABREMAN = Species(
        id=188,
        name="SabreMan",
        slug="sabreman",
        family=MonsterFamily.MATERIAL,
    )
    CURSELAMP = Species(
        id=189,
        name="CurseLamp",
        slug="curselamp",
        family=MonsterFamily.MATERIAL,
    )
    ROBOSTER = Species(
        id=190,
        name="Roboster",
        slug="roboster",
        family=MonsterFamily.MATERIAL,
    )
    EVILPOT = Species(
        id=191,
        name="EvilPot",
        slug="evilpot",
        family=MonsterFamily.MATERIAL,
    )
    GISMO = Species(
        id=192,
        name="Gismo",
        slug="gismo",
        family=MonsterFamily.MATERIAL,
    )
    LAVAMAN = Species(
        id=193,
        name="LavaMan",
        slug="lavaman",
        family=MonsterFamily.MATERIAL,
    )
    ICEMAN = Species(
        id=194,
        name="IceMan",
        slug="iceman",
        family=MonsterFamily.MATERIAL,
    )
    MIMIC = Species(
        id=195,
        name="Mimic",
        slug="mimic",
        family=MonsterFamily.MATERIAL,
    )
    MUDDOLL = Species(
        id=196,
        name="MudDoll",
        slug="muddoll",
        family=MonsterFamily.MATERIAL,
    )
    GOLEM = Species(
        id=197,
        name="Golem",
        slug="golem",
        family=MonsterFamily.MATERIAL,
    )
    STONEMAN = Species(
        id=198,
        name="StoneMan",
        slug="stoneman",
        family=MonsterFamily.MATERIAL,
    )
    BOMBCRAG = Species(
        id=199,
        name="BombCrag",
        slug="bombcrag",
        family=MonsterFamily.MATERIAL,
    )
    GOLDGOLEM = Species(
        id=200,
        name="GoldGolem",
        slug="goldgolem",
        family=MonsterFamily.MATERIAL,
    )
    DRACOLORD1 = Species(
        id=201,
        name="DracoLord1",
        slug="dracolord1",
        family=MonsterFamily.BOSS,
    )
    DRACOLORD2 = Species(
        id=202,
        name="DracoLord2",
        slug="dracolord2",
        family=MonsterFamily.BOSS,
    )
    HARGON = Species(
        id=203,
        name="Hargon",
        slug="hargon",
        family=MonsterFamily.BOSS,
    )
    SIDOH = Species(
        id=204,
        name="Sidoh",
        slug="sidoh",
        family=MonsterFamily.BOSS,
    )
    BARAMOS = Species(
        id=205,
        name="baramos",
        slug="baramos",
        family=MonsterFamily.BOSS,
    )
    ZOMA = Species(
        id=206,
        name="Zoma",
        slug="zoma",
        family=MonsterFamily.BOSS,
    )
    PIZZARO = Species(
        id=207,
        name="Pizzaro",
        slug="pizzaro",
        family=MonsterFamily.BOSS,
    )
    ESTERK = Species(
        id=208,
        name="Esterk",
        slug="esterk",
        family=MonsterFamily.BOSS,
    )
    MIRUDRAAS1 = Species(
        id=209,
        name="Mirudraas1",
        slug="mirudraas1",
        family=MonsterFamily.BOSS,
    )
    MIRUDRAAS2 = Species(
        id=210,
        name="Mirudraas2",
        slug="mirudraas2",
        family=MonsterFamily.BOSS,
    )
    MUDOU = Species(
        id=211,
        name="Mudou",
        slug="mudou",
        family=MonsterFamily.BOSS,
    )
    DEATHMORE1 = Species(
        id=212,
        name="DeathMore1",
        slug="deathmore1",
        family=MonsterFamily.BOSS,
    )
    DEATHMORE2 = Species(
        id=213,
        name="DeathMore2",
        slug="deathmore2",
        family=MonsterFamily.BOSS,
    )
    DEATHMORE3 = Species(
        id=214,
        name="DeathMore3",
        slug="deathmore3",
        family=MonsterFamily.BOSS,
    )
    DARKDRIUM = Species(
        id=215,
        name="DarkDrium",
        slug="darkdrium",
        family=MonsterFamily.BOSS,
    )

    @property
    def dragon_species(self) -> list[Species]:
        """Returns a list of all dragon-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.DRAGON
        ]

    @property
    def beast_species(self) -> list[Species]:
        """Returns a list of all beast-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.BEAST
        ]

    @property
    def bird_species(self) -> list[Species]:
        """Returns a list of all bird-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.BIRD
        ]

    @property
    def plant_species(self) -> list[Species]:
        """Returns a list of all plant-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.PLANT
        ]

    @property
    def bug_species(self) -> list[Species]:
        """Returns a list of all bug-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.BUG
        ]

    @property
    def devil_species(self) -> list[Species]:
        """Returns a list of all devil-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.DEVIL
        ]

    @property
    def zombie_species(self) -> list[Species]:
        """Returns a list of all zombie-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.ZOMBIE
        ]

    @property
    def material_species(self) -> list[Species]:
        """Returns a list of all material-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.MATERIAL
        ]

    @property
    def boss_species(self) -> list[Species]:
        """Returns a list of all boss-type species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == MonsterFamily.BOSS
        ]

    @property
    def all_species(self) -> list[Species]:
        """Returns a list of all species."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species)
        ]

    def get_species_by_class(self, family: MonsterFamily) -> list[Species]:
        """Return a list of species for the given monster class."""
        return [
            species
            for species in self.__class__.__dict__.values()
            if isinstance(species, Species) and species.family == family
        ]
