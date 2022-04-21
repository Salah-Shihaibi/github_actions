from setuptools import setup, find_packages


setup(
    name="r2_factory_platform",
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
