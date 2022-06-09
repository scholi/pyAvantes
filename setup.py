from setuptools import setup, find_packages
import re

def description():
    with open('README.md') as f:
        return f.read()

def find_version():
    with open("pyAvantes/__init__.py",'r') as fp:
        src = fp.read()
        version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", src, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find vesrion string.")
setup(
    name="pyAvantes",
    version=find_version(),
    description="library to handle Avantes Raw8 spectra",
    long_description=description(),
    long_description_content_type="text/markdown",
    url="https://github.com/scholi/pyAvantes",
    author = "Olivier Scholder",
    author_email = "o.scholder@gmail.com",
    license="Apache 2.0",
    keywords='spectromter spectrum Avantes raw8',
    packages=find_packages(exclude=['contrib','docs','tests']),
    package_data={},
    include_package_data=False,
    entry_points = {
        'console_scripts' : [],
        'gui_scripts':[]
    },
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
