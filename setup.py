import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='simpleaibackendswitcher',
    author='raymond lowe',
    author_email='raymond@wlmedia.com',
    description='simple ai backend switcher',
    keywords='ai, chatgpt, openai, poe, llama.cpp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raymondlowe/simpleaibackendswitcher',
    project_urls={
        'Documentation': 'https://github.com/raymondlowe/simpleaibackendswitcher',
        'Bug Reports':
        'https://github.com/raymondlowe/simpleaibackendswitcher/issues',
        'Source Code': 'https://github.com/raymondlowe/simpleaibackendswitcher'
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',        
       
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=simpleaiswitcher:main',
    # You can execute `run` in bash to run `main()` in src/simpleaiswitcher/__init__.py
    #     ],
    # },
)
