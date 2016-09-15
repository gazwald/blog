# Blogzwald

## Overview

I wanted to make my own blog in Python/Django so I did.

My plan for this thing is roughly:

1. Create something that will function as a blog
2. Deploy on AWS Elastic Beanstalk
3. Create unit and functional tests
4. Create AWS Pipeline for continuous deployment
5. Integrate things like S3 and ElastiCache

The general idea is to learn more about Django and AWS at the same time while blogging about it.

## Environment

Written in VIM

* tabstop=4
* shiftwidth=4
* expandtab

Targeting Python 3.4 on RHEL/Fedora based systems

See requirements.txt for package versions.

Currently checking test coverage with Coverage 4.2

## Useful links

AWS Guide for deploying Django to ElasticBeanstalk:
* http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

This article was super useful when working out how Python/Django/ElasticBeanstalk come together:
* https://realpython.com/blog/python/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/
