#code made by Dhiyanesh for CS project 2023 - Arranxo

import csv
import random
import pandas as pd

global Input_Data

Input_Data = pd.read_csv('original.csv')
Output_Data_Lines = pd.read_csv('edit.csv')

datafile = open("original.csv")
datareader = csv.reader(datafile)

def rolls_to_pair(dictpair, F1):
    key_list = list(dictpair.keys())
    val_list = list(dictpair.values())
    position = key_list.index(str(F1))


    return int(val_list[position])

def value_checker(listofcorrect,askthis,errorname = "ERROR: Please Enter Valid Input"):
    temprun = True
    while temprun == True:
        check = input(askthis)
        if check in listofcorrect:
            return check
        else:
            print(errorname)

def make_sheets_groups(Input_Data):
    global Data_Average_Marks_Descending
    global Data_Average_Marks_Increasing
    global Roll_Number_List_Descending
    global Roll_Number_List_Increasing
    global Marks_Increasing
    global Marks_Descending
    global ifile
    global dfile

    if extra > 0:
        for i in range(0,extra):
            Input_Data = Input_Data.drop(Input_Data.index[-1])

    Data_Average_Marks_Descending = Input_Data.sort_values('AM', ascending=False)
    Data_Average_Marks_Increasing = Input_Data.sort_values('AM', ascending=True)

    Data_Average_Marks_Descending.to_csv("data descending.csv", index=False)
    Data_Average_Marks_Increasing.to_csv("data increasing.csv", index=False)

    ifile = open("data increasing.csv")
    dfile = open("data descending.csv")

    Roll_Number_List_Descending = Data_Average_Marks_Descending['Roll'].tolist()
    Roll_Number_List_Increasing = Data_Average_Marks_Increasing['Roll'].tolist()

    Marks_Increasing = Roll_Number_List_Increasing
    Marks_Descending = Roll_Number_List_Descending

def Cloning(li1):
    li_copy = li1[:]
    return li_copy

def ask():
    global STUDENTS_FINAL
    global TYPE
    global datareader
    global friends
    STUDENTS_FINAL = len(list(datareader))
    STUDENTS_FINAL -= 1
    print(STUDENTS_FINAL)
    friends = int(input("How many friends per student: "))
    TYPE = value_checker(['g','G','l','L'],"Groups or Lines(G/L): ")

def groups():
    global STUDENTS_FINAL
    global STUDENTS
    global students
    global groups
    global extra

    x = 0

    i = 0

    DECIDE = value_checker(['g','G','s','S'], "Would you like to enter number of Students per groups or number of Groups(S/G): ")

    if DECIDE == "G" or DECIDE == "g":
        while x == 0:
            groups = int(input("Number of Groups: "))
            extra = STUDENTS_FINAL % groups
            STUDENTS = STUDENTS_FINAL - extra
            students = int(STUDENTS / groups)

            if extra > 0:
                if students > 6:
                    print("Please enter higher number of groups.")
                elif students < 3:
                    print("Please enter lower number of groups.")
                else:
                    x = 1
            else:
                if students > 7:
                    print("Please enter higher number of groups.")
                elif students < 3:
                    print("Please enter lower number of groups.")
                else:
                    x = 1

        i = 1

    elif DECIDE == "S" or DECIDE == "s":
        while x == 0:
            students = int(input("Number of Students per Groups: "))
            extra = STUDENTS_FINAL % students
            STUDENTS = STUDENTS_FINAL - extra
            groups = int(STUDENTS / students)

            if extra > 0:
                if students > 6:
                    print("Please enter lower number of students.")
                elif students < 3:
                    print("Please enter higher number of students.")
                else:
                    x = 1
            else:
                if students > 7:
                    print("Please enter lower number of students.")
                elif students < 3:
                    print("Please enter higher number of students.")
                else:
                    x = 1

    print("Number of groups is", groups, "and students per groups is", students, "with", extra, "groups having 1 extra student.")

