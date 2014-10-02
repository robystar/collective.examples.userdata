from setuptools import setup, find_packages
import os

version = '2.2.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read() + "\n"

long_description = \
    read('README.rst') + \
    read('docs', 'HISTORY.txt') + \
    read('docs', 'TODO.txt')

setup(
    name='collective.examples.userdata',
    version=version,
    description="Showcase for the new (Plone 5) plone.app.users "
                "IUserDataSchema. Shows how to extend the user data fields "
                "that can be selected for the registration form.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Kees Hink',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/collective/collective.examples.userdata',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.examples'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.users >= 2.0',

    ],
    extras_require={
        'test': ['plone.app.testing'],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
