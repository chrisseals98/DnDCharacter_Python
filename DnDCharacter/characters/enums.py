# enums.py

from enum import Enum

class Race(Enum):
    DWARF = 'Dwarf'
    ELF = 'Elf'
    HALFLING = 'Halfling'
    HUMAN = 'Human'
    DRAGONBORN = 'Dragonborn'
    GNOME = 'Gnome'
    HALF_ELF = 'Half-Elf'
    HALF_ORC = 'Half-Orc'
    TIEFLING = 'Tiefling'

class CharacterClass(Enum):
    BARBARIAN = 'Barbarian'
    BARD = 'Bard'
    CLERIC = 'Cleric'
    DRUID = 'Druid'
    FIGHTER = 'Fighter'
    MONK = 'Monk'
    PALADIN = 'Paladin'
    RANGER = 'Ranger'
    SORCERER = 'Sorcerer'
    WARLOCK = 'Warlock'
    WIZARD = 'Wizard'

class Alignment(Enum):
    TRUE_NEUTRAL = 'True Neutral'
    LAWFUL_NEUTRAL = 'Lawful Neutral'
    CHAOTIC_NEUTRAL = 'Chaotic Neutral'
    NEUTRAL_GOOD = 'Neutral Good'
    LAWFUL_GOOD = 'Lawful Good'
    CHAOTIC_GOOD = 'Chaotic Good'
    NEUTRAL_EVIL = 'Neutral Evil'
    LAWFUL_EVIL = 'Lawful Evil'
    CHAOTIC_EVIL = 'Chaotic Evil'
