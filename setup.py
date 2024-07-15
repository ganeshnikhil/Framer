from distutils.core import setup
setup(
    name='Framer',
    packages=['Framer'],
    version='0.1',
    license='Apache 2.0',
    description='Add frames and titles to your Google Play screenshots',
    author='Ganesh nikhil',
    author_email='ganeshnikhil124@gmail.com',
    url='https://github.com/ganeshnikhil/Framer',
    keywords=['Framer', 'computer', 'android', 'images', 'framing'],
    install_requires=['pillow==10.4.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    entry_points={
        'console_scripts': [
            'framer=Framer.main:main',
        ],
    },
)

