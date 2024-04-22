from setuptools import setup, find_packages

setup(
    name='ailogger_PythonSDK',
    version='0.1',
    packages=find_packages(),
    author='sarag5',
    author_email='your.email@example.com',
    description='A AI logger for monitoring errors, logs, and metrics in your application.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
    'requests>=2.22.0',
    # Add other dependencies here
    ],
)