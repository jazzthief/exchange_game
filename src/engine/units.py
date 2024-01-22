from enum import StrEnum
from logging import getLogger

# TODO: create higher level logger & share config
logger = getLogger(__name__)


class AttackType(StrEnum):
    PHYSICAL = "PHYSICAL"
    BLAST = "BLAST"
    FIRE = "FIRE"
    CHEMICAL = "CHEMICAL"
    ARCANE = "ARCANE"


class Unit:
    def __init__(
        self,
        name: str,
        health: int,
        armor: int,
        resistance: int,
        attack_dmg: int,
        attack_range: int,
        initiative: int,
        attack_type: AttackType = AttackType.PHYSICAL,
        attack_targets: int = 1,
        prefix: str | None = None,
    ) -> None:
        # TODO: active abilities
        self.name = name
        self.health = health
        self.armor = armor
        self.resistance = resistance
        self.attack_dmg = attack_dmg
        self.attack_type = attack_type
        self.attack_range = attack_range
        self.attack_targets = attack_targets
        self.initiative = initiative
        self.prefix = prefix

        logger.info(f"Created {__class__.__name__} {self.name}")

    def attack(self):
        pass


class Hero(Unit):
    def __init__(
        self,
        name: str,
        health: int,
        armor: int,
        resistance: int,
        attack_dmg: int,
        attack_range: int,
        initiative: int,
        attack_type: AttackType = AttackType.PHYSICAL,
        attack_targets: int = 1,
        prefix: str | None = None,
        level: int = 1,
    ) -> None:
        # TODO: inventory
        self.level = level

        super().__init__(
            name=name,
            health=health,
            armor=armor,
            resistance=resistance,
            attack_dmg=attack_dmg,
            attack_type=attack_type,
            attack_range=attack_range,
            attack_targets=attack_targets,
            initiative=initiative,
            prefix=prefix,
        )
