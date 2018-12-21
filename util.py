from scipy import stats
import numpy as np


# This method computes entropy for information gain
def entropy(class_y):
    n_zero=0.0
    n_one=0.0
    for i in class_y:
        #print i
        if i == 0:
            n_zero=n_zero+1
            #print n_zero
        else:
            n_one=n_one+1
    #print n_zero
    #print n_one
    #print len(class_y)
    #print "AA"
    if n_zero==0 or n_one==0 or len(class_y)==0:
        ent =0
    else:
        ent=-((n_zero/len(class_y))*(np.log2(n_zero/len(class_y)))+(n_one/len(class_y))*(np.log2(n_one/len(class_y))))
    """Compute the entropy for a list of classes
	
    Example:
        entropy([0,0,0,1,1,1,1,1,1]) = 0.92
    """
    return ent

def partition_classes(x, y, split_point):
    out = [[],[]]

    for j in range(0,len(x)):
        if x[j]<=split_point:
            out[0].extend([y[j]])
        else:
            out[1].extend([y[j]])
    return out
    """Partition the class vector, y, by the split point. 

    Return a list of two lists where the first list contains the labels 
    corresponding to the attribute values less than or equal to split point
    and the second list contains the labels corresponding to the attribute 
    values greater than split point

    Example:
    x = [2,4,6,7,3,7,9]
    y = [1,1,1,0,1,0,0]
    split_point = 5

    output = [[1,1,1], [1,0,0,0]]
    """ 
    # TODO: Implement this
    
def information_gain(previous_y, current_y):
    ent_a=entropy(previous_y)
    var1=current_y[0]
    var2=current_y[1]
    len1=float(len(var1))
    len2=float(len(var2))
    len3=len1+len2
    #print "NOW"
    #print len1
    #print len2
    #print "NOWW"
    ent_b=(len1/len3)*(entropy(var1))+(len2/len3)*(entropy(var2))
    ent_final=ent_a-ent_b
    #print ent_final
    
    """Compute the information gain from partitioning the previous_classes
    into the current_classes.

    Example:
    previous_classes = [0,0,0,1,1,1]
    current_classes = [[0,0], [1,1,1,0]]

    Information gain = 0.45915
    Input:
    -----
        previous_classes: the distribution of original labels (0's and 1's)
        current_classes: the distribution of labels given a particular attr
    """
    # TODO: Implement this
    return ent_final

