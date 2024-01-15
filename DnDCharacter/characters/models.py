from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .enums import Race, CharacterClass, Alignment

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=50, choices=[(val.value, val.name) for val in Race], default=Race.HUMAN.value)
    character_class = models.CharField(max_length=50, choices=[(val.value, val.name) for val in CharacterClass], default=CharacterClass.BARBARIAN.value)    
    strength = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dexterity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    constitution = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    intelligence = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    alignment = models.CharField(max_length=50, choices=[(val.value, val.name) for val in Alignment], default=Alignment.TRUE_NEUTRAL.value)
    inventory = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name