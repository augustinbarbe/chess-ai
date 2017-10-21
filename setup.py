from setuptools import setup

setup(
    name='chessai',
    packages=['chessai'],
    include_package_data=True,
    install_requires=[
        'redis',
    ],
)
