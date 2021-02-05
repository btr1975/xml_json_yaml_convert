from setuptools import setup
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about = {}
with open(os.path.join(base_dir, 'xml_json_yaml_convert', 'version.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

packages = [
    'xml_json_yaml_convert'
]

install_requires = [
    'PyYAML ~= 5.4.1',
    'xmltodict ~= 0.12.0',
]

tests_require = [
    'pytest',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    python_requires='>=3.6',
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=about['__keywords__'],
    url=about['__url__'],
    project_urls={
        'Documentation': 'https://xml_json_yaml_convert.readthedocs.io/en/latest/',
        'Source': 'https://github.com/btr1975/xml_json_yaml_convert',
        'Tracker': 'https://github.com/btr1975/xml_json_yaml_convert/issues',
    },
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    test_suite='pytest',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
