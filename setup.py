from distutils.core import setup

setup(
    name='AudioFilters',
    version='0.1dev',
    packages=['AudioFilters',],
    license='',
    long_description=open('README.md').read(),
    scripts=['AudioFilters/high_pass_filter.py'],

)
