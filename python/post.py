
from firebase import firebase
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
add = firebase.post('/action/data', {'action_name': 'Tong','motor':'(1,2,3,4,5,6,7,8)','step':'1'})