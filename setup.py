from setuptools import setup

import json
import os

def read_pipenv_dependencies(fname):
    """Получаем из Pipfile.lock зависимости по умолчанию."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]

if __name__ == '__main__':
    setup(
        name='turkey_eq',
        version='1.7',
        description='Package for practical work on Turkey_EQ.',
        license='MIT',
        url='https://github.com/EkaterinaKugot/Turkey_EQ_notebook.git',
        packages=['turkey_eq'],       
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ],
        python_requires='>=3.10',
    )