from distutils.core import setup, Extension


sfc_module = Extension('superfastcode', sources=['module.cpp'])

setup(name='superfastcode', version='1.0',
      description='Python Package with superfastcode C++ extension',
      ext_modules=[sfc_module]
      )
