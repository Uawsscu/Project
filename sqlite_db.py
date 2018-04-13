
# coding: utf-8

# In[1]:


from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
import sqlite3
result = firebase.get('/action/data/',None)
result = list(result)

while (True):
    result1 = firebase.get('/update/',None)
    result2 = str(result1)
    if (result2!="None"):
        result1 = list(result1)
        for i in result1:
            result3 = firebase.get('/update/'+i,None)
            result4 = firebase.delete('/update/'+i,None)
            if(result3==1):
                with sqlite3.connect("db1.db") as con:
                        con.execute('delete from action;')
                for i in result :
                    result5 = firebase.get('/action/data/'+i,None)
                    name=firebase.get('/action/data/'+i,'action_name')
                    motor=firebase.get('/action/data/'+i,'motor')
                    motor = str(motor)
                    motor = motor[1:][:-1]
                    list = motor.split(",")
                    step =firebase.get('/action/data/'+i,'step')
                    with sqlite3.connect("db1.db") as con:
                        con.execute('insert into action values (?,?,?,?,?,?,?,?,?,?)',(name,step,list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7]))
    else :
            continue

