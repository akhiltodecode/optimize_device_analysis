from setuptools import setup, find_packages

setup(
    name='optimize_device_analysis',
    version='0.1.1',
    author='Akhilesh Keerthi',
    author_email='akhileshkeerthi@gmail.com',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'optimize_device_analysis = optimize_device_analysis.__main__:main',
        ],
    },
)