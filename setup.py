from distutils.core import setup

README_PATH = "README.md"
long_description = ""
with open(README_PATH, "r", encoding="utf-8") as file:
    long_description = file.read()
    
setup(
  name = 'impytool',      
  packages = ['impytool'],  
  version = '0.4',      
  license='MIT',        
  description = 'impytool is an opencv based tool that facilitates some image processing operations',   
  author = 'ny.ahmet',                   
  author_email = 'any43071@gmail.com',      
  url = 'https://github.com/nyahmet/impytool',   
  download_url = 'https://github.com/nyahmet/impytool/archive/v_04.tar.gz',    
  keywords = ['image', 'tool', 'processing' , 'color' , 'detection'],   
  install_requires=[            
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
