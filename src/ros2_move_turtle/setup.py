from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_move_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xiwei',
    maintainer_email='xiwei@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_move_exec = ros2_move_turtle.turtle_move:main',
        ],
    },
)
