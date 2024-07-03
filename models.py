import constants

class Base:
    """Base model"""
    id: int
class User(Base):
    """User of the app."""
    name: str
    email: str
    password: str

class Monster(Base):
    """Real monsters in the game. Monsters become "real" if a user catches them or if they are the catchable boss of a travelers gate."""
    category: MonsterSpecies # reverse relationship monsters
    gate: Gate | None # Only pertinent to gate bosses
    user: User | None # reverse relationship owner
    name: str | None 
    level: int | None
    breeding_level: int | None
    breeding_plan: BreedingPlan # reverse relationship monsters
    health_points: int | None
    mana_points: int | None
    attack: int | None
    defense: int | None
    agility: int | None
    defense: int | None
    intelligence: int | None
    wild: int | None
    
    
class MonsterSpecies(Base):
    """Monster species."""
    name: str
    slug: str
    monster_class: constants.MonsterClasses

class Skill(Base):
    """The details and effect of a special attack."""
    name: str
    base: Skill # reverse relationship higher_levels
    level: int # default 1, not all skills have levels
    description: str
    damage_type: constants.DamageTypes
    combined: bool


class SkillStatRequirement(Base):
    """A stat requirement that a monster must have before it can learn a skill."""
    skill: Skill
    stat: constants.StatTypes
    level: int


class SpeciesSkill(Base):
    """A special attack automatically learned by a species at a level."""
    monster_species: MonsterSpecies
    skill: Skill


class Gate(Base):
    """A travelers gate through which monsters can be fought and collected."""
    name: str
    levels: int
    location: str
    boss: Monster

class MonsterGateMembership(Base):
    """Gates and levels in which a particular monster species can be caught in the wild."""
    monster: Monster
    gate: Gate
    levels: str # list of levels the monster appears on in this gate

class BreedingPlan(Base):
    """A plan with a target monster species for users to assign their monsters to."""
    target: Monster
    target_level: int | None
    def get_shortest_path(self):
        """From a user's current set of monsters, assigned or unassigned, get the shortest combination of monsters required to achieve it."""
        # This algorithm is going to be somethin else

class BreedingStep(Base):
    """A breeding pair necessary to achieve a breeding plan."""
    male: Monster # reverse relationship breeding_steps
    female: Monster # reverse relationship breeding_steps
    pedigree: constants.MonsterGenders
    breeding_plan: BreedingPlan # reverse relationship breeding_steps

    @property
    def pedigree_id(self):
        return self.female_id if self.pedigree == constants.MonsterGenders.FEMALE else self.male_id


