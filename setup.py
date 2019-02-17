from distutils.core import setup

setup(
    name='AudioFilters',
    version='0.1dev',
    author=['Marcelle Chiriboga', 'Paul Vial', 'Socorro Dominguez'],
    packages=['audiofilters'],
    license='',
    description='This package provides functions that add effects to vectors read from audio files.',
    url='https://github.com/UBC-MDS/AudioFilters_py',
    install_requires=['numpy', 'librosa']
)
