from django.db import models
from datetime import date


####################################################################
#
# IRRIGATION SYSTEM MODELS
#
# The irrigation system is often a source of concerns at golf
# courses. A fountain sprouting up in the middle of a fairway due to
# a faulty irrigation system element is a nightmare of most course
# superintendants. Hence, tracking them is good. All pieces of the 
# irrigation system (boxes, sprinklers, drains, valves, couplers) 
# should include GPS info so they are easy to find when an emergency 
# situation arises.
#
# All items will also have a `problem` Boolean field which defaults
# to False. When flagged True, it will show up on the GreensManager
# homepage for the facility to ensure management is aware of the
# problem. A problem could indicate a leaking area, an electrical
# issue, or perhaps just a poorly-drained area noted by a
# less-experienced crew member that is better investigated than 
# ignored.
#
####################################################################


class SatelliteBox(models.Model):
    """
    SatelliteBox class

    Tracks instances of what are commonly called satellite boxes,
    which are hardwired to a set of sprinklers, and are contacted via
    electromagnetic wave signals (analog or digital) to turn the 
    sprinklers under its control on or off.

    """

    class Meta:
        # Specify plural form of name since 'es', not just 's'
        verbose_name_plural = 'Satellite boxes'

    # Indicate box number as referenced by radio system
    box_number = models.IntegerField()

    # Indicate latitude and longitude to easily find the box, and
    # possibly for inserting into a GIS program. Should use the
    # decimal format of lat and long (e.g. 43.01226), not the
    # minutes and seconds. 
    latitude = models.FloatField()
    longitude = models.FloatField()

    problem = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "box %d" % (self.box_number)

class SprinklerHead(models.Model):
    """
    SprinklerHead class

    Tracks instances of sprinkler heads. Usually they are designed
    to irrigate a specific area (e.g. a tee, a green, a fairway),
    so they can belong to an instance of a golf course area.

    """

    # Indicate sprinkler number in box as referenced by radio system.
    sprinkler_number = models.IntegerField()
    
    make = models.CharField(max_length=256,
                            blank=True,
                            null=True)
    model = models.CharField(max_length=256,
                             blank=True,
                             null=True)

    # Latitude and longitude in decimal format. See note for lat and
    # long for SatelliteBox class ut supra.
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Some (fairway) sprinkler heads have a note on the distance to
    # green on them. Can be omitted.
    distance = models.IntegerField(blank = True, null = True)
    satellite_box = models.ForeignKey(SatelliteBox)

    ###
    # Can belong to a tee, fairway, green, rough, or none. The area
    # that the sprinkler is intended to cover should be noted, for
    # best reference.
    ###
    hole = models.ForeignKey('courses.Hole',
                             blank = True,
                             null = True)
    tee = models.ForeignKey('courses.Tee',
                            blank = True,
                            null = True)
    fairway = models.ForeignKey('courses.Fairway',
                                blank = True,
                                null = True)
    green = models.ForeignKey('courses.Green',
                              blank = True,
                              null = True)
    rough = models.ForeignKey('courses.Rough',
                              blank = True,
                              null = True)

    problem = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.tee:
            return "%s sprinkler" % (self.tee)
        elif self.fairway:
            return "%s sprinkler" % (self.fairway)
        elif self.green:
            return "%s sprinkler" % (self.green)
        elif self.rough:
            return "%s sprinkler" % (self.rough)
        else:
            return "sprinkler on %s" % (self.satellite_box)

class QuickCoupler(models.Model):
    """
    QuickCoupler class

    Tracks what are commonly  called 'quick couplers', couplers in
    the irrigation system where an external sprinkler or hose can be
    temporarily fitted into the system, whether to cover an area 
    where a sprinkler head is broken, or an area where the sprinklers
    do not usually reach.

    """

    # Indicate latitude and longitude in decimal form. See note on
    # lat and long for SatelliteBox class ut supra.
    latitude = models.FloatField()
    longitude = models.FloatField()

    ###
    # Can belong to a tee, fairway, green, rough, or none. The area
    # that the QC is intended to cover should be noted. Obviously 
    # this is not a strict rule, since often a hose will connect to
    # a QC to irrigate an area some distance from the coupler itself.
    ###
    tee = models.ForeignKey('courses.Tee',
                            blank = True,
                            null = True)
    fairway = models.ForeignKey('courses.Fairway',
                                blank = True,
                                null = True)
    green = models.ForeignKey('courses.Green',
                              blank = True,
                              null = True)
    rough = models.ForeignKey('courses.Rough',
                              blank = True,
                              null = True)

    problem = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Drain(models.Model):
    """
    Drain class

    Drains are intended to drain water out of the irrigaation system,
    either because there is a problem, or to close the system down
    for the winter. They are frequently attached to a hole, or
    sometimes more specifically to a green, tee, or fairway, hence
    the ability to attach them to an instance of one of those 
    classes.

    """

    # Whether the drain is open. Defaults to closed
    open = models.BooleanField(default = False)

    ###
    # Indicate latitude and longitude. These fields are probably more
    # important here than for any other irrigation Class, since
    # drains can sometimes be very difficult to find. As usual, 
    # should be in decimal format, cf SatelliteBox class ut supra.
    ###
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Hole should indicate which hole the drain is closest to. Even
    # if not explicitly along a fairway/tee/etc., there is usually
    # some convention of what is being drained.
    hole = models.ForeignKey('courses.Hole')

    problem = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShutoffValve(models.Model):
    """
    ShutoffValve class

    Shutoff valves are often one of the most important parts of an
    irrigation system, particularly in emergency circumstances. 
    
    """

    # Status indicates whether the valve is open or closed. A value
    # of True ineicates open, thus the areas that it is capable of 
    # shutting off ARE receiving water pressure. A value of False
    # indicates that the areas it covers should *not* be receiving
    # water pressure
    open = models.BooleanField()

    ###
    # Indicate latitude and longitude. As with drains, these fields
    # are important, since valves can often become overgrown and
    # difficult to find. Should be in decimal format.
    ###
    latitude = models.FloatField()
    longitude = models.FloatField()

    ###
    # Tee, fairway, green, or rough should indicate the area whose
    # irrigation is intended to be shut off by the valve.
    ###
    tee = models.ForeignKey('courses.Tee',
                            blank = True,
                            null = True)
    fairway = models.ForeignKey('courses.Fairway',
                                blank = True,
                                null = True)
    green = models.ForeignKey('courses.Green',
                              blank = True,
                              null = True)
    rough = models.ForeignKey('courses.Rough',
                              blank = True,
                              null = True)

    problem = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IrrigationDig(models.Model):
    """
    IrrigationDig class
     
    Keeps track of any digs/repairs on the irrigation system.
    Scale does not matter -- i.e. whether a tractor-driven excavator,
    or 10 workers with shovels, or a simple flick of a switch, 
    anything that fixes an irrigation system problem should fall 
    under this realm for future reference.
    """
    date = models.DateField(default=date.today)
    sprinkler = models.ForeignKey(SprinklerHead,
                                  blank = True,
                                  null = True)
    quick_coupler = models.ForeignKey(QuickCoupler)
    drain = models.ForeignKey(Drain)
    fixed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

