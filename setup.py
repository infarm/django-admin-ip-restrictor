import os
from setuptools import find_packages, setup

from admin_ip_restrictor import __version__

PROJECT_DIR = os.path.dirname(__file__)

with open(os.path.join(PROJECT_DIR, 'README.rst')) as readme:
    long_description = readme.read()

install_requires = [
    'django>=2.2; python_version >= "3.7.0"',
    'django-ipware>=2',
]

test_requires = [
    'coverage',
    'pytest',
    'pytest-cov',
    'pytest-django',
    'pytest-sugar',
    'tox',
]

setup(
    name='django-admin-ip-restrictor',
    version=__version__,
    packages=find_packages(exclude=["tests.*", "tests", ".tox"]),
    include_package_data=True,
    license='MIT License',
    description='A Django middleware to restrict incoming IPs to admin panel',
    long_description=long_description,
    url='https://github.com/sdonk/django-admin-ip-restrictor/',
    author='Alessandro De Noia',
    author_email='alessandro.denoia@gmail.com',
    install_requires=install_requires,
    extras_require={
        'tests': test_requires,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
