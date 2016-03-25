wiringpi_ctypes
===========

This is libwiring python ctypes bindings, it should support python2 and python3.

when i use wiringpi-pythong for si4432 receive, sometimes met a "Fatal Python error: Segmentation fault" error. I don't known why. So i write a python ctypes binds for wiringpi, and used very well in my si4432 codes.
  
It should work under other platform only need replace the libwiring path.  

It only test under Raspbian (raspberry pi) now.


Usage
-----

- Install (on raspberry pi)  
    - install libwringpi:
    
        see http://wiringpi.com/
    
    - install libwiring_ctypes::

        git clone https://github.com/zaazbb/libwiring_ctypes
        cd libwiring_ctypes
        sudo python3 setup.py install  

- Example (on raspberry pi)  
    - to be write.    
  
todo
----

Add all libwiring function bindings.

Contact
-------

by jf.  

zaazbb <zaazbb@163.com>
