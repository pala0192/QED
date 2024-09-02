#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import cgi, os
form = cgi.FieldStorage()

time=form["time"].value
os.remove(time+'T/'+time+'T')

print("Location: update.py")
print()
