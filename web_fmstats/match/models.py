from django.db import models


class Team(models.Model):
    team_name = models.CharField(
        'Название команды'
    )
    team_emblem = models.ImageField(
        'Эмблемма команды',
        blank=True
    )


class Match(models.Model):
    your_team = models.CharField( # Подвязать с моделью Team
        'Твоя команда'
    )
    enemy_team = models.CharField(
        'Команда противника'
    )
    match_date = models.DateField(
        'Дата сыгранного матча'
    )
    your_shots = models.ImageField(
        'Твои удары по воротам противника'
    )
    enemy_shots = models.ImageField(
        'Удары противника'
    )
    your_goals = models.ImageField(
        'Твои голы'
    )
    enemy_goals = models.ImageField(
        'Вражеские голы'
    )
    your_shots_on_target = models.ImageField(
        'Твои удары в створ'
    )
    enemy_shots_on_target = models.ImageField(
        'Вражеские удары в створ противника'
    )
    your_xg = models.FloatField(
        'Твой xG'
    )
    enemy_xg = models.FloatField(
        'Вражеский xG'
    )
    your_angular = models.ImageField(
        'Твои угловые'
    )
    enemy_angular = models.ImageField(
        'Вражеские угловые'
    )
