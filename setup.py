from distutils.core import setup
# 必须部分
from distutils.extension import Extension
# 必须部分
from Cython.Distutils import build_ext

ext_modules = [Extension("deal", ["deal.pyx"],
                         include_dirs=['C:\\Users\\HIn\\AppData\\Local\\Programs\\Python\\Python39\\include',
                                       'C:\\Users\\HIn\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site'
                                       '-packages\\murmurhash\\include',
                                       'C:\\Users\\HIn\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site'
                                       '-packages\\numpy\\core\\include',
                                       'C:\\Users\\HIn\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site'
                                       '-packages\\win32\\include',
                                       'C:\\Users\\HIn\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site'
                                       '-packages\\win32com\\include',
                                       r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt',
                                       r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\shared',
                                       r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\cppwinrt\winrt',
                                       r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\um',
                                       r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\winrt'],
                         library_dirs=[r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\ucrt\x64',
                                       r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\ucrt\x86',
                                       r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\ucrt_enclave\x64',
                                       r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\um\x64',
                                       r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\um\x86']
                         )]

setup(name="deal", cmdclass={"build_ext": build_ext}, ext_modules=ext_modules)
