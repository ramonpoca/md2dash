from setuptools import setup

setup(name='md2dash',
      version='0.1',
      description='A Markdown to Dash cheatsheet converter',
      url='http://github.com/ramonpoca/md2dash',
      author='Ramon Poca',
      author_email='ramon.poca@gmail.com',
      license='GPLv3',
      packages=['md2dash'],
      install_requires=[
          'markdown', 'mistune'
      ],
      zip_safe=False)
