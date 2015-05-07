from setuptools import setup, find_packages

setup(
    name='isup',
    version='0.1',
    description='isup.me command-line utility',
    author='Rustem Sayargaliev',
    author_email='r.sayargaliev@gmail.com',
    license='MIT',
    url='https://github.com/amureki/isup.git',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'isup = isup.main:main',
        ],
    },
    zip_safe=False
)