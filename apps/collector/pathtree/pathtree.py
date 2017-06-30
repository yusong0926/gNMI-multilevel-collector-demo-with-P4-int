ValKey = "_VALUE"

class Path:
    def __init__(self, arr):
        self.elements = arr 



class Branch:
    def __init__(self, model='', dic={}):
        self.model = model
        self.dic = dic

    def add(self, path, val):
        if len(path.elements) == 0:
            print "empty path"
            return
        
        dic_next = self.dic

        for i , element in enumerate(path.elements):
            if (i < len(path.elements) - 1) :
               if element in dic_next:
                   dic_next = dic_next[element]
               else:
                   dic_next[element] = {}
                   dic_next = dic_next[element]

        if path.elements[-1] in dic_next and type(dic_next[path.elements[-1]]) is list:
           dic_next[path.elements[-1]].append(val)
        else:
           dic_next[path.elements[-1]] = [val]

    def get(self, path):
         
         dic_next = self.dic
         for element in path.elements:
             if element in dic_next:
                 dic_next = dic_next[element]
             else:
                 return
         return dic_next

class PathVal:
    def __init__(self, path, value):
        self.path = path
        self.value = value

