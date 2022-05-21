from setuptools import setup, find_packages
setup(
    name="colablibm",
    version="1.0",
    packages=['colablibm'],
    install_requires=['ffmpeg-python', 'mediapipe', 'pillow', 'numpy'],

    # metadata to display on PyPI
    author="claireye",
    author_email="aijackliu@gmail.com",
    description="Some useful Python stuff for Google Colab notebooks",
    keywords="Notebook colab colaboratory google Numpy PIL OpenCV",
    url="https://github.com/advcloud/colablibm",
    classifiers=[
        'Programming Language :: Python :: 3 :: Only' # https://pypi.org/classifiers/
    ]
)

# https://setuptools.readthedocs.io/en/latest/setuptools.html
