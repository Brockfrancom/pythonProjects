import csv
import math
import copy
##################################################
# module: bin_id3.py
# description: Binary ID3 decision tree learning
# Brock Francom
# A02052161
# bugs to vladimir dot kulyukin at usu dot edu
###################################################
### Positive and Negative Constant labels; don't change
### these.
PLUS  = 'Yes'
MINUS = 'No'

class id3_node(object):

    def __init__(self, lbl):
        self.__label = lbl
        self.__children = {}

    def set_label(self, lbl):
        self.__label = lbl
        
    def add_child(self, attrib_val, node):
        self.__children[attrib_val] = node

    def get_label(self):
        return self.__label

    def get_children(self):
        return self.__children

    def get_child(self, attrib_val):
        assert attrib_val in self.__children
        return self.__children[attrib_val]

class bin_id3(object):

    @staticmethod
    def get_attrib_values(a, kvt):
        """
        Looks up values of attribute a in key-value table.
        """
        return kvt[a]

    @staticmethod
    def get_example_attrib_val(example, attrib):
        """
        Get the value of attribute attrib in example.
        """
        assert attrib in example
        return example[attrib]

    @staticmethod
    def parse_csv_file_into_examples(csv_fp):
        """
        Takes a csv file specified by the path csv_fp and
        converts it into an array of examples, each of which
        is a dictionary of key-value pairs where keys are
        column names and the values are column attributes.
        """
        examples = []
        with open(csv_fp) as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            key_names  = None
            for row in csv_reader:
                if len(row) == 0:
                    continue
                if line_count == 0:
                    key_names = row
                    for i in range(len(key_names)):
                        ## strip whitespace on both ends.
                        row[i] = row[i].strip()
                        line_count += 1
                else:
                    ex = {}
                    for i, k in enumerate(key_names):
                        ## strip white spaces on both ends.
                        ex[k] = row[i].strip()
                    examples.append(ex)
            return examples, key_names

    @staticmethod
    def construct_attrib_values_from_examples(examples, attributes):
        """
        Constructs a dictionary from a list of examples where each attribute
        is mapped to a list of all its possible values in examples.
        """
        avt = {}
        for a in attributes:
            if not a in avt:
                avt[a] = set()
            for ex in examples:
                if a in ex:
                    if not ex[a] in avt[a]:
                        avt[a].add(ex[a])
                else:
                    avt[a].add(None)
        return avt

    @staticmethod
    def find_examples_given_attrib_val(examples, attrib, val):
        """
        Finds all examples in such that attrib = val.
        """
        rslt = []
        #print('Looking for examples where {}={}'.format(attrib, val))
        for ex in examples:
            if attrib in ex:
                if ex[attrib] == val:
                    rslt.append(ex)
        return rslt

    @staticmethod
    def find_most_common_attrib_val(examples, attrib, avt):
        """
        Finds the most common value of attribute attrib in examples.
        """
        attrib_vals = bin_id3.get_attrib_values(attrib, avt)
        val_counts = {}
        for av in attrib_vals:
            SV = bin_id3.find_examples_given_attrib_val(examples, attrib, av)
            val_counts[av] = len(SV)
        max_cnt = 0
        max_val = None
        #print('val_counts = {}'.format(val_counts))
        for val, cnt in val_counts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_val = val
        assert max_val != None
        return max_val, max_cnt

    @staticmethod
    def get_non_target_attributes(target_attrib, attribs):
        """
        Returns a comma separated string of all attributes in the list attribs that
        that are not equal to target_attrib; 
        - target_attrib is a string.
        - attribs is a list of strings.
        """
        return ', '.join([a for a in attribs if a != target_attrib])

    @staticmethod
    def display_info_gains(gains):
        """
        Displays a dictionary of information gains in the format attribute: gain.
        """
        print('Information gains are as follows:')
        for attrib, gain in gains.items():
            print('\t{}: {}'.format(attrib, gain))

    @staticmethod
    def display_id3_node(node, tabs):
        """
        Displays the subtree rooted at a node.
        """
        print(tabs + '{}'.format(node.get_label()))
        children = node.get_children()
        for v, n in children.items():
            print(tabs + '\t{}'.format(v))
            bin_id3.display_id3_node(n, tabs+'\t\t')

    ## HW10
    @staticmethod
    def proportion(examples, attrib, val):
        """
        Computes the proportion of examples whose attribute attrib has the value val.
        """
        num = bin_id3.find_examples_given_attrib_val(examples, attrib, val)
        if len(examples) == 0:
            return 0
        p = len(num)/len(examples)  
        return p    

    ## HW10
    @staticmethod
    def entropy(examples, attrib, avt):
        """
        Computes entropy of examples with respect of attribute attrib.
        avt is the attribute value table computed by construct_attrib_values_from_examples().
        """
        p1 = bin_id3.proportion(examples, attrib, PLUS)
        p0 = bin_id3.proportion(examples, attrib, MINUS)
        atv, cnt = bin_id3.find_most_common_attrib_val(examples, attrib, avt)
        try:
            entropy = -p1*math.log(p1,2) + -p0*math.log(p0,2)
        except Exception:
            entropy = 0
        return entropy

    ## HW10    
    @staticmethod
    def gain(examples, target_attrib, attrib, avt):
        """
        Computes gain of the attribute attrib in examples.
        """
        entropy = bin_id3.entropy(examples, target_attrib, avt)
        for val in avt[attrib]:
            newExamples = bin_id3.find_examples_given_attrib_val(examples, attrib, val)
            p = bin_id3.proportion(examples, attrib, val)
            newEnt = bin_id3.entropy(newExamples, target_attrib, avt)
            ent = (p) * newEnt
            entropy -= ent
        return entropy 

    ## HW10    
    @staticmethod
    def find_best_attribute(examples, target_attrib, attribs, avt):
        """
        Finds the attribute in attribs with the highest information gain.
        This method returns three values: best attribute, its gain, and
        a dictionary that maps each attribute to its gain.
        """
        best = 0
        gain = 0
        dic = {}
        for attrib in attribs:
            if attrib != target_attrib:
                tempGain = bin_id3.gain(examples, target_attrib, attrib, avt)
                dic[attrib] = tempGain
                if tempGain > gain:
                    gain = tempGain
                    best = attrib
        return (best, gain, dic)
    
    ## HW10    
    @staticmethod
    def fit(examples, target_attrib, attribs, avt, dbg):
        """
        Returns a decision tree from examples given target_attribute target_attrib,
        attributes attribs, and attribute-value table.
        - examples is a list of examples;
        - target_attrib is a string (e.g., 'PlayTennis')
        - attribs is a list of attributes (strings)
        - avt is a dictionary constructed by construct_attrib_values_from_examples()
        - dbg is a debug flag True/False. When it is true, then things should
          be printed out as the algorithm computes the decision tree. For example,
          in my implementation I have things like
          if len(SV) == len(examples):
            ## if all examples are positive, then return the root node whose label is PLUS.
            if dbg == True:
                print('All examples positive...')
                print('Setting label of root to {}'.format(PLUS))
            root.set_label(PLUS)
            return root
            
            1. examples is a list of examples, each of which is a Python dictionary;
            2. target_attrib is a string (e.g., 'PlayTennis');
            3. attribs is a list of attributes (strings);
            4. avt is a dictionary constructed by construct_attrib_values_from_examples();
            5. dbg is a debug True/False 
            
            Run test_id3_ut22(self, tn=22) to test your implementation. Your implementation of fit() should return the
            id3_node object that is the root of the decision tree shown on slide 3 of CS3430_S20_Decision_Trees_Part02.pdf.
            Remember to remove best attributes from the list of attributes (i.e., attribs) in your recursive calls. Don't use a single
            global list of attributes. Each recursive call should have its own copy of attributes. You can use the method copy.copy
            from the copy package to make shallow copies of attribs. Here's a quick example of how I remove the best attribute
            from the list of attributes in my implementation of fit before making a recursive call.         
            
            BinID3(Examples, TargetAttrib, Attributes)
                6) If there are no more attributes (i.e., the length of Attributes is 0), then set the label 
                of the root node to the most common value of TargetAttrib in Examples; 
                7)  best_attrib,  best_gain  =  find  best  attribute  and  its  information  gain  in  the 
                remaining Attributes and set the root’s label to best_attrib;
                8) For each value bav of best_attrib 
                        new_examples = find all examples in where the value of best_attrib=bav
                        If there are no new_examples, Then
                            lbl = find most common attribute value of TargetAttrib in Examples
                            child_node = create a new new whose lable is lbl
                            add child_node to the root node on the link bav
                        Else remove best_attrib from Attribs
                            child_node = BinID3(new_examples, TargetAttrib, Attribs)
                            add child_node on the link bav to root
                    return root   
                    
        Looking for best attribute among Temperature, Wind, Humidity, Outlook...
        Information gains are as follows:
        	Temperature: 0.029222565658954647
        	Wind: 0.04812703040826927
        	Humidity: 0.15183550136234136
        	Outlook: 0.2467498197744391
        Best attrib is Outlook with a gain of 0.2467498197744391...
        Looking for examples where Outlook=Overcast...
        Found some examples...
        Removing Outlook from attributes...

        """
        global PLUS
        global MINUS
        
        root = id3_node("root")
        print("Looking for best attribute among {}...".format(attribs))

        SV = bin_id3.find_examples_given_attrib_val(examples, target_attrib, PLUS)
        if len(SV) == len(examples):
            ## if all examples are positive, then return the root node whose label is PLUS.
            if dbg == True:
                print('All examples positive...')
                print('Setting label of root to {}'.format(PLUS))
            root.set_label(PLUS)
            return root
        SV = bin_id3.find_examples_given_attrib_val(examples, target_attrib, MINUS)
        if len(SV) == len(examples):
            ## if all examples are negative, then return the root node whose label is MINUS.
            if dbg == True:
                print('All examples negative...')
                print('Setting label of root to {}'.format(MINUS))
            root.set_label(MINUS)
            return root
        ba, bag, gs = bin_id3.find_best_attribute(examples, target_attrib, attribs, avt)
        bin_id3.display_info_gains(gs)
        print("Best attrib is {} with a gain of {}...".format(ba, bag))
        
        values = bin_id3.get_attrib_values(ba, avt)
        for value in values:
            if dbg == True:
                print("Looking for examples where {}={}...".format(ba, value))
            new_examples = bin_id3.find_examples_given_attrib_val(examples, ba, value)
            if len(new_examples) == 0:
                pass
            else:
                print("Found some examples...")
            if dbg == True:
                print('Removing {} from attributes...'.format(ba))
            copy_attribs = copy.copy(attribs)
            copy_attribs.remove(ba)
            
            if dbg == True:
                print('\nComputing decision tree for examples where {}={}...'.format(ba, value))
            child_node = bin_id3.fit(new_examples, target_attrib, copy_attribs, avt, dbg)        
            print("Looking for best attribute among {}...".format(attribs))
        

        
    ## HW10            
    @staticmethod
    def predict(root, example):
        """
        Classifies an example given a decision tree whose root is root.
        """
        global PLUS
        global MINUS
        ## YOUR CODE HERE
        pass
        
        
