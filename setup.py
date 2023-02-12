from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='vpylib',
    version='0.0.1',
    description='Vicos python libary with usefull decorators and functions.',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='https://github.com/VicoShortman',
    author='Vico Shortman',
    author_email='vico.shortman@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='tools time timestamp conversion decorators benchmark',
    packages=find_packages(),
    install_requires=['']
)
