import os
import time

count = 0
# title of the software
print('_'.center(80, '_'))
print('SMART TABLE SOFTWARE'.center(80))
print('APPLIED PHYSICS AND COMPUTER SCIENCE :[ Y1S2 ]'.center(80))
print('\n', 'FULL_VERSION 1.0'.center(80))
print('_'.center(80, '_'))

# prints the current timestamp
print('\nTODAY::', time.ctime())
# the while loop is meant to exit the software after the user has accessed the course unit two times
while count < 8:
    count += 1
    time.sleep(1)
    time.clock()
    print('\n\n\n', '_'.center(76, '_'))
    Request_0 = input('\a\nPRESS 1-TO VIEW INSTRUCTIONS 2-TO GET SOFTWARE LICENSE 3-TO USE THE SOFTWARE :')
    if Request_0 == '3':
        try:
            os.chdir('C:\\Windows_bin\\bin')
            of_win_reg = open('win_reg.txt', 'r')
            of_win_reg.close()
        except Exception:
            print('\a\n', 'YOU NEED TO BE REGISTERED AND ISSUED WITH A LICENSE, TO USE THIS SOFTWARE!'.center(80))
        else:
            try:
                os.chdir('C:\\Windows_bin\\bin')
                of_filekey = open('key.txt', 'r')
                of_filekey.close()
            except Exception:
                # the user is prompted to input the Activation Key of the Software
                input_key = (input('\a\n\nEnter ACTIVATION KEY/ID :: ')).upper()
                print('\nPLEASE WAIT,AS THE ACTIVATION KEY IS BEING ANALYSED...')
                # 3 seconds for activation key analysation
                time.sleep(2)
                if input_key != 'G8H-2P3-01U-2017':
                    print('\a\n', 'ACCESS DENIED!'.center(80, '+'),
                          '\nACTIVATION KEY :', input_key, ' is INCORRECT!')
                else:
                    os.chdir('C:\\Windows_bin\\bin')
                    of_keyfile = open('key.txt', 'w')
                    of_keyfile.write('1')
                    of_keyfile.close()
                    print('ACCESS GRANTED!'.center(80, '+'))
            else:
                pswrd = input('\nPLEASE INPUT YOUR PASSWORD :: ')
                os.chdir('C:\\Windows_bin\\bin')
                of_pss = open('win_reg.txt', 'r')
                pss = of_pss.read()
                if pswrd == pss:
                    day = (input('\nEnter Day Of WEEK Here ::')).upper()
                    if day == 'MONDAY':
                        # prints out Monday Course Units Timetable
                        print('\n' + 'MONDAY COURSE UNITS'.center(80))
                        print('\nLESSON', '\t\tTIME', '\t\tROOM', '\t\tLECTURER', '\tFREE TIME')
                        print('MAT 2124(L)', '\t7AM-10AM', '\tLR5', '\t\tMR.Mutegi', '\t10AM-4PM(5HRS)')
                        print('UCU 2103(L)', '\t4PM-7PM', '\tLR5', '\t\t(UNKNOWN)')
                        input('\n\n' + 'PRESS ENTER'.center(80))
                        print('\nYou Have used :', time.clock(), ' Seconds To Use the Timetable Software')
                    elif day == 'TUESDAY':
                        # prints out Tuesday Course Units Timetable
                        print('\n' + 'TUESDAY COURSE UNITS'.center(80))
                        print('\nLESSON', '\t\tTIME', '\t\tROOM', '\t\tLECTURER', '\tFREE TIME')
                        print('PHY 2123(L)', '\t7AM-9AM', '\tSM1 RM2', '\tMR.Musyoki', '\t9AM-5PM(8HRS)')
                        print('ICS 2123(L)', '\t5PM-7PM', '\tLR5', '\t\tMr.Oyuu')
                        input('\n\n' + 'PRESS ENTER'.center(80))
                        print('\nYou Have used :', time.clock(), ' Seconds To Use the Timetable Software')
                    elif day == 'WEDNESDAY':
                        # prints out Wednesday Course Units Timetable
                        print('\n' + 'WEDNESDAY COURSE UNITS'.center(80))
                        print('\nLESSON', '\t\tTIME', '\t\tROOM', '\t\tLECTURER', '\tFREE TIME')
                        print('ICS 2123(PRAC)', '\t8AM-11AM', '\tMMLAB', '\t\tMR.Oyuu', '\t7AM-8AM(1HR)')
                        print('ICS 2124(PRAC)', '\t11AM-2PM', '\tMMLAB', '\t\t(UNKNOWN)')
                        print('ICS 2125(L)', '\t2PM-5PM', '\tLR5', '\t\t(UNKNOWN', '\t5PM-7PM(2HRS)')
                        input('\n\n' + 'PRESS ENTER'.center(80))
                        print('\nYou Have used :', time.clock(), ' Seconds To Use the Timetable Software')
                    elif day == 'THURSDAY':
                        # prints out Thursday Course Units Timetable
                        print('\n' + 'THURSDAY COURSE UNITS'.center(80))
                        print('\nLESSON', '\t\tTIME', '\t\tROOM', '\t\tLECTURER', '\tFREE TIME')
                        print('MAT 2123(L)', '\t10AM-2PM', '\tPHY LAB', '\tMR.Mocheche', '\t7AM-10AM(3HRS)')
                        print('PHY 2124(PRAC)', '\t2PM-5PM', '\tPHY LAB', '\tMRS.Thairu')
                        print('PHY 2124(L)', '\t5PM-7PM', '\tSM1 RM2', '\tMRS.Thairu')
                        input('\n\n' + 'PRESS ENTER'.center(80))
                        print('\nYou Have used :', time.clock(), ' Seconds To Use the Timetable Software')
                    elif day == 'FRIDAY':
                        # prints out Friday Course Units Timetable
                        print('\n' + 'FRIDAY COURSE UNITS'.center(80))
                        print('\nLESSON', '\t\tTIME', '\t\tROOM', '\t\tLECTURER', '\tFREE TIME')
                        print('ICS 2124(L)', '\t8AM-11AM', '\tLR5', '\t\t(UNKNOWN)', '\t7AM-8AM(1HR)')
                        print('PHY 2123(PRAC)', '\t11AM-2PM', '\tPHY LAB', '\tMR.Musyoki')
                        print('ICS 2125(PRAC)', '\t2PM-5PM', '\tMM LAB', '\t\t(UNKNOWN)', '\t5PM-7PM(2HRS)')
                        input('\n\n' + 'PRESS ENTER'.center(80))
                        print('\nYou Have used :', time.clock(), ' Seconds To Use the Timetable Software')
                    # Reminds the user that there are no lessons on saturday and sunday
                    elif day == 'SATURDAY':
                        print('\a\n' + 'THERE ARE NO LESSONS ON SATURDAY'.center(80))
                    elif day == 'SUNDAY':
                        print('\a\n' + 'THERE ARE NO LESSONS ON SUNDAY'.center(80))
                    else:
                        # shows the user what days to input incase his or her input day is not expected
                        print('\a\n' + 'THE DAY OF THE WEEK YOU HAVE ENTERED :' + day + ', IS UNDEFINED!')
                        print('IT IS EITHER:MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY')
                else:
                    # Ensures that the user has given the right Activation Key for the software to function
                    print('\aACCESS DENIED!'.center(80, '+'))
                    print('\aTHE PASSWORD : ', pswrd, ' IS INCORRECT!')
                    print('DO YOU WISH TO RECOVER YOUR PASSWORD?'.center(80))
                    choice = input('\nPRESS 1 TO RECOVER PASSWORD :: ')
                    if choice == '1':
                        os.chdir('C:\\Windows_bin\\lib')
                        of_sec_q = open('sec_qst.txt', 'r')
                        sec_qstn = of_sec_q.read()
                        of_sec_q.close()
                        os.chdir('C:\\Windows_bin\\bin')
                        of_pass = open('win_reg.txt', 'r')
                        r_pss = of_pass.read()
                        ans_sec = str((input('SECURITY QUESTION : WHAT\'S YOUR FAVOURITE TOWN ? : ')).upper())
                        if sec_qstn == ans_sec:
                            print('\nYOUR PASSWORD IS : ', r_pss)
                        else:
                            print('\nTHAT\'S NOT THE TOWN YOU REGISTERED WITH')
                    else:
                        print('ALRIGHT,NO PASSWORD RECOVERY SINCE YOU DIDN\'T PRESS 1')
    elif Request_0 == '1':
        # prints out the Guides and Instructions of Using the software
        print('\n\n\n', 'GUIDES AND INSTRUCTIONS OF USING THIS SOFTWARE'.center(80))
        print('\nA:: IT IS MEANT TO ASSIST STUDENTS IN THEIR DAILY LEARNING ACTIVITIES')
        print('B:: A LICENSE FROM MANUFACTURER IS NEEDED SO AS TO USE THIS SOFTWARE')
        print('C:: YOU WILL GET THE ACTIVATION KEY WHEN YOU REGISTER FOR THE LICENSE')
        print('C:: THIS IS NOT A VIRUS NOR SCUM,ITS FULLY ANALYSED BY THE MANUFACTURER')
        print('\n\n' + 'THANKS FOR CHOOSING SMART TABLE SOFTWARE!'.center(80))
        print('DESIGNED BY KIM GICHUNGE... AN APPLIED PHYSICS AND COMPUTER SCIENCE STUDENT'.center(80))
        print('\n\n' + 'NOW GET THE LICENSE TO USE THIS SOFTWARE!'.center(80))
    elif Request_0 == '2':
        print('\n\n' + 'KINDLY REGISTER HERE TO GET LICENSE AND ACTIVATION KEY'.center(80))


        def reg_win(name, adm, pswd, course, sec_qst):
            ln_pass = len(pswd)
            mx_nm = max(name)
            spt_nm = list(name)
            spt_crse = list(course)
            ln_crse = len(course)
            id_lcns = 'TB_' + str(ln_pass) + mx_nm + spt_crse[1] + '_' + str(ln_crse) + spt_nm[2] + '_' \
                      + spt_nm[0] + '_' + str(len(name)) + spt_crse[0]
            try:
                os.chdir('C:\\')
                os.mkdir('Windows_bin')
                os.chdir('Windows_bin')
                os.mkdir('bin')
                os.mkdir('lib')
                os.chdir('bin')
                of_reg = open('win_reg.txt', 'w')
                of_reg.write(pswd)
                os.chdir('C:\\Windows_bin\\lib')
                of_license = open('win_lcns.txt', 'w')
                of_license.write('SERIAL KEY::' + id_lcns + '\nCopyright (c) 2017 Gichunge Kim Softwares' +
                                 '\nAll Rights Reserved.' +
                                 '\n\nTHANKS ' + name +
                                 ' FOR CHOOSING SMART TABLE SOFTWARE' +
                                 '\nNAME:: ' + name +
                                 '\nADMISSION NO :: ' + adm +
                                 '\nCOURSE :: ' + course + '\nTIME OF SOFTWARE REGISTRATION :: ' + time.ctime() +
                                 '\nSOFTWARE ACTIVATION KEY/ID :: G8H-2P3-01U-2017\n\nCAUTION :YOU SHOULD KEEP THIS '
                                 'LICENSE INCASE THE TIMETABLE CHANGES, '
                                 '\nSHOW IT TO THE MANUFACTURER TO MAKE YOU A NEW UPDATED TIMETABLE\nMANUFACTURER '
                                 ':GICHUNGE KELVIN KIM\nCONTACTS :+254724097929')
                of_sec_qstn = open('sec_qst.txt', 'w')
                of_sec_qstn.write(sec_qst)
            except Exception:
                print('\n\n' + 'ERROR!: UNABLE TO CONNECT TO WINDOWS FILE SYSTEM'.center(80))
            else:
                os.chdir('C:\\')
                os.mkdir('SMART TABLE')
                os.chdir('SMART TABLE')
                of_user_lcns = open('License.txt', 'w')
                of_user_lcns.write('SERIAL CODE::' + id_lcns + '\nCopyright (c) 2017 Gichunge Kim Softwares' +
                                   '\nAll Rights Reserved.' +
                                   '\n' + '_'.center(80, '_') + '\n\nTHANKS ' + name +
                                   ' FOR CHOOSING SMART TABLE SOFTWARE\nNAME:: ' + name +
                                   '\nADMISSION NO :: ' + adm +
                                   '\nCOURSE :: ' + course + '\nTIME OF SOFTWARE REGISTRATION :: ' + time.ctime() +
                                   '\nSOFTWARE ACTIVATION KEY/ID :: G8H-2P3-01U-2017'
                                   '\n' + '_'.center(80, '_') +
                                   '\nCAUTION :YOU SHOULD KEEP THIS LICENSE INCASE THE TIMETABLE CHANGES, '
                                   '\nSHOW IT TO THE MANUFACTURER TO MAKE YOU A NEW UPDATED TIMETABLE'
                                   '\n\nWARNING :TAMPERING WITH THE LICENSE DETAILS OR CHANGING THE SERIAL KEY,'
                                   '\nIS AGAINST THE MANUFACTURER\'S GUIDE AND INSTRUCTIONS!'
                                   '\n' + '_'.center(80, '_') + '\nMANUFACTURER '
                                                                ':GICHUNGE KELVIN KIM\nFOR TECHNICAL ISSUES,CONTACT '
                                                                'US :+254724097929 '
                                                                '\nFIELD : APPLIED PHYSICS AND COMPUTER SCIENTIST'
                                                                '\n' + '_'.center(80, '_'))

                of_reg.close()
                of_license.close()
                of_user_lcns.close()
                of_sec_qstn.close()
                print('\n\n', 'YOU HAVE SUCCESSFULLY REGISTERED TO USE THIS SOFTWARE !'.center(80),
                      '\n', 'CHECK YOUR LICENCE AND ACTIVATION KEY IN'.center(80),
                      '\nLICENSE  FOLDER IN LOCAL DISK C:\ ON SMART TABLE FOLDER '.center(80))


        def register():
            os.chdir('C:\\')
            try:
                os.chdir('Windows_bin')
            except Exception:
                course = str((input('\nENTER YOUR FULL COURSE NAME :: ')).upper())
                full_nm = str((input('\nENTER YOUR FULL NAME :: ')).upper())
                if full_nm == '':
                    print('\a\nWE DID NOT FIND YOUR NAME!')
                else:
                    adm_no = str((input('\nENTER YOUR ADMISSION NO :: ')).upper())
                    if adm_no == '':
                        print('\a\nWE DID NOT FIND YOUR ADMISSION NUMBER!')
                    else:
                        pswrd0 = input('\nPLEASE SET YOUR PASSWORD :: ')
                        pssd = input('\nCONFIRM YOUR PASSWORD :: ')
                        if pswrd0 != pssd:
                            print('\n', 'YOUR SECOND PASSWORD CONFIRMATION WAS WRONG!'.center(80))
                        else:
                            print('\n', 'SECURITY QUESTION HELPS YOU TO RECOVER YOUR PASSWORD INCASE'
                                        ' YOU FORGET IT'.center(80))
                            security_q = str((input('\nSECURITY QUESTION: WHAT\'S YOUR FAVOURITE TOWN? : ')).upper())
                            reg_win(full_nm, adm_no, pssd, course, security_q)
            else:
                print('PLEASE WAIT FOR COMPONENTS ANALYSATION TO COMPLETE...')
                time.sleep(2)
                print('\n' + 'YOU ARE ALREADY REGISTERED  AND YOU WERE ISSUED WITH A LICENSE!'.center(80))


        register()
    if count == 8:
        # when the user accesses the course units for 8days consecutively,the software closes itself automatically
        print('\n\n' + 'YOU HAVE ACCESSED THE SOFTWARE TO THE MAXIMUM LIMIT SET TO HOLD ON YOUR RAM!'.center(80))
        print('\n' + 'KINDLY RESTART SMART TABLE TO USE IT AFRESH!'.center(80))
        print('EXITING THE SMART TABLE  SERVER...')
        # giving the Exit notification to the user for seven seconds to ensure console contents are read fully
        time.sleep(7)
        # THIS TIMETABLE SOFTWARE IS DESIGNED BY KELVIN GICHUNGE KIMATHI
        # Last Review of the Source-Code: FEB-19-2017 BY:GICHUNGE KELVIN
