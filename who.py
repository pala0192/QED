#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import cgi
form = cgi.FieldStorage()
password=form["password"].value

if password=='1221':
    print("Location:update.py")
    print()
else:
    print("Location:index.py")
    print()