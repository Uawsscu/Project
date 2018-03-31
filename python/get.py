
from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
result = firebase.get('/action/data/',None)
print result
result = list(result)

for i in result :
    result2 = firebase.get('/action/data/'+i,None)
    print result2
    name=firebase.get('/action/data/'+i,'action_name')
    print name
    if(str(name) == 'grab ball'):
        motor=firebase.get('/action/data/'+i,'motor')
        print motor
    