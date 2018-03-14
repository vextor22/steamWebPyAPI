from setuptools import setup

setup(name='SteamAPI',
        version='0.1',
        description='Steam webAPI interface',
        install_requires=[
            "requests==2.18.4",
            ],
        url='https://github.com/vextor22/steamWebPyAPI',
        author='Matthew Higgins',
        author_email='mrhiggi@g.clemson.edu',
        packages=['SteamAPI'],
        zip_safe=False)


