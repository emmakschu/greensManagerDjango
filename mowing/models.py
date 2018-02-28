from django.db import models
from datetime import date
from django.utils import timezone

####################################################################
#
# MOWING MODELS
#
# The mowing models track instances of mowing greens, tees, fairways,
# and roughs. Each instance should belong to a particular course
# area (Tee/Fairway/Green/Rough), and a particular mower 
# (TeeMower, FairwayMower, GreensMower, or RoughMower).
#
####################################################################

class Mowing(models.Model):
    """
    Mowing class

    The parent class for all mowing instances. The only thing
    common to all is the datetime, all else is in the subclasses
    """

    # When the mowing occurred. Defaults to current time. Can of
    # course be as exact or approximate as desired.
    mow_date = models.DateTimeField(default=timezone.now)

class GreensMowing(Mowing):
    """
    GreensMowing class

    A subclass of Mowing. Tracks when greens were mowed, on a 
    many-to-many basis.

    Different mowers means a different mowing session, so any
    potential problems with mowers can be tracked.
    """

    # Select one or more greens that were mowed in this session
    green = models.ManyToManyField('courses.Green')
    # Mower used
    mower = models.ManyToManyField('machines.GreensMower')

class TeeMowing(Mowing):
    """
    TeeMowing class

    A subclass of Mowing. Tracks when tees were mowed, on a 
    many-to-many basis

    Different mowers means a different mowing session, so any
    potential problems with mowers can be tracked.
    """

    # Select one or more tees that were mowed in this session
    tee = models.ManyToManyField('courses.Tee')
    # Mower was used
    mower = models.ManyToManyField('machines.TeeMower')

class FairwayMowing(Mowing):
    """
    FairwayMowing class

    A subclass of Mowing. Tracks when fairways were mowed, on a 
    many-to-many basis

    Different mowers means a different mowing session, so any
    potential problems with mowers can be tracked.
    """
    fairway = models.ManyToManyField('courses.Fairway')
    mower = models.ManyToManyField('machines.FairwayMower')

class RoughMowing(Mowing):
    """
    RoughMowing class

    A subclass of Mowing. Tracks when roughs were mowed, on a 
    many-to-many basis

    Different mowers means a different mowing session, so any
    potential problems with mowers can be tracked. Mightn not be as 
    strict as with greens,tees,and fairways.
    """
    rough = models.ManyToManyField('courses.Rough')
    mower = models.ManyToManyField('machines.RoughMower')
