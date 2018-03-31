from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)

while (True):
    result = firebase.get('/STT/',None)
    result4 = str(result)
    if (result4!="None"):
        result = list(result)
        #print result
        for i in result:   
            #print result
            result2 = firebase.get('/STT/'+i,None)
            a=result2
            #result3 = firebase.delete('/STT/'+i,None)
            print (a)
    else :
            continue
        
        
        
from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
result = firebase.get('/STT/',None)
#print result
result = list(result)

for i in result :
    print (result)
    result2 = firebase.get('/STT/'+i,None)
    a=result2
    #result3 = firebase.delete('/STT/'+i,None)
    print (a)
    
