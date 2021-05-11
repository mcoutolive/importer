# Para utilizar bibliotecas não nativas do Python, é necessário instalá-las antes

try:
    from pip import main
except:
    from pip._internal import main

libs = ['schedule', 'pywin32']

for lib in libs:
    main(['install', str(lib), '-i',
          'https://depdes.artifactory.prod.cloud.ihf/artifactory/api/pypi/python-devel/simple/',
          '--trusted-host', 'depdes.artifactory.prod.cloud.ihf', '--user'])
