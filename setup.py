
#!/usr/bin/env python
"""
Installs the Wagtail Guide plugin.
"""

from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='wagtail_guide',
      version='1.0.7',
      description='Adds functionality to add and edit a CMS guide page for editors.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/kevinhowbrook/wagtailguide',
      author='Kevin Howbrook - Torchbox',
      author_email='kevin.howbrook@torchbox.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.16',
      ])
