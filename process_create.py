#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import cgi
form = cgi.FieldStorage()
name=form["name"].value
time=form["time"].value
tel=form["tel"].value
if time=='1':
    opened_file=open('1T/1T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='2':
    opened_file=open('2T/2T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='3':
    opened_file=open('3T/3T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='4':
    opened_file=open('4T/4T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='5':
    opened_file=open('5T/5T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='6':
    opened_file=open('6T/6T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='7':
    opened_file=open('7T/7T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='8':
    opened_file=open('8T/8T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()
elif time=='9':
    opened_file=open('9T/9T','w',encoding='utf-8')
    opened_file.write(name+'님: '+tel)
    opened_file.close()
    print("Location: index.py")
    print()