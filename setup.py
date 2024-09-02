from setuptools import setup, find_packages

setup(
    name='phil_loc',
    version='0.5.7',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django library package for Locations/Addresses in the Philippines based on Philippine Standard Geographic Code(PSGC)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/delletran/phil_loc',
    author='Rodel Letran',
    author_email='delioletran@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=5.1',
    ],
)
