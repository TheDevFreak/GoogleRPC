from setuptools import setup

setup(
    name='googlerpc',
    packages=['googlerpc'],
    version='1.0.0',
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
