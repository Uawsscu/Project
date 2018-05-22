from firebase import firebase
import requests
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
result = firebase.get('/object/data/',None)
#print result
result = list(result)
for i in result :
    name=firebase.get('/object/data/'+i,'object_Name')
    url = firebase.get('/object/data/'+i,'thumbnail')
    #print url
    r = requests.get(url)
    with open('C:\\Users\\MOJI\\Downloads\\'+name+'.jpg', 'wb') as f:  
        f.write(r.content)


