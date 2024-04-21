import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
from setuptools import find_packages, setup

package_name = 'spot'
package_path = os.path.join('share', package_name)

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join(package_path,'urdf'), glob(os.path.join('urdf','spot_model.urdf'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srajara4',
    maintainer_email='srajara4@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
