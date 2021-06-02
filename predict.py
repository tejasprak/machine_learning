# Written by Tejas Prakash
# Updated on June 2, 2021
# Uses a support vector machine (SVM) to predict NBA player position

import csv
import numpy as np
from sklearn.svm import LinearSVC
import warnings

data = []
feat = []

#Get input.
input = raw_input("Enter name of file [adv_stats.csv]")
with open(input) as csvfile:
        nbalist = csv.reader(csvfile)
        data = []
        target = []
        z = 0
        for row in nbalist:
            if z == 0:
                z = z + 1
                continue
            name = row[1]
            #print row
            z = []
            for i in range(8,19):
                if row[i] == '':
                    z.append(0)
                else:
                    z.append(float(row[i]))
            data.append(z)
            position = row[2]
            if position == "PG":
                feat.append(0)
            elif position == "SG":
                feat.append(1)
            elif position == "SF":
                feat.append(2)
            elif position == "PF":
                feat.append(3)
            elif position == "C":
                feat.append(4)
            elif position == "PF-C":
                feat.append(3)
            elif position == "SF-PF":
                feat.append(2)
            elif position == "SF-SG":
                feat.append(1)
            elif position == "SG-PG":
                feat.append(0)
data = np.array(data)
feat = np.array(feat)
print data
print feat
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    with open('adv_stats86.csv') as csvfile:
            def get_prediction(array):
                lonzo_list = []
                for i in range(25):
                    linSVC = LinearSVC()
                    linSVC.fit(data, feat)
                    result = linSVC._predict_proba_lr(array)
                    lonzo_list.append(list(result[0]))
                avg = [float(sum(col))/len(col) for col in zip(*lonzo_list)]
                return avg
            nbalist = csv.reader(csvfile)
            target = []
            z = 0
            highest_value = 0.0
            highest_string = ""
            for row in nbalist:
                if z == 0:
                    z = z + 1
                    continue
                name = row[1]
                s = []
                for i in range(8,19):
                    if row[i] == "":
                        s.append(0)
                    else:
                        s.append(float(row[i]))
                result = get_prediction(s)
                max_value =  max(result)
                role  = result.index(max_value)
                pred = ""
                if role == 0:
                    pred = "PG"
                if role == 1:
                    pred = "SG"
                if role == 2:
                    pred =  "SF"
                if role == 3:
                    pred =  "PF"
                if role ==4:
                    pred =  "C"
                position = row[2]
                if position == "PG":
                    position = 0
                elif position == "SG":
                    position = 1
                elif position == "SF":
                    position  = 2
                elif position == "PF":
                    position = 3
                elif position == "C":
                    position = 4
                elif position == "PF-C":
                    position = 3
                diff = position - role
                diff = abs(diff)
                print name
                print "Real position: " + str(position) + " Predicted position: " + str(role)
                print result
                #if role == 4:
                #    if position == 0 or position == 1:
                #        if int(row[5]) > 45:
                #            highest_string = name + "Real position: " + str(position) + "Predicted position: " + str(role)
                #            print highest_string
                #print result
                #else:
                #    print "-"
                #print result
                #if position == 1:
                    #if role == 4:
                        #print name
                #if diff > 2:
                    #print name
                    #print pred
                    #print "Difference!"
                #if position == role:
                    #print "Match Found!"


print highest_value
print highest_string
