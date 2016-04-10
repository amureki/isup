from setuptools import setup, find_packages

required_packages = [
    'requests',
]

setup(
    name='isup',
    version='0.3',
    description='isitup.org command-line utility',
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
    install_requires=required_packages,
    zip_safe=False
)
