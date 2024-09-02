#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

file= os.listdir('databox')

listStr = ''
for item in file:
        listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)


form = cgi.FieldStorage()

from datetime import datetime

now = datetime.now()

file_list = []
for files in file:
  file_list.append(files)

file_count_num=0
file_num_and_list={}
file_keys_list = []

for file in file_list:
  file_num_and_list[file]=file_count_num
  file_keys_list.append(file)
  file_count_num=file_count_num+1

name_checklist=''
a=0
while a<file_count_num:
  name=file_keys_list[a]
  description = open('databox/'+name, 'r',encoding='utf-8').read()
  name_checklist=name_checklist+'<li>{0}:{1}</li>'.format(name,description)
  a=a+1


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
    
    <br>
    <br>
    <form action="process_create.py" id="process_create" method="post">
        <p><input type="text" name="title" style="width:90%; font-size:280%" placeholder="이름">
        </p>
        <p><input type="number" name="member_num" style="width:90%; font-size:280%" placeholder="총 인원">
        </p>
        <input type="hidden" name="check" value="예약 ">
        <input type="hidden" name="now_hour" value="{hour}">
        <input type="hidden" name="now_minute" value="{minute}">
        <p><input type="submit"  style="width:90%; font-size:280%"></p>
    </form>
    
    <div style="border:black solid 1px; padding:3%">
        <h3 style="font-size:300%;">신청자 목록</h3>
        <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <br>
</body>
</html>
    '''.format(listStr=name_checklist,hour=now.hour,minute=now.minute))
            