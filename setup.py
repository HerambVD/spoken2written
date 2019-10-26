import setuptools


with open('README.md') as f:
    README = f.read()
    
setuptools.setup(
    author="Heramb Devbhankar",
    author_email="heramb1711@gmail.com",
    name='spoken2written',
    license="MIT",
    description='This package is to translate spoken languag to its written form',
    version='v0.1.4',
    long_description=README,
    url='https://github.com/HerambVD/spoken2written',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['spacy','word2number'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
