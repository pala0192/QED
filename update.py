#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

form = cgi.FieldStorage()

if os.path.isfile('1T/1T') :
  name1 = open('1T/1T', 'r',encoding='utf-8').read()
  sign_up1='''<p style="font-size:200%;margin-top:2%;">09:40~10:00  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="1">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name1)
else: 
  sign_up1='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''
        
if os.path.isfile('2T/2T') :
  name2 = open('2T/2T', 'r',encoding='utf-8').read()
  sign_up2='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="2">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name2)
else: 
  sign_up2='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''

if os.path.isfile('3T/3T') :
  name3 = open('3T/3T', 'r',encoding='utf-8').read()
  sign_up3='''<p style="font-size:200%;margin-top:2%;">10:40~11:00  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="3">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name3)
else: 
  sign_up3='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''

if os.path.isfile('4T/4T') :
  name4 = open('4T/4T', 'r',encoding='utf-8').read()
  sign_up4='''<p style="font-size:200%;margin-top:2%;">11:10~11:30  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="4">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name4)
else: 
  sign_up4='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''
        
if os.path.isfile('5T/5T') :
  name5 = open('5T/5T', 'r',encoding='utf-8').read()
  sign_up5='''<p style="font-size:200%;margin-top:2%;">11:40~12:00  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="5">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name5)
else: 
  sign_up5='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''
if os.path.isfile('6T/6T') :
  name6 = open('6T/6T', 'r',encoding='utf-8').read()
  sign_up6='''<p style="font-size:200%;margin-top:2%;">12:10~12:30  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="6">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name6)
else: 
  sign_up6='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''        
if os.path.isfile('7T/7T') :
  name7 = open('7T/7T', 'r',encoding='utf-8').read()
  sign_up7='''<p style="font-size:200%;margin-top:2%;">12:40~13:00  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="7">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name7)
else: 
  sign_up7='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''        
if os.path.isfile('8T/8T') :
  name8 = open('8T/8T', 'r',encoding='utf-8').read()
  sign_up8='''<p style="font-size:200%;margin-top:2%;">13:10~13:30  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="8">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name8)
else: 
  sign_up8='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''
if os.path.isfile('9T/9T') :
  name9 = open('9T/9T', 'r',encoding='utf-8').read()
  sign_up9='''<p style="font-size:200%;margin-top:2%;">13:40~14:00  {0}</p>
    <form action="process_delete.py" method="post">
        
        <input type="hidden" name="time" value="9">
        <input type="submit" value="delete" style="width:8%; height:40px; font-size:130%">
    </form>'''.format(name9)
else: 
  sign_up9='''<p style="font-size:200%;margin-top:2%;">10:10~10:30  No Reservation</p>'''



print('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hanmin wiki making practice</title>
  <link rel="stylesheet" href="front.css">
</head>

<body>
    
    <div style="margin:12%; background-color: rgb(151, 64, 64);;">
      <h1 style="text-align: center;"><a href="index.py"><span style="color:rgb(87, 122, 205);font-size:280%">Q.E.D</span>
      <span style="color:rgb(139, 83, 236);font-size:260%">방탈출 부스 예약 웹</span></a></h1>
    </div>
    
    <div style="border:black solid 1px; padding:3%">
      <h3 style="font-size:350%;">신청자 목록</h3>
      {sign_up1}
      {sign_up2}
      {sign_up3}
      {sign_up4}
      {sign_up5}
      {sign_up6}
      {sign_up7}
      {sign_up8}
      {sign_up9}
    </div>
    <br>
    <br>
    <br>
    <a href='index.py' style="font-size:300%">back</a>
</body>
</html>
      '''.format(sign_up1=sign_up1,sign_up2=sign_up2,sign_up3=sign_up3,\
        sign_up4=sign_up4,sign_up5=sign_up5,sign_up6=sign_up6,\
          sign_up7=sign_up7,sign_up8=sign_up8,sign_up9=sign_up9))

