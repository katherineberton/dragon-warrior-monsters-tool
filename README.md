Here's my plan for the db models when I implement them eventually.


--------------------------------For the breeding module:--------------------------------

class BreedingPlan(base_models.BaseModel):
    """A plan with a target monster species for users to assign their monsters to."""

    target: Species
    target_level: int | None


class BreedingEvent(base_models.BaseModel):
    """A breeding pair initiated to achieve a breeding plan."""

    male: Monster # An actual owned monster
    female: Monster # An actual owned monster
    pedigree: constants.MonsterGenders (male or female)
    breeding_plan: BreedingPlan


--------------------------------For the monsters module:--------------------------------

class Monster(base_models.BaseModel):
    """Real monsters in the game. Monsters become "real" if a user catches them or if they are the catchable boss of a travelers gate."""

    species: Species
    name: str | None
    gender: constants.MonsterGenders
    level: int | None
    breeding_level: int | None # How long of a chain of breeding it took to get this monster
    stats: MonsterStat
    boss_of_gate: TravelersGate | None

class MonsterStat(base_models.BaseModel):
    max_health_points: int
    max_mana_points: int
    attack: int
    defense: int
    agility: int
    intelligence: int
    wild: int

