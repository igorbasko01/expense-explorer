from setuptools import setup, find_packages

setup(
    name="expense_explorer",
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        expense_explorer=expense_explorer.main:cli
    ''',
)