def lines():
    global STUDENTS_FINAL
    global STUDENTS
    global students
    global groups
    global extra
    global friends

    global columns
    global rows

    if STUDENTS_FINAL % 2 == 1:
        extra = 1
        STUDENTS = (STUDENTS_FINAL - 1)//2
    else:
        extra = 0
        STUDENTS = (STUDENTS_FINAL)//2

    groups = 1

    students = STUDENTS_FINAL//2

    columns = int(input("How many colums can the class occupy?(No. of pairs)"))

    extrarow = students%columns
    a = students - extrarow
    global rows
    rows = int(a/columns)
    if extrarow != 0:
        if columns/extrarow < 2:
            rows += 1

    friends = friends*2

    print("Class will contain", columns, "columns with", rows, "rows having", extrarow, "columns with 1 extra pair.")

def pairing_lines():

    global Data_Average_Marks_Descending
    global Roll_Number_List_Descending
    global Input_Data
    global listofpairpair
    global listofstudentspair

    Index_Value = 0
    Pair_Number = 1

    templist = Cloning(Roll_Number_List_Increasing)

    headerlist = ["Roll","Name","AM","F1","F2","F3","F4","F5","F6","F7","F8","B"]

    dictpair = {}
    
    while templist!=[]:
        for Roll in range(1, students+1):
            S1 = templist.pop(0)
            S2 = templist.pop(-1)
            for i in range(1, friends+1):
                F1 = "F" + str((2*i)-1)
                F2 = "F" + str(2*i)
            F1, F2 = Input_Data.iloc[S1 - 1, 3], Input_Data.iloc[S2 - 1, 3]
            F3, F4 = Input_Data.iloc[S1 - 1, 4], Input_Data.iloc[S2 - 1, 4]
            F5, F6 = Input_Data.iloc[S1 - 1, 5], Input_Data.iloc[S2 - 1, 5]
            F7, F8 = Input_Data.iloc[S1 - 1, 6], Input_Data.iloc[S2 - 1, 6]
            dictpair[str(S1)] = str(Roll)
            dictpair[str(S2)] = str(Roll)
            B = (Input_Data.iloc[S1 - 1, 7] + Input_Data.iloc[S2 - 1, 7]) // 2
            Name = "Pair" + str(Roll)
            AM = (Input_Data.iloc[S1 - 1, 2] + Input_Data.iloc[S2 - 1, 2]) // 2
            Index_Value = Index_Value + 1
            Pair_Number = Pair_Number + 1

    templist = Cloning(Roll_Number_List_Increasing)

    while templist!=[]:
        for Roll in range(1, students+1):
            S1 = templist.pop(0)
            S2 = templist.pop(-1)
            F1, F2 = Input_Data.iloc[S1 - 1, 3], Input_Data.iloc[S2 - 1, 3]
            F3, F4 = Input_Data.iloc[S1 - 1, 4], Input_Data.iloc[S2 - 1, 4]
            F5, F6 = Input_Data.iloc[S1 - 1, 5], Input_Data.iloc[S2 - 1, 5]
            F7, F8 = Input_Data.iloc[S1 - 1, 6], Input_Data.iloc[S2 - 1, 6]
            F1 = rolls_to_pair(dictpair, F1)
            F2 = rolls_to_pair(dictpair, F2)
            F3 = rolls_to_pair(dictpair, F3)
            F4 = rolls_to_pair(dictpair, F4)
            F5 = rolls_to_pair(dictpair, F5)
            F6 = rolls_to_pair(dictpair, F6)
            F7 = rolls_to_pair(dictpair, F7)
            F8 = rolls_to_pair(dictpair, F8)
            B = (Input_Data.iloc[S1 - 1, 7] + Input_Data.iloc[S2 - 1, 7]) // 2
            Name = "Pair" + str(Roll)
            AM = (Input_Data.iloc[S1 - 1, 2] + Input_Data.iloc[S2 - 1, 2]) // 2
            Output_Data_Lines.loc[Index_Value] = [Roll,Name,AM,F1,F2,F3,F4,F5,F6,F7,F8,B]
            Index_Value = Index_Value + 1
            Pair_Number = Pair_Number + 1

    Output_Data_Lines.to_csv("data.csv", header=headerlist, index=False)
    Input_Data = pd.read_csv("data.csv")

    listofstudentspair = list(dictpair.keys())
    listofpairpair = list(dictpair.values())

def variable_maker():
    global groups
    global avg
    for i in range (1, groups + 1):
        i = str(i)
        x = "grp" + str(i)
        globals() [x] = []
    
    avg = []
    for i in range(1,students + 1 ):
        a = "rank" + str(i)
        avg.append(a)

