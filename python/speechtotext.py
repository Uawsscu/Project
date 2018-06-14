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
            strDecode=result2
            #result3 = firebase.delete('/STT/'+i,None)
            print (strDecode)
            if strDecode == 'merry one' :
                            print "..."
                           # talker2("-1")

                        if JOB == True and strDecode[-3:] == 'end' and strDecode[:9] == "this is a":
                            JOB = False
                            TRAIN = True
                            print "\n--------------------this is a----------------------"

                            ST = strDecode[9:]
                            print "Do you want to train", ST, "image (yes or no)"
                            ST = "Do you want to train" + ST + " image"
                            espeak.synth(ST)
                            time.sleep(4)
                            obj_name = get_object_train(strDecode)  # sentence to word

                        elif TRAIN == True and strDecode == "yes" :
                            espeak.synth("ok,Please rotate the object. When i say continue")
                            time.sleep(7)
                            print "Speech : ", obj_name
                            # create folder
                            dataset_Path = r'/home/kns/PycharmProjects/Aj/AJ2/pic/' + obj_name
                            p = PATH + "/pic/" + obj_name + "/"

                            if not os.path.exists(dataset_Path):
                                print "New Data"
                                os.makedirs(dataset_Path)
                                capture(p, obj_name, 1)  # capture image for train >> SAVE IMAGE
                                lenObj = int(lenDB("Corpus_Main.db", "SELECT * FROM obj_ALL2"))  # count ROWs
                                insert_object_Train2(obj_name, int(lenObj + 1))  # check Found objects?
                            else:
                                count = int(search_count_Train2(obj_name))
                                capture(p, obj_name, count + 1)  ####cap2
                                update_object_Train2(count + 1, obj_name)  # UPDATE COUNT++

                            JOB = True
                            TRAIN = False
                            print "OK "
                            espeak.synth("OK")
                            time.sleep(2)

                            print "\n------------------------------------------"

                        elif TRAIN == True and strDecode == "no":
                            print obj_name
                            JOB = True
                            TRAIN = False
                            print "\n------------------------------------------"



                        # >>>>>>> JERRY <<<<<<<<<<<<

                        elif JERRY==True and JOB == True and strDecode[:5] == 'jerry':
                            Jsubject = strDecode
                            JOB = False
                            JERRY = False
                            print "\n---------------------jerry---------------------"
                            print '\nStream decoding result:', strDecode
                            obj_name = get_objectJerry(strDecode)
                            ST = strDecode[5:]
                            print "Do you want to", ST, " (yes or no)"
                            ST = "Do you want to" + ST
                            espeak.synth(ST)
                            time.sleep(4)

                        elif JERRY == False and strDecode == "yes" :
                            keep_First_Home()
                            obj_find = str(search_object_Train(obj_name))  # KNOW
                            print "obj_find"
                            v = get_V(Jsubject)
                            print obj_name, " ", v
                            # sert name
                            check1 = 0

                            with sqlite3.connect("Test_PJ2.db") as con:
                                cur1 = con.cursor()
                                cur1.execute(
                                    'Select ID from ActionName where Name = ?', (v,))
                                row1 = cur1.fetchall()
                                for i in row1:
                                    check1 = check1 + 1

                            if obj_find != "None" and check1 != 0:
                                detectBOW4(obj_name)
                                time.sleep(2)

                                print obj_name, " and ", v
                                center1 = str(search_callDetect(obj_name))
                                print ">>> call", center1

                                if (center1 != "None"):
                                    center1 = int(center1)
                                    if center1 > 50 and center1 < 100:
                                        Contorl_Basic_FGB(v)
                                        print"contorl_Basic"
                                    elif center1 <= 65 :
                                        print "center Left!!!"
                                    else :
                                        Control_Basic_Move(v, center1)
                                        print"contorl_Move"

                                if center1 == "None" :
                                    print "I can not see it..............................1"
                                    checkLeft() # CHECK TO The LEFT @ Roll LEFT
                                    time.sleep(2)
                                    talker2("Forward2000")
                                    time.sleep(2)
                                    detectBOW4(obj_name)
                                    talker2("Backward2000")
                                    time.sleep(2)

                                    center1 = str(search_callDetect(obj_name))
                                    print obj_name, " and ", v, " ", center1

                                    if (center1 != "None"):
                                        goToLeft()  # @ TO The LEFT
                                        time.sleep(17)
                                        detectBOW4(obj_name) #Detect

                                        center1 = str(search_callDetect(obj_name))
                                        center1 = int(center1)
                                        if center1 > 50 and center1 < 100:
                                            Contorl_Basic_FGB(v)
                                        elif center1 <= 65:
                                            print "center Left!!!"
                                        else:

                                            Control_Basic_Move(v, center1)

                                    if center1 == "None":
                                        print "I can not see it...........................2" #### if not @ Back <---
                                        talker2("turnRight45") # @ TO Mid , Roll Right
                                        time.sleep(2)
                                        checkRight()  # CHECK TO The Right @ Roll Right
                                        time.sleep(2)

                                        j = 1
                                        talker2("Forward2000")
                                        time.sleep(2)
                                        detectBOW4(obj_name)
                                        talker2("Backward2000")
                                        time.sleep(2)
                                        center1 = str(search_callDetect(obj_name))
                                        print obj_name, " and ", v, " ", center1

                                        if (center1 != "None"):
                                            goToRight()  # @ TO The Right
                                            time.sleep(17)
                                            detectBOW4(obj_name)

                                            center1 = str(search_callDetect(obj_name))
                                            center1 = int(center1)
                                            if center1 > 50 and center1 < 100:
                                                print "Basic >>"
                                                Contorl_Basic_FGB(v)
                                            elif center1 <= 65:
                                                print "center Left!!!"
                                            else:
                                                print "Move >>"
                                                Control_Basic_Move(v, center1)

                                        if center1 == "None":
                                            print "I can not see it"  #### if not @ Back <---
                                            talker2("turnLeft45")  # @ TO Mid , Roll Left
                                            time.sleep(2)

                                    

                            print "\n------------------------------------------"
                            JOB = True
                            JERRY = True

                        elif JERRY == False and strDecode == "no":
                            keep_First_Home()
                            espeak.synth("ok no")
                            time.sleep(2)
                            print "ok no"
                            print "\n------------------------------------------"
                            JOB = True
                            JERRY = True


                        # >>>>>>> ARM <<<<<<<<<<<<
                        elif check_Go == False and JOB == True and strDecode[:14] == 'this is how to':
                            JOB = False
                            print "\n------------------------------------------"
                            print '\nStream decoding result:', strDecode
                            STPname = get_V(strDecode)  # grab
                            check = 0


                            with sqlite3.connect("Test_PJ2.db") as con:
                                cur1 = con.cursor()
                                cur1.execute(
                                    'Select ID from ActionName where Name = ?', (STPname,))
                                row1 = cur1.fetchall()
                                for i in row1:
                                    check = check + 1
                            if (check != 0):
                                check_Go = True

                                #keep_First_Home()

                                print "Do you want to save?" + "look : " + STPname
                                espeak.synth("Do you want to save?")
                                time.sleep(1)

                            else:

                                #keep_First_Home()

                                insert_name()

                                print " check=0 , please say next. If you want to teach me"
                                espeak.synth("OK , please say next. If you want to teach me")
                                time.sleep(2)
                                JOB_HowTo_Open = True


                        elif check_Go == True and strDecode == "yes let go":

                            print " OK , please say next. If you want to teach me"
                            espeak.synth("OK , please say next. If you want to teach me")
                            time.sleep(2)
                            talker2("Deflut")
                            time.sleep(2)
                            talker2("Forward")
                            time.sleep(2)
                            JOB_HowTo_Open = True
                            check_Go = False

                        elif check_Go == True and strDecode == "no":
                            print "OK stop"
                            espeak.synth("OK stop it")
                            time.sleep(2)

                            check_Go = False
                            JOB_HowTo_Open = False
                            JOB = True


                        elif JOB_HowTo_Open == True and strDecode == 'next':
                            JOB = False
                            print 'Stream decoding result:', strDecode
                            STPindex += 1
                            print STPindex, " : ", STPname

                            #send(1)

                            sendCmd2(1)

                            # SAVE Action
                        elif JOB_HowTo_Open == True and strDecode == 'stop call back':
                            JJOB = False
                            JOB_HowTo_Open = False
                            STPindex = 0
                            JOB_SAVE = True
                            print "STOP.. Do you want to save? ..."
                            espeak.synth("Do you want to save?")
                            time.sleep(1)
                            talker2("Backward")
                            time.sleep(2)

                        elif JOB_SAVE == True and strDecode == 'yes':

                            with sqlite3.connect("Test_PJ2.db") as con:
                                cur2 = con.cursor()
                                cur2.execute('select ID from ActionName where Name = ?', (STPname,))
                                row = cur2.fetchone()
                                for element11 in row:
                                    id1 = int(element11)

                                    cur3 = con.cursor()
                                    cur3.execute('delete from Action_Robot where ID = ?', (id1,))

                            list1 = []
                            for i in select_Buffer():
                                list1.append(selectID_AcName(STPname))
                                for x in i:
                                    print(x, "...")
                                    list1.append(x)
                                with sqlite3.connect("Test_PJ2.db") as con:
                                    cur4 = con.cursor()
                                    cur4.execute(
                                        'insert into Action_Robot (ID,StepAction,M1,M2,M3,M4,M5,M6,M7,M8) values (?,?,?,?,?,?,?,?,?,?)',
                                        (list1))
                                    print(list1)
                                    del list1[:]

                            del_buff()

                            print "SAVE action !"
                            JOB = True
                            JOB_SAVE = False
                            print "\n------------------------------------------"

                        elif JOB_SAVE == True and strDecode == 'no':
                            print "del buff"
                            print "OK No!"
                            espeak.synth("Ok, No")
                            time.sleep(2)
                            del_buff()
                            JOB_SAVE = False
                            JOB = True
                            print "\n------------------------------------------"


                        # >>>>>>> PASS DO YOU KNOW~??? <<<<<<<<<<<<
                        elif JOB == True and strDecode[:11] == 'do you know':
                            JOB = False
                            print "\n--------------------do you know----------------------"
                            print '\nStream decoding result:', strDecode
                            obj_name = get_object_question(strDecode)
                            print(obj_name)
                            obj_find = search_object_Train(obj_name)
                            status = search_status(obj_name)


                            if obj_find != "None" and status == "yes" :

                                print "Yes , I know!"
                                espeak.synth("Yes, I know")
                                time.sleep(4)

                            else:
                                print "No , I don't know!"
                                espeak.synth("No , I don't know!")
                                time.sleep(4)
                            print "\n------------------------------------------"
                            JOB = True

                        elif TRAIN_DATA_SET == True and JOB == True and strDecode == "training data set":
                            JOB=False
                            TRAIN_DATA_SET = False
                            print "\n-------------------training data set-----------------------"
                            print "Do you want to save model? (yes or no)"
                            espeak.synth("Do you want to save model?")
                            time.sleep(5)

                        elif TRAIN_DATA_SET == False and strDecode == "yes":
                            print "! training data set"
                            espeak.synth("Just a moment, please.")
                            time.sleep(4)
                            save_model()
                            espeak.synth("OK, finish")
                            time.sleep(3)
                            JOB = True
                            TRAIN_DATA_SET = True
                            print "\n------------------------------------------"

                        elif TRAIN_DATA_SET == False and strDecode == "No":
                            print "OK No!"
                            espeak.synth("Ok, No")
                            time.sleep(2)
                            JOB = True
                            TRAIN_DATA_SET = True
                            print "\n------------------------------------------"
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
    
