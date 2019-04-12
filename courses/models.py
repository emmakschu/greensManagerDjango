from django.db import models

#####################################################################
#
# GOLF COURSE FEATURES MODELS
#
# This app tracks the main geographic features of a golf course --
# the courses, holes, tees, fairway, greens, roughs, and bunkers.
# These features will be referenced by objects from many other apps,
# e.g. mowing, spraying, turfgrasses planted, etc.
#
# Everything ultimately references back to a Course instance, so
# even at a facility with only one course, it should be created as
# an instsance of the Course model.
#
#####################################################################

class Course(models.Model):
    """
    Course class

    Tracks courses at the facility. There should be at least one,
    but how the enduser chooses to make use of this class is up to
    them (e.g. for a 36-hole facility it would be fairly straight-
    forward; for a 27-hole facility, perhaps one Course instance for
    each 9 holes; for an 18-hole facility, either one Course total,
    or two Courses for front nine and back nine). 

    It's also recommended to have at least one separate Course object
    for practice facilities.

    """

    # Name as a VARCHAR(256) -- anything longer would seem excessive
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)

class Hole(models.Model):
    """
    Hole class
    
    Tracks instances of golf course holes. Belongs to a Course. It is
    strongly recommended that each Course have at least one Hole,
    even if it as abstract placeholder, as in the case of practice
    facilities. Id est, to keep track of a driving range tee, the
    Tee object (ut infra) must belong to a Hole object. Likewise for
    a practice green's Green object, etc.

    """

    # Hole number as played on the course. Can be 0 (e.g. for
    # practice facilities)
    number = models.IntegerField()
    # Some facilities like to refer to holes by nicknames
    nickname = models.CharField(max_length=256,
                                null = True,
                                blank = True)
    # Par rating of the hole. Can be 0 (e.g. for practice facilities)
    par = models.IntegerField(default = 4)
    # Yardage as printed on scorecards, or other local convention
    yardage = models.IntegerField()
    
    # Hole must belong to a Course object
    course = models.ForeignKey(Course,
                               related_name='hole',
                               on_delete=models.CASCADE)
    map = models.ImageField(blank=True,
                            null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, hole %d" % (self.course,
                                self.number)

class TurfFeature(models.Model):
    """
    TurfFeature class

    The template class for Tee, Fairway, Green, and Rough. Most of
    the items to store are identical for those features, so in
    accord with the DRY (don't repeat yourself) ethos, they will be
    subclasses of TurfFeature.

    """

    # Surface area of the tee
    area = models.IntegerField()

    # Optionally track the (primary) soil type, turf species, and
    # turf cultivar
    soil_type = models.ForeignKey('turfs.SoilType',
                                  blank = True,
                                  null = True,
                                  on_delete=models.CASCADE)
    turf_species = models.ForeignKey('turfs.TurfgrassSpecies',
                                     blank = True,
                                     null = True,
                                     on_delete=models.CASCADE)
    turf_cultivar = models.ForeignKey('turfs.Cultivar',
                                      blank = True,
                                      null = True,
                                      on_delete=models.CASCADE)

    mow_direction = models.DecimalField(decimal_places=24,
                                        max_digits=32,
                                        default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tee(TurfFeature):
    """
    Tee class

    A subclass of the TurfFeature class. Must belong to a Hole
    instance.

    """

    hole = models.ForeignKey(Hole,
                             related_name='tee',
                             on_delete=models.CASCADE)
    notes = models.CharField(max_length=256)

    def __str__(self):
        return "%s %s" % (self.hole,
                          self.notes)

class Fairway(TurfFeature):
    """
    Fairway class

    A subclass of the TurfFeature class. Must belong to a Hole
    instance.

    """

    hole = models.ForeignKey(Hole,
                             related_name='fairway',
                             on_delete=models.CASCADE)

    def __str__(self):
        return "%s fairway" % (self.hole)

class Green(TurfFeature):
    """
    Green class

    A subclass of the TurfFeature class. Must belong to a Hole
    instance.

    """

    hole = models.ForeignKey(Hole,
                             related_name='green',
                             on_delete=models.CASCADE)
    map = models.ImageField(blank=True,
                            null=True)

    def __str__(self):
        return "%s green" % (self.hole)

class Rough(TurfFeature):
    """
    Rough class

    A subclass of the TurfFeature class. Must belong to a Hole
    instance.
    
    """

    hole = models.ForeignKey(Hole,
                             related_name='rough',
                             on_delete=models.CASCADE)

    def __str__(self):
        return "%s rough" % (self.hole)

class BunkerLocation(models.Model):
    """
    BunkerLocation class

    Used to standardize descriptions of bunker locations. Endusers
    can use whatever names are meaningful to them, e.g. "left
    fairway 1" for the first fairway bunker on the left.

    """
    name = models.CharField(max_length=256)

    def __str__(self):
        return "%s" % (self.name)

class Bunker(models.Model):
    """
    Bunker class

    Keeps track of bunkers/sand traps. Must belong to an instance of
    the Hole class, and an instance of the BunkerLocation class.

    """
    hole = models.ForeignKey(Hole,
                             related_name='bunker',
                             on_delete=models.CASCADE)
    bunker_location = models.ForeignKey(BunkerLocation,
                                        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s bunker" % (self.hole, self.bunker_location)
