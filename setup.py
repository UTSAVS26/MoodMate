from setuptools import setup, find_packages

setup(
    name='moodmate',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'textblob',
        'streamlit',
    ],
    description='A project for analyzing mood from daily journal entries and providing suggestions.',
    author='UUtsav Singhal',
    author_email='utsavsinghal26@gmail.com',
    url='https://github.com/UTSAVS26/moodmate',
)