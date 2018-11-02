from setuptools import setup, find_packages

requirements = [
    x.strip() for x
    in open('requirements.txt').readlines() if not x.startswith('#')]

setup(
    name='python-coconut-protos',
    version='0.0.1',
    author='Importcjj',
    author_email='importcjj@gmail.com',
    url='https://github.com/coconut/python-coconut-protos',
    license='MIT',
    description='',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)