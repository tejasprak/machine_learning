import csv
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.svm import LinearSVC
import warnings
data = []
feat = []
# np.array(['1','2','3']).astype(np.float)

with open('adv_stats86.csv') as csvfile:
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
            #feat.append(row[2])
#print len(data)
#print len(feat)
data = np.array(data)
feat = np.array(feat)
print data
print feat
#print data
#print len(data)
#print len(feat)
#gnb = GaussianNB()
#model = gnb.fit(data, feat)
#linSVC = LinearSVC()
#linSVC.fit(data,feat)
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
                    #print i
                #print lonzo_list
                avg = [float(sum(col))/len(col) for col in zip(*lonzo_list)]
                return avg
            nbalist = csv.reader(csvfile)
            #data = []
            target = []
            z = 0
            highest_value = 0.0
            highest_string = ""
            for row in nbalist:
                if z == 0:
                    z = z + 1
                    continue
                name = row[1]
                #print row
                s = []
                for i in range(8,19):
                    #print name
                    if row[i] == "":
                        s.append(0)
                    else:
                        s.append(float(row[i]))
                #result = linSVC._predict_proba_lr(s)
                result = get_prediction(s)
                #print result
                #result = list(result)
                max_value =  max(result)
                #result = list(result)
                #result = list(result[0])
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
                #print diff
                #if diff > 2:
                #if role == 2:
                #    if int(row[5]) > 45:
                #        if result[2] > highest_value:
                #            print name
                #            highest_value = result[2]
                #            highest_string = name + "Real position: " + str(position) + "Predicted position: " + str(role)
                #            print "New Highest Found"
#
                #            print highest_string
                #            print result
                #else:
                #    print name
                #    print result
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

#array = [.580,.244,.397,2.0,11.4,6.9,48.9,3.5,0.1,12.4,23.7]
#result = linSVC._predict_proba_lr(array)
#    print result
print highest_value
print highest_string
