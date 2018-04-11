# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:24:36 2018

@author: MOJI
"""

import sqlite3
with sqlite3.connect("db1.db") as con:
    
    con.execute('insert into action values (?,?,?,?,?,?,?,?,?,?)',("bbb",1,11,22,33,44,55,66,77,88))
    
    



from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
import sqlite3
result = firebase.get('/action/data/',None)
#print result
result = list(result)

for i in result :
    result2 = firebase.get('/action/data/'+i,None)
    #print result2
    name=firebase.get('/action/data/'+i,'action_name')
    motor=firebase.get('/action/data/'+i,'motor')
    motor = str(motor)
    motor = motor[1:][:-1]
    list = motor.split(",")
    step =firebase.get('/action/data/'+i,'step')
    
    with sqlite3.connect("db1.db") as con:
            con.execute('insert into action values (?,?,?,?,?,?,?,?,?,?)',(name,step,list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7]))

            
            
            
            
            
            
            
            
            
            

from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
import sqlite3
#result = firebase.get('/action/data/',None)
#print result
#result = list(result)
while (True):
    result1 = firebase.get('/update/',None)
    result2 = str(result)
    if (result2!="None"):
        result = list(result1)
        #print result
        for i in result1:   
            #print result
            result3 = firebase.get('/update/'+i,None)
            #a=result2
            #result3 = firebase.delete('/STT/'+i,None)
            if(result3==1):
                print (result3)
    else :
            continue