from django.db import models

#####################################################################
#
# FERTILIZER MODELS
#
# Used to track types of fertilizer (by manufacturer as well as
# N-P-K values, as well as the act of fertilizing different areas of
# the golf course.
#
#####################################################################

class Fertilizer(models.Model):
    """
    Fertilizer class

    Used to store fertilizer types. Can have separate instances for
    the same N-P-K value, providing they are from different
    manufacturers.

    """

    # Manufacturer (or, distributor purchased from)
    manufacturer = models.CharField(max_length = 128)
    # Name (if not applicable, could be used for organizing, e.g.
    # "midsummer greens fert")
    name = models.CharField(max_length = 256,
                            null = True,
                            blank = True)

    # N-P-K values, as is industry standard for identifying fert
    n_value = models.PositiveIntegerField()
    p_value = models.PositiveIntegerField()
    k_value = models.PositiveIntegerField()

    # Bag size. Can use any units, but should have a consistent
    # standard for the facility (or, price per container for 
    # liquid fertilizers)
    bag_size = models.PositiveIntegerField()
    # Price paid per bag/container
    price_per_bag = models.DecimalField(decimal_places = 2,
                                        max_digits = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %d-%d-%d" % (self.manufacturer,
                                self.n_value,
                                self.p_value,
                                self.k_value)

class Fertilizing(models.Model):
    """
    Fertilizing class

    A superclass used for tracking fertilization applications of
    greens, tees, fairways, or roughs. Not used directly in the app
    data
    """

    # Datetime fertilizer was applied
    fert_date = models.DateTimeField(auto_now = True)

    # Fertilizer used; refs an instance of the Fertilizer class
    fertilizer = models.ForeignKey(Fertilizer)

    # Amount of bags/containers used
    bags_used = models.DecimalField(decimal_places=2,
                                    max_digits=10)

    # Application rate. Will be calculated by the app using
    #
    #    (bags_used * bag_size) / (total area covered)
    rate = models.FloatField(blank = True, null = True)

    # Cost of the fertilizer application. Will be calculated by the
    # app using
    #
    #       bags_used * price_per_bag
    cost = models.DecimalField(decimal_places = 2,
                               max_digits = 10,
                               blank=True,
                               null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_cost(self):
        fert = self.fertilizer
        ppb = fert.price_per_bag
        self.cost = self.bags_used * ppb

class GreensFert(Fertilizing):
    """
    GreensFert class

    A subclass of Fertilizing.
    Used to track instances of Fertilizing in which the area(s)
    covered were golf greens.
    """

    class Meta:
        verbose_name_plural = 'Greens fertilizations'

    # Greens fertilized in a many-to-many model. References one or
    # more instances of the courses/Green model
    green = models.ManyToManyField('courses.Green')

class TeeFert(Fertilizing):
    """
    TeeFert class

    A subclass of Fertilizing.
    Used to track instances of Fertilizing in which the area(s)
    covered were golf tees.
    """

    class Meta:
        verbose_name_plural = 'Tee fertilizations'

    # Tees fertilized in a many-to-many model. References one or 
    # more instances of the courses/Tee model
    tee = models.ManyToManyField('courses.Tee')

class FairwayFert(Fertilizing):
    """
    FairwayFert class

    A subclass of Fertilizing.
    Used to track instances of Fertilizing in which the area(s)
    covered were golf fairways.
    """

    class Meta:
        verbose_name_plural = 'Fairway fertilizations'

    # Fairways fertilized in a many-to-many model. References one or
    # more instances of the courses/Fairway model
    fairway = models.ManyToManyField('courses.Fairway')

class RoughFert(Fertilizing):
    """
    FairwayFert class

    A subclass of Fertilizing.
    Used to track instances of Fertilizing in which the area(s)
    covered were golf fairways.
    """

    class Meta:
        verbose_name_plural = 'Rough fertilizations'

    # Roughs fertilized in a many-to-many model. References one or 
    # more instances of the courses/Rough model
    rough = models.ManyToManyField('courses.Rough')
