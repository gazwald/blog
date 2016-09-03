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

Targeting Python 3.4

See requirements.txt for package versions.

Currently checking test coverage with Coverage 4.2

## TODO

* Login page
* Google reCaptcha
* Image upload and management
* Basic WYSIWYG editor for posts
* Fixtures
* Unit tests
* Integration tests
* Functional tests
* Elastic Beanstalk - (http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
* Fix CORS on S3 - (https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)
* Pipeline
* Memcache/Redis (ElastiCache)
* CloudFront
* Google Analytics
