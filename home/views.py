from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import psycopg2
from datetime import datetime
from .models import load

# Create your views here.
def home(request):
    data=fetch()
    #data={"hi":"usre"}
    return render(request,'home.html',data)
def fetch():
    conn = psycopg2.connect(   database="scrumdb", user='postgres', password='123qwe', host='localhost', port= '5432'   )
    cursor = conn.cursor()
    q1="select * from home_load WHERE STATUS = 'working'"
    q2="select * from home_load WHERE STATUS = 'workpool'"
    q3="select * from home_load where status = 'finished'"
    cursor.execute(q1)
    working=cursor.fetchall()
    working=parserow(working)
    cursor.execute(q2)
    workpool=cursor.fetchall()
    workpool=parserow(workpool)
    cursor.execute(q3)
    finished=cursor.fetchall()
    finished=parserow(finished)
    return  { "working":working,  "workpool":workpool , "finished":finished }

def parserow(row):
    ls=[]
    for i in row:
        ls.append({'task':i[0],'priority':i[1] })
    return ls
def load(request):
    task=request.POST['task']
    priority=request.POST['priority']
    conn = psycopg2.connect(   database="scrumdb", user='postgres', password='123qwe', host='localhost', port= '5432'   )
    cursor = conn.cursor()
    qurey="insert into home_load values('" +task+ "','" +priority+ "','workpool','" +str(datetime.now())+ "')"
    cursor.execute(qurey)    
    conn.commit()
    cursor.close()
    conn.close()
    data=fetch()
    #data={"hi":"usre"}
    return render(request,'home.html',data)

def alt(request):
    task=request.POST['task']
    mode=request.POST['mode']
    conn = psycopg2.connect(   database="scrumdb", user='postgres', password='123qwe', host='localhost', port= '5432'   )
    cursor = conn.cursor()
    print("hi")
    qurey="update home_load set status='"+mode+"' where task = '"+task+"'"
    cursor.execute(qurey)    
    conn.commit()
    cursor.close()
    conn.close()
    data=fetch()
    #data={"hi":"usre"}
    #return render(request,'home.html',data)
    return HttpResponseRedirect("home")