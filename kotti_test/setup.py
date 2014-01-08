from setuptools import setup

setup(
    name='kotti_test',
    version='0.1',
    install_requires=[
        'colander',
        'kotti',
    ],
    message_extractors={
        'kotti_test': [
            ('**.py', 'lingua_python', None),
            ('**.pt', 'lingua_xml', None),
        ],
    },
)
