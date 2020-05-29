import py_compile
import os

print("Current Working Directory " , os.getcwd())
#os.chdir("/Nicholas_Flask_Webserver/")
py_compile.compile("httpsrv_Nicholas.py")
