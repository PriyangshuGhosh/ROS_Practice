from setuptools import find_packages, setup

package_name = 'my_1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='darkknight',
    maintainer_email='darkknight@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "my_node=my_1_pkg.my_first_node:main",
            "bot_transmitter=my_1_pkg.robot_news_station:main",
            "bot_receiver=my_1_pkg.robot_receiver:main",
            "num_pub=my_1_pkg.number_publisher:main",
            "num_counter=my_1_pkg.number_counter:main",
            "server=my_1_pkg.server:main",
            "client=my_1_pkg.client:main",
            "reset=my_1_pkg.reset_counter:main"

        ],  
    },
)
