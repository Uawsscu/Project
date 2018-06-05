from firebase import firebase
from google.cloud import storage
firebase = firebase.FirebaseApplication('https://dogwood-terra-184417.firebaseio.com/', None)
client = storage.Client.from_service_account_json('C:\Users\MOJI\Downloads\dogwood-terra-184417-firebase-adminsdk-vy9o9-e8b71233d5.json')
bucket = client.get_bucket('dogwood-terra-184417.appspot.com')
blob = bucket.blob('8121cc95-36ce-405f-af9b-e67c8589242d.jpg')
blob.upload_from_filename(filename ='C:\Users\MOJI\Pictures\8121cc95-36ce-405f-af9b-e67c8589242d.jpg')
firebase.post('/object/data', {'object_Name':'aaaa','thumbnail':'https://firebasestorage.googleapis.com/v0/b/dogwood-terra-184417.appspot.com/o/'+'8121cc95-36ce-405f-af9b-e67c8589242d.jpg'+'?alt=media'})

