import json
import os
from setuptools import setup


with open(os.path.join('dash_extra_components', 'package.json')) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package['description'] if 'description' in package else package_name,
    url='https://github.com/plotly/dash-extra-components',
    install_requires=[]
)
