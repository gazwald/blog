# Blogzwald

## Overview

I wanted to make my own blog in Python/Django so I did.

My plan for this thing is roughly:

1. Create something that will function as a blog
2. Deploy on AWS ELB
3. Create unit and functional tests
4. Create AWS Pipeline for continuous deployment
5. Integrate things like S3 and ElasticCache

The general idea is to learn more about Django and AWS at the same time while blogging about it.

## Environment

Written in VIM

* tabstop=4
* shiftwidth=4
* expandtab

Targeting Python 3.4

See requirements.txt for package versions.

## TODO

Login
Add post
Basic WYSIWYG editor for posts
Custom CSS
Unit tests
ELB - http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
S3 - Move static content into S3
CodeCommit?
Pipeline
CloudFront
