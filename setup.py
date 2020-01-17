import os
import setuptools

__version__ = "1.0"
__author__ = "Kevin Jonathan"

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='gojek-api',
    version=__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    description='Gojek private API Python',
    long_description=README,
    keywords="Gojek Private API Python",
    platforms='any',
    url='https://github.com/kevinjon27/GojekAPI',
    author=__author__,
    author_email='kevinjonathan2701@gmail.com',
    install_requires=[
        'promise==2.2.1',
        'six==1.13.0',
    ],
    classifiers=[
        # 'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)