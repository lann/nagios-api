from distutils.core import setup
import nagios

setup(name='nagios-api',
      version=nagios.version,
      description='Control nagios using an API',
      author='Mark Smith',
      author_email='mark@qq.is',
      url='https://github.com/xb95/nagios-api',
      packages=['nagios'],
      scripts=['nagios-cli', 'nagios-api'],
      install_requires=[
        'diesel==2.1.1',
        'greenlet==0.3.4'
      ]
     )