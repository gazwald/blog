# Blog-zwald

## Overview

I wanted to make my own blog in Python/Django so I did.

My plan for this thing is roughly:

1. Create something that will function as a blog
2. Create unit and UAC tests
3. Create AWS Pipeline for continuous deployment

The general idea is to learn more about Django and AWS at the same time while blogging about it.

## Environment

Written in VIM

* tabstop=4
* shiftwidth=4
* expandtab

Targeting Python 3.6 on RHEL 7/FreeBSD 11 based systems

See requirements.txt for package versions.

Currently checking test coverage with Coverage 4.4

## Tests

Django tests:

./manage test

Code coverage:
coverage run --source='.' manage.py test myapp
coverage report
