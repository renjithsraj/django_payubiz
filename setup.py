from setuptools import setup

LONG_DESCRIPTION = """ payu payment gateway package for django"""


setup(
  name = 'payu_biz',
  packages = ['payu_biz'], # this must be the same as the name above
  version = '1.3.1',
  description = LONG_DESCRIPTION,
  license='MIT',
  author = 'Renjith S Raj',
  author_email = 'renjithsraj@live.com',
  url = 'https://github.com/renjithsraj/django_payubiz/tree/master/payu_biz', # use the URL to the github repo
  download_url = 'https://github.com/renjithsraj/django_payubiz/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['payu payment gateway package django','payment gateway python package','payu', 'payu python package','payment gateway', 'payu gateway django', 'django gateway package'], # arbitrary keywords
  classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)