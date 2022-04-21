from setuptools import setup, find_packages


setup(
    name="backend_framework_library",
    version="1.1",
    packages=find_packages(),
    install_requires=[
      'flask',
      'gunicorn',
      'pytest',
      'pytest-cov',
      'black',
      'flask-swagger',
      'Flask-Cors'
    ],
)
