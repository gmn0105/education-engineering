def logger(**kwargs):
    """
    This method is a logger function to log any values
    :param kwargs: Variable arguments
    """
    print "-----------------------------------------------------------------------"
    print "----------------------------Logger-------------------------------------"
    print "-----------------------------------------------------------------------"
    for key in kwargs:
        print key + str(':'), kwargs[key]
    print "-----------------------------------------------------------------------"
    print "-----------------------------------------------------------------------"
    print "-----------------------------------------------------------------------"
