from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Set'),
)

TEAM_CHOICES = (
    ('NS', 'None'),
    ('Albania','Alb'),
    ('Austria','Aus'),
    ('Belgium','Bel'),
    ('Croatia','Cro'),
    ('Czech Republic','Czech'),
    ('England','Eng'),
    ('France', 'Fra'),
    ('Germany', 'Ger'),
    ('Hungary', 'Hun'),
    ('Iceland', 'Ice'),
    ('Italy', 'Ita'),
    ('Northern Ireland', 'NIre'),
    ('Poland', 'Pol'),
    ('Portugal', 'Por'),
    ('Republic of Ireland', 'RIre'),
    ('Romania', 'Rom'),
    ('Russia', 'Russ'),
    ('Slovakia', 'Slov'),
    ('Spain', 'Spa'),
    ('Sweden', 'Swe'),
    ('Switzerland', 'Swi'),
    ('Turkey', 'Tur'),
    ('Ukraine', 'Ukr'),
    ('Wales', 'Wal'),
)

class CustomUser(AbstractUser):
    fav_team = models.CharField(max_length = 100, choices = TEAM_CHOICES, default = TEAM_CHOICES[0][0])

    class Meta:
        unique_together = ('email',)
        verbose_name = 'User'
