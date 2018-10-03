import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

sfc_module = Extension(
    'superfastcode2', sources=['module.cpp'],
    include_dirs=['pybind11/include'],
    language='c++',
    extra_compile_args=cpp_args,
    )

setup(
    name='superfastcode2',
    version='1.0',
    description='Python package with superfastcode2 C++ extension (PyBind11)',
    ext_modules=[sfc_module],
)
