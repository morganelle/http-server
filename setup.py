"""creating python distribution package setup.py."""
from setuptools import setup

setup(
    name="http-server",
    description="A concurrent web server.",
    version=0.1,
    author="Morgan, Ronel, Kurt",
    author_email="",
    license='MIT',
    py_modules=['client', 'server'],
    package_dir={'': 'src'},
    install_requires=['gevent'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
            "client = client:client",
            "server = server:server"
        ]
    }
)
