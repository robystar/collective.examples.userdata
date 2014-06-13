from setuptools import setup, find_packages
import os

version = '0.4'

setup(name='collective.examples.userdata',
      version=version,
      description="Estende i campi di registrazione per il portale Fondimpresa Liguria.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read() + "\n"
                       + open(os.path.join("docs", "TODO.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kees Hink',
      author_email='',
      url='https://github.com/collective/collective.examples.userdata',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.examples'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.users >= 1.0b7',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
