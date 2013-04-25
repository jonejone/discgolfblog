#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Jone'
SITENAME = u'Disc Golf utviklingsblogg'
SITEURL = 'http://treningsblogg.caddybok.no'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'no'
DISQUS_SITENAME = 'discgolfutviklingsblogg'
GOOGLE_ANALYTICS = 'UA-36863156-2'

# Blogroll
LINKS =  (('Frisbeegolf.no', 'http://www.frisbeegolf.no'),
          ('Caddybok', 'http://www.caddybok.no'),
          ('DiscTourney', 'http://www.disctourney.com'),
          ('Discgolfgutta', 'http://discgolfgutta.com'),
)

# Social widget
SOCIAL = ()

PLUGINS = [
    'pelican.plugins.gravatar',
]

DEFAULT_PAGINATION = 10
