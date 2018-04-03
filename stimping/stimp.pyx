cpdef double list_sum(list values):
    """ Calculates the sum of a Python list of numeric values """
    cdef double total = 0
    for item in values:
        total += item
    
    return total


cpdef int list_count(list values):
    """ Returns the number of items in a Python list """
    cdef int count = 0
    for item in values:
        count += 1

    return count


cpdef double list_mean(list values):
    """ Returns the arithmetic mean from a Python list of values """

    return list_sum(values) / list_count(values)


cpdef double stimp_one_axis(double x_1,
                            double x_2,
                            double x_3,
                            double w_1,
                            double w_2,
                            double w_3):
    """ Takes three ball rolls in each direction along a single axis
        and returns the calculated green speed using the
        USGA-approved method.
    """

    cdef double mean_x = list_mean([x_1, x_2, x_3])
    cdef double mean_w = list_mean([w_1, w_2, w_3])
    
    return list_mean([mean_x, mean_w]) / 12.0


cpdef double stimp_two_axes(double x_1,
                            double x_2,
                            double x_3,
                            double w_1,
                            double w_2,
                            double w_3,
                            double y_1,
                            double y_2,
                            double y_3,
                            double z_1,
                            double z_2,
                            double z_3):
    """ Takes three ball rolls in each direction along a two-
        dimensional (x-y) axis, and returns the calculated green
        speed using the expanded USGA method.
    """

    cpdef double x_axis = stimp_one_axis(x_1, x_2, x_3,
                                         w_1, w_2, w_3)
    cpdef double y_axis = stimp_one_axis(y_1, y_2, y_3,
                                         z_1, z_2, z_3)

    return list_mean([x_axis, y_axis])


cpdef double list_std_dev(list values):
    """ Returns the standard deviation for a Python list of values.
        Uses the 1/n method for when n (the number of items in the
        list) is relatively small.
    """
    cdef int n = list_count(values)
    cdef double mean = list_mean(values)
    cdef double deviation = 0

    for item in values:
        cur_dev = item - mean
        deviation += (cur_dev * cur_dev)

    return deviation / n


cpdef double stimp_one_axis_adjusted(double x_1,
                                     double x_2,
                                     double x_3,
                                     double w_1,
                                     double w_2,
                                     double w_3):
    """ Takes three ball rolls in each direction along a single axis
        and calculates the green speed, adjusted for slope using
        Dr. A. Douglas Brede's simplified method.
    """
    cdef double x_mean = list_mean([x_1, x_2, x_3])
    cdef double w_mean = list_mean([w_1, w_2, w_3])

    return (x_mean * w_mean) / (6 * (x_mean + w_mean))


cpdef double stimp_two_axes_adjusted(double x_1,
                                     double x_2,
                                     double x_3,
                                     double w_1,
                                     double w_2,
                                     double w_3,
                                     double y_1,
                                     double y_2,
                                     double y_3,
                                     double z_1,
                                     double z_2,
                                     double z_3):
    """ Takes three ball rolls in each direction along two axes and
        calculates the green speed, adjusted for slope using an
        expanded form of Dr. A. Douglas Brede's simplified method.
    """
    cdef double x = list_sum([x_1, x_2, x_3])
    cdef double w = list_sum([w_1, w_2, w_3])
    cdef double y = list_sum([y_1, y_2, y_3])
    cdef double z = list_sum([z_1, z_2, z_3])

    cdef double num = x*w*(y + z) + y*z*(x + w)
    cdef double den = 36.0 * (x + w) * (y + z)

    return num / den


cpdef double get_friction_coeff(double s_bar):
    """ Calculates the coefficient of kinetic friction (\mu_k) using
        the green speed on a LEVEL green (denoted as s_bar). This 
        can then be used to calculate more accurate adjusted speeds 
        on slopes of known angle using Weber's expansion of Dr. 
        Brede's method. Assumes a golf ball weight of 1.62 oz., 
        stimpmeter length of 36 in., and stimpmeter notch release 
        angle of 20.5 deg above horizontal.
    """
    return 0.983 / s_bar
