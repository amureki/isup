from setuptools import setup, find_packages

from isup import __version__

required_packages = [
    'requests',
]

setup(
    name='isup',
    version=__version__,
    description='isitup.org command-line utility',
    author='Rustem Sayargaliev',
    author_email='r.sayargaliev@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/amureki/isup.git',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'console_scripts': [
            'isup = isup.cli:main',
        ],
    },
    install_requires=required_packages,
    test_suite='tests',
)
