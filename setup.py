from setuptools import setup, find_packages

setup(
    name='iAlignment',
    version="0.0.1",
    packages=find_packages(exclude=["examples", "tests"]),
    url='https://github.com/OpenGreekAndLatin/ILA_python',
    license='GNU GPL',
    author='Tariq Yousef',
    author_email='tariq.yousef@dh.uni-leipzig.de',
    description='Intra Language Alignment tool',
    test_suite="tests",
    zip_safe=False
)
