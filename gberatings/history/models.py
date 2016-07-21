# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Confindex(models.Model):
    confname = models.CharField(db_column='confName', max_length=128)  # Field name made lowercase.
    confabbv = models.CharField(db_column='confAbbv', max_length=16)  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confIndex'


class Confindex2010(models.Model):
    confname = models.CharField(db_column='confName', max_length=128)  # Field name made lowercase.
    confabbv = models.CharField(db_column='confAbbv', max_length=16)  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confIndex2010'


class Confindex2012(models.Model):
    confname = models.CharField(db_column='confName', max_length=128)  # Field name made lowercase.
    confabbv = models.CharField(db_column='confAbbv', max_length=16)  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confIndex2012'


class Ratingsindex(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    seasoncurrent = models.IntegerField(db_column='seasonCurrent')  # Field name made lowercase.
    weekcurrent = models.CharField(db_column='weekCurrent', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ratingsIndex'


class Season0000(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season0000'


class Season2003(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2003'


class Season2004(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2004'


class Season2005(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(max_digits=10, decimal_places=8)
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2005'


class Season2006(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2006'


class Season2007(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2007'


class Season2008(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2008'


class Season2009(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2009'


class Season2010(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2010'


class Season2011(models.Model):
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2011'


class Season2012(models.Model):
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2012'


class Season2013(models.Model):
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2013'


class Season2014(models.Model):
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2014'


class Season2015(models.Model):
    team = models.CharField(max_length=64)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    conf = models.CharField(max_length=16)
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    week1rating = models.DecimalField(db_column='week1Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week1rank = models.CharField(db_column='week1Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week2rating = models.DecimalField(db_column='week2Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2rank = models.CharField(db_column='week2Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week3rating = models.DecimalField(db_column='week3Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3rank = models.CharField(db_column='week3Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week4rating = models.DecimalField(db_column='week4Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4rank = models.CharField(db_column='week4Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week5rating = models.DecimalField(db_column='week5Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5rank = models.CharField(db_column='week5Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week6rating = models.DecimalField(db_column='week6Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6rank = models.CharField(db_column='week6Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week7rating = models.DecimalField(db_column='week7Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7rank = models.CharField(db_column='week7Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week8rating = models.DecimalField(db_column='week8Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8rank = models.CharField(db_column='week8Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week9rating = models.DecimalField(db_column='week9Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9rank = models.CharField(db_column='week9Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week10rating = models.DecimalField(db_column='week10Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10rank = models.CharField(db_column='week10Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week11rating = models.DecimalField(db_column='week11Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11rank = models.CharField(db_column='week11Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week12rating = models.DecimalField(db_column='week12Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12rank = models.CharField(db_column='week12Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week13rating = models.DecimalField(db_column='week13Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13rank = models.CharField(db_column='week13Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week14rating = models.DecimalField(db_column='week14Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14rank = models.CharField(db_column='week14Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week15rating = models.DecimalField(db_column='week15Rating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15rank = models.CharField(db_column='week15Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weekfinalrating = models.DecimalField(db_column='weekFinalRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalrank = models.CharField(db_column='weekFinalRank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    week1sos = models.DecimalField(db_column='week1Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week2sos = models.DecimalField(db_column='week2Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week3sos = models.DecimalField(db_column='week3Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week4sos = models.DecimalField(db_column='week4Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week5sos = models.DecimalField(db_column='week5Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week6sos = models.DecimalField(db_column='week6Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week7sos = models.DecimalField(db_column='week7Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week8sos = models.DecimalField(db_column='week8Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week9sos = models.DecimalField(db_column='week9Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week10sos = models.DecimalField(db_column='week10Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week11sos = models.DecimalField(db_column='week11Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week12sos = models.DecimalField(db_column='week12Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week13sos = models.DecimalField(db_column='week13Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week14sos = models.DecimalField(db_column='week14Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    week15sos = models.DecimalField(db_column='week15Sos', max_digits=10, decimal_places=8)  # Field name made lowercase.
    weekfinalsos = models.DecimalField(db_column='weekFinalSos', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2015'


class Seasonindex(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    season = models.CharField(unique=True, max_length=4)
    weekstart = models.IntegerField(db_column='weekStart')  # Field name made lowercase.
    champ = models.CharField(max_length=128)
    champid = models.IntegerField(db_column='champId')  # Field name made lowercase.
    lastweekplayed = models.IntegerField(db_column='lastWeekPlayed')  # Field name made lowercase.
    finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seasonIndex'


class Teamindex(models.Model):
    teamname = models.CharField(db_column='teamName', unique=True, max_length=64)  # Field name made lowercase.
    teammascot = models.CharField(db_column='teamMascot', max_length=256)  # Field name made lowercase.
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamIndex'


class Teamindex2010(models.Model):
    teamname = models.CharField(db_column='teamName', unique=True, max_length=64)  # Field name made lowercase.
    teammascot = models.CharField(db_column='teamMascot', max_length=256)  # Field name made lowercase.
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teamIndex2010'


class Teamindex2012(models.Model):
    teamname = models.CharField(db_column='teamName', unique=True, max_length=64)  # Field name made lowercase.
    teammascot = models.CharField(db_column='teamMascot', max_length=256)  # Field name made lowercase.
    confid = models.IntegerField(db_column='confId')  # Field name made lowercase.
    currentrating = models.DecimalField(db_column='currentRating', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teamIndex2012'


class Top40(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    year = models.CharField(max_length=8)
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    score = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'top40'
