from django.db import models

####################################################################
#
# GOLF COURSE MACHINES MODELS
# 
# Used to track machines used for turfgrass management, such as 
# mowers, carts, sprayers, utility vehicles, etc.
#
# Will be referenced frequently by other apps, e.g. which mower was
# used for this mowing instance, which machines is this oil filter
# used for, which machine was this repair on, etc.
#
# Each machine has an `in_commission` field which defaults to True,
# but can be be flagged False by mechanical staff when maintenance
# or repairs are needed. Instances marked False will show up on the
# facility's homepage to ensure superintendants know the status.
# 
####################################################################

class Machine(models.Model):
    """
    Machine class

    A superclass used by all different types of turf management
    machines.
    """

    # Machine must have a make (manufacturer)
    make = models.CharField(max_length=128)
    # Machine must have a model name
    model = models.TextField(max_length=256)
    # Machine must have a year (model year, or year of production)
    year = models.IntegerField()

    serial = models.CharField(max_length=128,
                              blank=True,
                              null=True)

    # Often facilities have multiple machines of the same type which
    # are identified by an alphanumeric tag/sticker. Can be blank if
    # not applicable
    ident_number = models.CharField(max_length=16,
                                    blank = True,
                                    null = True)
    # Date the machine was purchased/acquired
    date_purchased = models.DateField()
    purchase_price = models.DecimalField(decimal_places=2,
                                         max_digits=16,
                                         blank=True,
                                         null=True)
    # Hours on the machine. Not automatically updated, of course, so
    # should be updated at regular intervals by relevant staff
    hours = models.FloatField()

    # Is the machine in or out of commission? Flagged false by the
    # mechanical staff in the maintenance app
    in_commission = models.BooleanField(default = True)
    fuel_type = models.ManyToManyField('parts.Fuel', 
                                       blank = True,
                                       related_name = 'machine_fuel')


    # Mechanics/Supers can optionally set the fluids and filters 
    # used on a machine so that lower level staff can maintain them
    # without having to seek a mechanic. E.g. a greenskeeper can 
    # notice that the oil is a bit low on a particular mower, find
    # it on the app, and be sure to add the correct type before
    # going out on the course to mow.
    oil_type = models.ManyToManyField('parts.Oil', 
                                      blank = True,
                                      related_name = 'machine_oil')
    oil_capacity = models.FloatField(blank = True, null = True)
    oil_units = models.ForeignKey('measures.VolumeUnit', blank=True,
                                  null=True,
                                  related_name="mach_oil_units")
    hyd_oil_type = models.ManyToManyField('parts.Oil', 
                                          blank = True,
                                          related_name = 'mach_hyd_oil')
    hyd_oil_capacity = models.FloatField(blank = True, null = True)
    hyd_oil_units = models.ForeignKey('measures.VolumeUnit',
                                      blank=True,
                                      null=True,
                                      related_name="mach_hyd_unit")
    oil_filter = models.ManyToManyField('parts.Filter', 
                                        blank = True,
                                        related_name = 'mach_oil_filter')
    hyd_oil_filter = models.ManyToManyField('parts.Filter', 
                                            blank = True,
                                            related_name = 'mach_hyd_oil_filter')
    fuel_filter = models.ManyToManyField('parts.Filter', 
                                         blank = True,
                                         related_name = 'mach_fuel_filter')
    air_filter = models.ManyToManyField('parts.Filter',
                                        blank=True,
                                        related_name='mach_air_filter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.ident_number != None:
            return "%s %s" % (self.model, self.ident_number)
        else:
            return "%s %s" % (self.make, self.model)
    
class Mower(Machine):
    """
    Mower class

    A subclass of Machine, and a superclass of the various types of
    mower (greens, tee, fairway, rough). Identical to the Machine
    model except for the cut_height field.

    Its subclasses are all identical, separated only for primary
    function, which is usually a very important distinction for
    monitoring golf course equipment
    """

    # Cut height of the mower. Can be in whatever units are 
    # preferred, but MUST BE IN DECIMAL FORMAT (e.g. 0.125 instead
    # of 1/8 inch).
    cut_height = models.FloatField()
    height_units = models.ForeignKey('measures.DistanceUnit',
                                     blank=True,
                                     null=True,
                                     related_name="height_unit")

class GreensMower(Mower):
    """
    GreensMower class

    A subclass of Machine->Mower. Tracks machines typically used to
    mow greens.
    """

class TeeMower(Mower):
    """
    TeeMower class

    A subclass of Machine->Mower. Tracks machines typically used to
    mow tees.
    """

class FairwayMower(Mower):
    """
    FairwayMower class

    A subclass of Machine->Mower. Tracks machines typically used to
    mow fairways.
    """
    
class RoughMower(Mower):
    """
    RoughMower class

    A subclass of Machine->Mower. Tracks machines typically used to
    mow roughs.
    """
class Roller(Machine):
    """
    Roller class

    A subclass of Machine. Tracks machines used to roll greens,
    tees, fairways, etc
    """

    # Roll width of the machine. OPTIONAL. Primarily for the case
    # when facilities have both the single roller and newer-gen
    # triple-rollers on hand
    roll_width = models.FloatField(blank = True, null = True)
    width_units = models.ForeignKey('measures.DistanceUnit',
                                    blank=True,
                                    null=True,
                                    related_name="width_unit")

class Aerator(Machine):
    """
    Aerator class

    A subclass of Machine. Tracks machines used for aerating/
    quadra-tining/etc. 
    """

class Sprayer(Machine):
    """
    Sprayer class

    A subclass of Machine. Tracks machines used to spray chemicals. 
    """

    # Tank capacity can be in units of your choosing, but they must
    # be consistent with those used in the Spraying app in order to
    # have accurate calculations
    tank_capacity = models.IntegerField()
    tank_units = models.ForeignKey('measures.VolumeUnit',
                                   blank=True,
                                   null=True,
                                   related_name="tank_unit")

class Cart(Machine):
    """
    Cart class

    A subclass of Machine 
    """

class TrapRake(Machine):
    """
    TrapRake class

    A subclass of Machine. Tracks machines that are primarily used
    for raking sand traps.
    """

    # Plow field indicates if a plow is available (i.e. in the
    # shop) for the machine.
    plow = models.BooleanField()

    # Plow_attached indicates whether an optional plow is currently
    # attached
    plow_attached = models.BooleanField(default=False)

class UtilVehicle(Machine):
    """
    UtilVehicle

    A subclass of Machine. Tracks utility vehicles, meant to 
    transport people, small, or medium size loads.
    """

    # Bed size in preferred cubic units
    bed_size = models.FloatField(blank = True, null = True)
    bed_units = models.ForeignKey('measures.Unit',
                                  blank=True,
                                  null=True,
                                  related_name="bed_unit")

class Tractor(Machine):
    """
    Tractor class

    A subclass of Machine
    Used to track compact to medium-size utility/agricultural 
    tractors.
    """

class FertSpreader(models.Model):
    """
    Class FertSpreader

    Tracks machines used to spread fertilizer, whether man-powered
    or tractor-powered
    """

    # Make of the machine
    make = models.CharField(max_length = 128)
    model = models.CharField(max_length = 256,
                             blank = True,
                             null = True)
    # ID number if used
    ident_number = models.CharField(max_length = 16,
                                    blank = True,
                                    null = True)
    
    date_purchased = models.DateField()
    in_commission = models.BooleanField(default=True)
    
    # Capacity, in preferred local units. Should conform to units
    # used in the Fertilizing app
    capacity = models.FloatField(blank=True, null=True)
    units = models.ForeignKey('measures.Unit',
                              blank=True,
                              null=True,
                              related_name="cap_unit")
    # Notes, e.g.: "Should be set to H for tees", etc.
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s %s spreader" % (self.make, self.ident_number)

class Truck(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    mileage = models.FloatField()
    # Date the machine was purchased/acquired
    date_purchased = models.DateField()
    purchase_price = models.DecimalField(decimal_places=2,
                                         max_digits=16,
                                         blank=True,
                                         null=True)
    serial = models.CharField(max_length=128,
                              blank=True,
                              null=True)
    fuel_type = models.ManyToManyField('parts.Fuel', 
                                       blank = True,
                                       related_name = 'truck_fuel')


    # Mechanics/Supers can optionally set the fluids and filters 
    # used on a machine so that lower level staff can maintain them
    # without having to seek a mechanic. E.g. a greenskeeper can 
    # notice that the oil is a bit low on a particular mower, find
    # it on the app, and be sure to add the correct type before
    # going out on the course to mow.
    oil_type = models.ManyToManyField('parts.Oil', 
                                      blank = True,
                                      related_name = 'truck_oil')
    oil_capacity = models.FloatField(blank = True, null = True)
    oil_units = models.ForeignKey('measures.VolumeUnit',
                                  blank=True,
                                  null=True,
                                  related_name="truck_oil_unit")
    hyd_oil_type = models.ManyToManyField('parts.Oil', 
                                          blank = True,
                                          related_name = 'truck_hyd')
    hyd_oil_capacity = models.FloatField(blank = True, null = True)
    hyd_oil_units = models.ForeignKey('measures.VolumeUnit',
                                      blank=True,
                                      null=True,
                                      related_name="truck_hyd_unit")
    oil_filter = models.ManyToManyField('parts.Filter', 
                                        blank = True,
                                        related_name = 'truck_oil_filter')
    hyd_oil_filter = models.ManyToManyField('parts.Filter', 
                                            blank = True,
                                            related_name = 'truck_hyd_filter')
    fuel_filter = models.ManyToManyField('parts.Filter', 
                                         blank = True,
                                         related_name = 'truck_fuel_filter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HourReading(models.Model):
    """
    Class HourReading

    Keeps track of regular readings of hour meters
    """

    machine = models.ForeignKey(Machine)
    hours = models.FloatField()
    date = models.DateField(auto_now=True)
    notes = models.TextField(blank=True, null=True)


