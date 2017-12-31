from setuptools import setup
from googlerpc import index as package

setup(
    name='googlerpc',
    packages=['googlerpc'],
    version=package.__version__,
    description='A Google Play Music song displayer for Discord',
    author='AlexFlipnote',
    author_email='root@alexflipnote.xyz',
    url='https://github.com/AlexFlipnote/googlerpc',
    keywords=['googlerpc'],
    entry_points={
        "console_scripts": [
            "googlerpc=googlerpc.index:main"
        ],
    },
)