def pairing_groups():
    global Roll_Number_List_Increasing
    global groups

    templist = Cloning(Roll_Number_List_Increasing)

    while templist!=[]:
        for i in range (1, (groups+1)):
            x = "grp"
            i = str(i)
            x += i
            globals() [x].append(templist.pop())
    for i in range (1, (groups+1)):
        x = "grp"
        i = str(i)
        x += i    
        globals() [x].reverse()

def conversion(tup, dict):
    for x, y in tup:
        dict[x] = y
    return dict

def friends_finder():
    global friends
    global listofrows
    global listforfriends

    listofrows = list(csv.reader(ifile, delimiter=","))
    listofrows.pop(0)

    for i in listofrows:
        a = int(i[0])
        dict = {}
        for j in range(3, friends+3):
            b = int(float(i[j]))
            for k in listofrows:
                if int(k[0]) == b:
                    for l in range(3, friends+3):
                        if int(float(k[l])) == a:
                            dict[b] = l - 2
        value = "dict"
        value += str(a)
        globals() [value] = dict

    matchs = {}
    for i in range(1, STUDENTS+1):
        test = "dict" + str(i)
        temp = globals() [test]
        matchs[str(i)] = len(temp.keys())

    dictmatchs = {}
    matchstup = sorted(matchs.items(), key=lambda x:x[1])
    conversion(matchstup, dictmatchs)

    listforfriends = list(dictmatchs.keys())

def rank_groups():
    global Roll_Number_List_Descending
    global groups
    global students

    templist = Cloning(Roll_Number_List_Descending)

    for i in range(1, students+1):
        a = "rank" + str(i)
        globals() [a] = []
        for j in range(1, groups+1):
            globals() [a].append(templist.pop())

def trail():
    a = Cloning(listforfriends)
    VALUE = int(a[0])
    l = True

    while l == True:
        xyz = 0
        for G in range(1, groups+1):
            VALUE = int(a[0])
            RANKS = Cloning(avg)
            GROUPS = "grp" + str(G)
            globals() [GROUPS] = []
            while len(globals() [GROUPS]) < students:
                while len(globals() [GROUPS]) < students:
                    for STUD in range(1, students+1):
                        d = "rank" + str(STUD)
                        RANK = globals() [d]
                        if VALUE in RANK:
                            break
                    if VALUE in RANK:
                        DICT = "dict" + str(VALUE) 
                        if d in RANKS:
                            RANK.remove(VALUE)
                            RANKS.remove(d)
                            e = len(globals() [GROUPS])
                            if e < students - 1:
                                globals() [GROUPS].append(VALUE)
                                a.remove(str(VALUE))
                                temp = min(globals() [DICT].values())
                                res = [key for key in globals() [DICT] if globals() [DICT][key] == temp]
                                k = True
                                xyz = 0
                                while k == True:
                                    for g in res:
                                        g = int(g)
                                        for h in RANKS:
                                            for j in globals() [h]:
                                                if j == g:
                                                    VALUE = j
                                                    k = False
                                                    l = False
                                                elif (6-G)*(len(res))*(len(RANKS)) < xyz:
                                                    d = random.choice(RANKS)
                                                    VALUE = random.choice(globals() [d])
                                                    xyz = 0
                                                    break
                                                else:
                                                    xyz += 1
                                            else:
                                                continue
                                            break
                                        else:
                                            continue
                                        break    
                                    else:
                                        continue
                                    break
                                else:
                                    continue
                                break                
                            else:
                                globals() [GROUPS].append(VALUE)
                                a.remove(str(VALUE))
                        else:
                            d = random.choice(RANKS)
                            VALUE = random.choice(globals() [d])

def print_groups():
    global groups
    global avg
    for i in range (1, groups + 1):
        i = str(i)
        x = "grp" + str(i)
        print(globals() [x])

