# ******************************************************************************
#
# cs-hello-world, python hello world project
#
# Copyright 2024 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# ******************************************************************************

"""Hello functions."""

# Above this comment is the file banner, with basic information about
# the program and typical copyright and license information.  The
# string inside three quotation marks documents what this file does in
# the program and is only used when generating documentation.

# This line imports the ``sys`` module and allows access to system
# utilities.
import sys


# This is a function, with an optional argument ``msg``.  It will
# print ``msg``.
#
# Change the ellipses (...) to make the program behave as specified.
#
# Giving a variable a value in a function definition sets a default
# value for the variable.  If a new value is not supplied when the
# function is called, it uses the default value.
#
# Change the ellipsis to set the default value of ``msg`` to be
# "Hello, world!".  This type of variable is a string and values for
# strings must be in quotation marks, either single or double.
def hello(msg=...):
    """Print ``msg``.

    Print ``msg``.

    Parameters
    ----------
    msg : str
        The message to print.

    Returns
    -------
        ``None``.
    """
    # The information above is the documentation for this function.
    # The format used above allows software that generates
    # documentation automatically to create the documentation for this
    # function.

    # Change the ellipsis below to make the ``print`` function print
    # the variable ``msg``.  Do not use quotation marks around
    # variable names.
    print(...)


# Copy and modify the ``hello`` function above so that it says
# "Goodbye" instead of hello.
def goodbye(msg=...):
    """Print goodbye messages."""
    pass


# A function named ``main`` is typically the function that runs a
# program, although it is not required to have this name.  Here,
# ``main`` just runs ``hello``.
def main():
    """Run the program."""
    hello()


# This construct is used so that this file may work as a program or as
# a module.  When used as a program, this will run ``main``, which
# runs ``hello``, and then exits.  When used as a module, this will be
# ignored.
if __name__ == "__main__":
    sys.exit(main())
