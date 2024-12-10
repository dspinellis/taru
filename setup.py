"""
Taru is a Unix command-line tool that processes a tar(1) listing to display
the cumulative size of files stored in individual directories.
Its output and options are similar to the Unix disk usage command du(1).
"""
from setuptools import find_packages, setup

dependencies = []

setup(
    name='taru',
    version='1.0.3',
    url='https://github.com/dspinellis/taru',
    license='Apache Software License',
    author='Diomidis Spinellis',
    author_email='dds@aueb.gr',
    keywords='tar, du, size',
    description='Taru processes a tar listing to display the cumulative size of files stored in individual directories.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    data_files=[("share/man/man1", ["man/taru.1"])],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'taru = taru.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Archiving',
        'Topic :: Utilities'
    ]
)
