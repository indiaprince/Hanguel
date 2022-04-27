
import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hanguel",
    version="0.0.0.1",


    author="indiaprince",
    author_email="hyeonsuhan@gmail.com",


    license='MIT',


    description="Python Hanguel preprocess package for TTS(Text To Speech) STT | TTB(Text To Braille) BTT |",

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

    keywords='Python Project For Hanguel Decomposition & Construction',
)