from setuptools import find_packages, setup

setup(
    name='netbox_route_static',
    version='0.1.0',
    description='NetBox Static Routing',
    long_description='Plugin for documentation of static routing configuration',
    url='https://github.com/wvandervaart/netbox_route_static',
    download_url='https://github.com/wvandervaart/netbox_route_static',
    author='Wouter van der Vaart',
    author_email='wouter@terrean.net',
    maintainer='Wouter van der Vaart',
    maintainer_email='wouter@terrean.net',
    license='All rights reserved',
    platform=[],
    keywords=['netbox', 'netbox-plugin'],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'django-polymorphic',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
