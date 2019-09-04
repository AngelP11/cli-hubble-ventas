from setuptools import setup


setup(
    name='hv',
    version='0.1',
    py_modules=['hv'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        hv=hv:cli
    """,
)
