#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io
from datetime import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os

# file= os.listdir('databox')

# listStr = ''
# for item in file:
#     listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)



form = cgi.FieldStorage()

# file_list = []
# for files in file:
#   file_list.append(files)


# file_count_num=0
# file_num_and_list={}
# file_keys_list = []

# for file in file_list:
#   file_num_and_list[file]=file_count_num
#   file_keys_list.append(file)
#   file_count_num=file_count_num+1


# file_count_num=0
# file_num_and_list={}
# file_keys_list = []

# for file in file_list:
#   file_num_and_list[file]=file_count_num
#   file_keys_list.append(file)
#   file_count_num=file_count_num+1


# name_checklist=''
# a=0
# while a<file_count_num:
#   name=file_keys_list[a]
#   description = open('databox/'+name, 'r',encoding='utf-8').read()
#   name_checklist=name_checklist+'<li>{0}:{1}</li>'.format(name,description)
#   a=a+1

if os.path.isfile('1T/1T') :
  name1 = open('1T/1T', 'r',encoding='utf-8').read()
  sign_up1='''<p style="font-size:200%;margin-top:2%">09:40~10:00  {0}</p>'''.format(name1)
else: 
  sign_up1='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T1" style="font-size:200%">09:40~10:00</label>
        <input type="text" name="name" id="T1" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='1'>
        <input type="submit"  style="font-size:200%">
        </form>'''
        
if os.path.isfile('2T/2T') :
  name2 = open('2T/2T', 'r',encoding='utf-8').read()
  sign_up2='''<p style="font-size:200%;margin-top:2%">10:10~10:30  {0}</p>'''.format(name2)
else: 
  sign_up2='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T2" style="font-size:200%">10:10~10:30</label>
        <input type="text" name="name" id="T2" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='2'>
        <input type="submit"  style="font-size:200%">
        </form>'''

if os.path.isfile('3T/3T') :
  name3 = open('3T/3T', 'r',encoding='utf-8').read()
  sign_up3='''<p style="font-size:200%;margin-top:2%">10:40~11:00  {0}</p>'''.format(name3)
else: 
  sign_up3='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T3" style="font-size:200%">10:40~11:00</label>
        <input type="text" name="name" id="T3" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='3'>
        <input type="submit"  style="font-size:200%;">
        </form>'''

if os.path.isfile('4T/4T') :
  name4 = open('4T/4T', 'r',encoding='utf-8').read()
  sign_up4='''<p style="font-size:200%;margin-top:2%">11:10~11:30  {0}</p>'''.format(name4)
else: 
  sign_up4='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T4" style="font-size:200%">11:10~11:30</label>
        <input type="text" name="name" id="T4" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='4'>
        <input type="submit"  style="font-size:200%;">
        </form>'''
        
if os.path.isfile('5T/5T') :
  name5 = open('5T/5T', 'r',encoding='utf-8').read()
  sign_up5='''<p style="font-size:200%;margin-top:2%">11:40~12:00  {0}</p>'''.format(name5)
else: 
  sign_up5='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T5" style="font-size:200%">11:40~12:00</label>
        <input type="text" name="name" id="T5" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='5'>
        <input type="submit"  style="font-size:200%">
        </form>'''

if os.path.isfile('6T/6T') :
  name6 = open('6T/6T', 'r',encoding='utf-8').read()
  sign_up6='''<p style="font-size:200%;margin-top:2%">12:10~12:30  {0}</p>'''.format(name6)
else: 
  sign_up6='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T6" style="font-size:200%">12:10~12:30</label>
        <input type="text" name="name" id="T6" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='6'>
        <input type="submit"  style="font-size:200%">
        </form>'''
        
if os.path.isfile('7T/7T') :
  name7 = open('7T/7T', 'r',encoding='utf-8').read()
  sign_up7='''<p style="font-size:200%;margin-top:2%">12:40~13:00  {0}</p>'''.format(name7)
else: 
  sign_up7='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T7" style="font-size:200%">12:40~13:00</label>
        <input type="text" name="name" id="T7" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='7'>
        <input type="submit"  style="font-size:200%">
        </form>'''
        
if os.path.isfile('8T/8T') :
  name8 = open('8T/8T', 'r',encoding='utf-8').read()
  sign_up8='''<p style="font-size:200%;margin-top:2%">13:10~13:30  {0}</p>'''.format(name8)
else: 
  sign_up8='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T8" style="font-size:200%">13:10~13:30</label>
        <input type="text" name="name" id="T8" style="font-size:200%;display: inline;width:18%" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='8'>
        <input type="submit"  style="font-size:200%">
        </form>'''

if os.path.isfile('9T/9T') :
  name9 = open('9T/9T', 'r',encoding='utf-8').read()
  sign_up9='''<p style="font-size:200%;margin-top:2%">13:40~14:00  {0}</p>'''.format(name9)
else: 
  sign_up9='''<form action="process_create.py" style="margin-top:2%" method="post">
        <label for="T9" style="font-size:200%;">13:40~14:00</label>
        <input type="text" name="name" id="T9" style="font-size:200%;display: inline;width:18%;" placeholder="이름">
        <input type="tel" name="tel" style="font-size:200%;display:inline;width:20%" placeholder="전화번호">
        <input type="hidden" name="time" value='9'>
        <input type="submit"  style="font-size:200%">
        </form>'''



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
      <h3 style="font-size:350%;">부스 예약하기</h3>
      <p>(전화번호는 띄어쓰기없이 숫자만 해주세요. 잘못 입력시 예약 기회는 다른 사람에게 넘어갑니다.)</p>
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
    <br>
    <br>
    <br>
    <form action="who.py" method="post">
      <input type="text" name="password" style="width:30%; font-size:100%" placeholder="누르지마시오">
      <input type="submit" style="width:20%; font-size:100%">
    </form>
</body>
</html>
      '''.format(sign_up1=sign_up1,sign_up2=sign_up2,sign_up3=sign_up3,\
        sign_up4=sign_up4,sign_up5=sign_up5,sign_up6=sign_up6,\
          sign_up7=sign_up7,sign_up8=sign_up8,sign_up9=sign_up9))

