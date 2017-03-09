**EDIT: THIS IS DEPRECATED. FORK OR USE SOMETHING ELSE!**

_Since Textbelt has discontinued their service, you would need to modify this to allow a configurable Textbelt endpoint
and secret key/access token. As you can tell, I have not worked on this in a while so that's not super going to
happen anytime soon, feel free to fork this guy and give it the love it deserves._

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

