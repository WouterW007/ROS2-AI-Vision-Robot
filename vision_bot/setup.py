from setuptools import setup

package_name = 'vision_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='or4cl3',
    maintainer_email='or4cl3@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher_node = vision_bot.publisher:main',
                'subscriber_node = vision_bot.subscriber:main',

                            ],
                },
    
)
