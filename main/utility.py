"""
utility module where all the generalised function present
which can be imported any where in the code base"""
import params
import re

def check(email):
    """
    Return True or False after checking whether email is in
    valid format or not


    Parameters
    ----------
    email : str
        email address that need to be validated

    Returns
    -------
    True/False
    """

    if (re.search(params.regex, email)):
        return True
    else:
        return False

#method to add ordinal to numbers
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
