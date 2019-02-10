from setuptools import setup

setup(name='SteamAPI',
        version='0.1.3',
        description='Steam webAPI interface',
        install_requires=[
            'requests>=2.20.0'
            ],
        url='https://github.com/vextor22/steamWebPyAPI',
        author='Matthew Higgins',
        author_email='mrhiggi@g.clemson.edu',
        packages=['SteamAPI'],
        zip_safe=False)


