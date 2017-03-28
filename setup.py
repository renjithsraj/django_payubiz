import sys
import os
from os.path import join, dirname, split
from setuptools import setup

LONG_DESCRIPTION = """
Django Sauth is an easy to setup social authentication/registration
mechanism with support for several auth providers.
"""


# def long_description():
#     """Return long description from README.rst if it's present
#     because it doesn't get installed."""
#     try:
#         return open(join(dirname(__file__), 'README.rst')).read()
#     except IOError:
#         return LONG_DESCRIPTION

setup(
  name = 'payu_biz',
  packages = ['payu_biz'], # this must be the same as the name above
  version = '1.1',
  description = LONG_DESCRIPTION,
  author = 'Renjith S Raj',
  author_email = 'renjithsraj@live.com',
  url = 'https://github.com/renjithsraj/django_payubiz/tree/master/payu_biz', # use the URL to the github repo
  download_url = 'https://github.com/renjithsraj/django_payubiz/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['payu', 'payment gateway', 'payu gateway django', 'django gateway package'], # arbitrary keywords
  classifiers = [],
)