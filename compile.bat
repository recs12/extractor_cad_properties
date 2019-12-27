:: app name: opendoc
:: Set this file for compiling the executable of the macro.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./opendoc/__main__.py ^
./opendoc/Interop.SolidEdge.dll ^
./opendoc/api.py ./bullet/holes.py ^
./opendoc/equivalences.py ^
./opendoc/customs.py ^
/embed ^
/out:opendoc_macro_64x_0-0-0 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:logo.ico 
