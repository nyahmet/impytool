from distutils.core import setup
setup(
  name = 'impytool',      
  packages = ['impytool'],  
  version = '0.1',      
  license='MIT',        
  description = 'impytool is an opencv based tool that facilitates some image processing operations',   
  author = 'Ahmet Nuri Yılmaz',                   
  author_email = 'nyahmet7836@gmail.com',      
  url = 'https://github.com/nyahmet/impytool',   
  download_url = 'https://github.com/nyahmet/impytool/archive/v_01.tar.gz',    
  keywords = ['image', 'tool', 'processing' , 'color' , 'detection'],   
  install_requires=[            # I get to this in a second
          'opencv-python',
          'matplotlib',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
