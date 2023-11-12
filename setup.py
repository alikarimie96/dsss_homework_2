from setuptools import setup, find_packages

setup(
    name='dsss_homework_2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        random,
        math,
        unittest
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.module_name:main',
        ],
    },
    author='Ali',
    author_email='QQQQQQQQQQQQQQ',
    description='QQQQQQQQQQQQQQQQQQQQQQ',
    url='https://github.com/alikarimie96/dsss_homework_2',
)
