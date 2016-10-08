try: 
    from setuptools import setup
except ImportError: 
    from distutils.core import setup

setup(
    name='django-tekextensions',
    version=__import__('tekextensions').__version__,
    description='A set of re-usable widgets and commands for django',
    long_description='',
    author='Adam Stein',
    author_email='adam@csh.rit.edu',
    url='http://github.com/adamestein/django-tekextensions',
    download_url='http://github.com/adamestein/django-tekextensions',
    license='BSD',
    packages=['tekextensions'],
    include_package_data = True,
    classifiers = [
            'Framework :: Django',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
    ],
)
