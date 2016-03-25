minipager
=========

A small Python utility that will monitor one of a set of sites, using [Textbelt](https://textbelt.com) to notify a
specified phone number in the event the site is down (i.e. server returns an unexpected response code for a certain
page.

DISCLAIMER: **NOT FOR PRODUCTION USE.**


Starting out
------------

The following will go and install the dependencies (currently just the awesome [requests](http://docs.python-requests.org/en/master/) library):

    > ./setup.sh

Running
-------

    > ./venv/bin/python minipager.py -h

