from setuptools import setup, find_packages

setup(
    name='psp',
    version='1.0.0',
    packages=find_packages(),
    description='A Python module implementing various sorting algorithms.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Cuisset Mattéo',
    author_email='matteo.cuisset@gmail.com',
    url='https://github.com/Flyns157/psp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[],
)
