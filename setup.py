from setuptools import setup

setup(
    name='jsnDB',
    description="A lighweight JSON-BASED database",
    version="1.0.0",
    license="Apache License 2.0",
    url='https://github.com/dracxi/jsnDB',
    author='DracX',
    author_email='dracx.py@gmail.com',
    py_modules=['jsnDB'],
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)