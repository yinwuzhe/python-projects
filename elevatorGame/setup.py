try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'yinwuzhe',
    'url': ' ',
    'download_url': 'Where to download it.',
    'author_email': '704064151@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['elevator'],
    'scripts': [],
    'name': 'elevatoGame'
}

setup(**config)