def extra_placer():
    global extra
    global STUDENTS_FINAL
    global STUDENTS
    global listofrowsnoorder

    with open('data.csv', 'r') as read_obj:
  
        csv_reader = csv.reader(read_obj)
        listofrowsnoorder = list(csv_reader)
    
    listofrowsnoorder.pop(0)

    for i in listofrowsnoorder:
        a = int(i[0])
        dict = {}
        for j in range(3, friends+3):
            b = i[j]
            for k in listofrowsnoorder:
                if int(k[0]) == int(b):
                    for l in range(3, friends+3):
                        if int(float(k[l])) == a:
                            dict[b] = l - 2
        value = "dict"
        value += str(a)
        globals() [value] = dict

    matchs = {}
    for i in range(STUDENTS + 1, STUDENTS_FINAL+1):
        test = "dict" + str(i)
        temp = globals() [test]
        matchs[str(i)] = len(temp.keys())

    dictmatchs = {}
    matchstup = sorted(matchs.items(), key=lambda x:x[1])
    conversion(matchstup, dictmatchs)

    for i in range(0, STUDENTS):
        listofrowsnoorder.pop(0)
    
    listforextra = []
    for row in range(STUDENTS+1, STUDENTS_FINAL+1):
        listforextra.append(row)
    grp = []

    for i in range(1, groups+1):
        grp.append("grp" + str(i))
    
    for m in listofrowsnoorder:
        for i in listforextra:
            tempextralist = []
            tempextralist = Cloning(listforextra)
            templist = list((globals() ["dict" + str(i)]).keys())
            for j in templist:
                for k in listofrowsnoorder:
                    tempvalue = m[0]
                    if tempvalue == j:
                        if l in grp:
                            if int(j) in globals() [l]:
                                globals() [l].append(i)
                                tempextralist.remove(i)
                                grp.remove(l)

    if len(tempextralist) > 0:
        for i in tempextralist:
            tempvalue = random.choice(grp)
            globals() [tempvalue].append(i)

def duplicate_file():
    tempdata = pd.read_csv("original.csv")

    tempdata.to_csv('data.csv', index=False)

def final_placer_lines():
    global grp1
    global listofstudentspair
    global listofpairpair
    global columns

    tempgrp = []

    for i in grp1:
        tempgrp.append(str(i))

    templist = Cloning(listofstudentspair)

    for i in range(1, (len(grp1))+1):
        i = str(i)
        k = []
        k.append(templist.pop(0))
        k.append(templist.pop(0))
        globals() [i] = k

    for i in tempgrp:
        tempgrp[tempgrp.index(i)] = globals() [i]

    for i in grp1:
        i = str(i)
        for j in listofpairpair:
            if j == i:
                k = []
                position =  listofpairpair.index(i)
                listofstudentspair[position]
    
    finaltemp = Cloning(tempgrp)

    tempvalue = 0
    while finaltemp != []:
        if len(finaltemp) >= columns:
            if tempvalue % 2 == 0:
                print(" ")
                for j in range(0,columns):
                    if finaltemp != []:
                        print(finaltemp.pop(0), end="")
                tempvalue += 1

            elif tempvalue % 2 == 1:
                print(" ")
                for j in range(columns - 1 ,-1 ,-1):
                    if finaltemp != []:
                        print(finaltemp.pop(j), end="")
                tempvalue += 1
        else:
            if tempvalue % 2 == 0:
                print(" ")
                for j in range(0,columns):
                    if finaltemp != []:
                        print(finaltemp.pop(0), end="")
                tempvalue += 1

            elif tempvalue % 2 == 1:
                print(" ")
                for j in range(len(finaltemp) - 1 ,-1,-1):
                    if finaltemp != []:
                        print(finaltemp.pop(j), end="")
                tempvalue += 1
    
    if extra > 0:
        l = []
        l.append(str(STUDENTS_FINAL))
        
    print(" ")

run = True

while run == True:
    ask()
    duplicate_file()
    if TYPE == "G" or TYPE == "g":
        groups()
        make_sheets_groups(Input_Data)
        variable_maker()
        pairing_groups()
        friends_finder()
        rank_groups()
        trail()
        if extra > 0:
            extra_placer()
            print_groups()

        run = False

    elif TYPE == "L" or TYPE == "l":
        lines()
        make_sheets_groups(Input_Data)
        pairing_lines()
        make_sheets_groups(Input_Data)
        variable_maker()
        pairing_groups()
        friends_finder()
        rank_groups()
        trail()
        final_placer_lines()
        run = False
