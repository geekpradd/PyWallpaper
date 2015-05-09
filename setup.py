from setuptools import setup
try:
    import pypandoc
    description = pypandoc.convert('README.md','rst')
except:
    description=''

setup(
    name = "PyWallpaper",
    version = '1.0.0',
    author = 'Pradipta Bora',
    author_email = 'pradd@outlook.com',
    description = "Cross Platform Python module to change wallpaper",
    license = "MIT",
    keywords = "wallpaper",
    url = "https://github.com/geekpradd/PyWallpaper",
    py_modules = ['PyWallpaper'],
    long_description=description,
    classifiers=[
     "Development Status :: 5 - Production/Stable",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
    ],

)