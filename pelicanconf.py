#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aldi'
SITENAME = u'kriwil'
SITEURL = 'https://kriwil.com'

TIMEZONE = 'Asia/Jakarta'

THEME = 'themes/kriwil'
DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'custom_article_urls', 'sitemap']

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ALL_ATOM = None

# format
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
CATEGORY_URL = '{name}/'
CATEGORY_SAVE_AS = '{name}/index.html'
AUTHOR_URL = 'author/{name}/'
AUTHOR_SAVE_AS = 'author/{name}/index.html'
PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = 'page/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_URL = 'tags/index.html'

SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily',
    },
    'exclude': ['tag/', 'category/'],
}

CUSTOM_ARTICLE_URLS = {
    'links': {
        'URL': '{category}/{date:%Y%m%d}/{slug}/',
        'SAVE_AS': '{category}/{date:%Y%m%d}/{slug}/index.html',
    }
}

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 20

DISQUS_SITENAME = 'kriwil'
TWITTER_USERNAME = 'kriwil'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# pelican-cait
USE_CUSTOM_MENU = False
CUSTOM_MENUITEMS = (
    ('contact', 'pages/contact/'),
)

# CONTACT_EMAIL = "me@example.com"
CONTACTS = (
    ('twitter', 'https://twitter.com/kriwil'),
    ('github', 'https://github.com/kriwil'),
)
