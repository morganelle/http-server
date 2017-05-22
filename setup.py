"""creating python distribution package setup.py."""
from setuptools import setup

setup(
    name="http-server",
    description="A script that uses a client and server to echo a message.",
    version=0.1,
    author="Morgan, Ronel, Kurt",
    author_email="",
    license='MIT',
    py_modules=['client', 'server'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
            "client = client:client",
            "server = server:server"
        ]
    }
)
