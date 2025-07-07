from setuptools import setup, find_packages

setup(
    name='backblaze-b2-uploader',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'b2sdk>=1.20.0',
        'pytest'
    ],
    description='Minimal utility to upload and access files on Backblaze B2 Cloud Storage',
    long_description=open('README.md').read(),
    author='Susmita Dhara',
    author_email='smitra258@gmail.com',
    url='https://github.com/susmitadhara/backblaze-b2-uploader',
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
)