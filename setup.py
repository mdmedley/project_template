from setuptools import setup, find_packages

setup(name='project_name',
      version='0.0.1',
      description='Skeleton Project',
      author='Marcus Medley',
      author_email='mdmeds@gmail.com',
      packages=find_packages(exclude=[]),
      entry_points={
          'console_scripts': [
              'project_template = project_name.project:main'
          ]
      }
)
