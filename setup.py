import pathlib

import pkg_resources
import setuptools
import codecs
import os.path

here = pathlib.Path(__file__).parent.resolve()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with codecs.open('requirements.txt', 'r', encoding='utf-16') as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]



def read(rel_path):
    path = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(path, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='django_seo_module',
    author='Darkdeal',
    version=get_version("src/django_seo_module/__init__.py"),
    author_email='mark@goltsev.net',
    description='django SEO optimization module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache2',
    url='https://github.com/goltsevnet/Django-SEO-Module.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: Apache Software License',
    ],
    packages=setuptools.find_packages(
        where='src',
        include=['django_seo_module', 'django_seo_module.*'],
        exclude=['django_seo_module.tests']
    ),
    package_dir={'': 'src'},
    python_requires=">=3.6",
    install_requires=install_requires,
    include_package_data=True
    # package_data={
    #     'static': ['src/django_seo_module/static/*.js'],
    # },
)
