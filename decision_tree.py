from util import entropy, information_gain, partition_classes
import numpy as np

class DecisionTree(object):

    def __init__(self):
        self.tree = {"first" : None,"second" : None,"inform_gain" : 0,"label" : 0,"attr_num" : -1,"split_val" : 0}
        #print self.tree["second"]

    def learn(self, X, y):
        # TODO: train decision tree and store it in self.tree
        #print "AA"
        #print X
        #print "GG"
        #print len(X)
        #print X[0]
        #print len(X[0])
        #i=0        
        attr_list = range(len(X[0]) - 1)
        """if i<=1:
            print i
            print X[0]            
            print attr_list
            i=i+1"""
        self.learn_new(attr_list, X, y)

    def classify(self, record):
        # TODO: return predicted label for a single record using self.tree        
        if self.tree["first"] == None and self.tree["second"] == None:
            return(self.tree["label"])
        elif self.tree["attr_num"] > -1 and record[self.tree["attr_num"]] <= self.tree["split_val"]:
            return(self.tree["first"].classify(record))
        else:
            return(self.tree["second"].classify(record))        

    def learn_new(self, attr_list, X, y):
        """j=0
        if j<=1:
            #print j
            print y
            print"A"
            print len(y)
            print (y.count(0))
            print (y.count(1))
            print y[0]
            j=j+1"""
        if y.count(0) == len(y):
            self.tree["label"] = 0
            return 

        if y.count(1) == len(y):
            self.tree["label"] = 1
            return 

        if len(attr_list) == 0:
            if y.count(0) > y.count(1):
                self.tree["label"] = 0
            else:
                self.tree["label"] =1
            
        for attr in attr_list:
            #print attr
            temp_split = np.median(X, axis=0)[attr]
            #print temp_split
            #print 
            
            attr_column = []
            for x in X:
                attr_column.append(x[attr])
            #print attr_column
            #print        
            #two_y_class = partition_classes(attr_column, y, self.tree["split_val"])
            two_y_class = partition_classes(attr_column, y,temp_split)
            #print two_y_class
            #print len(two_y_class[0])
            #print len(two_y_class[1])
            #print 
            #print
            temp_infogain = information_gain(y, two_y_class)
            #print temp_infogain
            #print
            
            if self.tree["attr_num"] == -1 or temp_infogain > self.tree["inform_gain"]:            
                self.tree["attr_num"] = attr
                self.tree["inform_gain"] = temp_infogain
                self.tree["split_val"] = temp_split

        #print self.tree["attr_num"]
        #print self.tree["inform_gain"]
        #print self.tree["split_val"]
        #print len(attr_list)
        #print "HERE"

        if len(attr_list) > 0:
                        
            first_X = []
            first_y = []
            second_X = []
            second_y = []            
            for i in range(len(X)):
                #print
                if (X[i][self.tree["attr_num"]]) <= self.tree["split_val"]:
                    first_X.append(X[i])
                    first_y.append(y[i])
                else:
                    second_X.append(X[i])
                    second_y.append(y[i])                    

            #print first_X
            #print len(first_X)
            #print "BB"
            #print len(first_y)

            #print second_X
            #print len(second_X)
            #print len(second_y)
            #print

            #RECURSION- CALLING THE SAME FUNCTION ITSELF HERE
            attr_list.remove(self.tree["attr_num"])
            
            self.tree["first"] = DecisionTree()
            self.tree["second"] = DecisionTree()
            
            self.tree["first"].learn_new(attr_list, first_X, first_y)
            #print "AA"
            #print 
            self.tree["second"].learn_new(attr_list, second_X, second_y)  



 

