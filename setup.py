from setuptools import setup
import os

setup(name='aggregator',
      version='0.1.0',
      description='Simple dataframe aggregation',
      long_description=open('README.md').read(),
      url='https://github.com/newknowledge/aggregator',
      download_url ='https://github.com/newknowledge/aggregator/tarball/v0.1.0',
      author='Jonathon Morgan',
      author_email='jonathon@newknowledge.io',
      license='MIT',
      packages=['aggregator'],
      test_suite='tests',
      dependency_links=[
            'dateutil',
            'pandas',
            'numpy'],
      zip_safe=False)