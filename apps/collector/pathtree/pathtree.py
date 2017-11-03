ValKey = "_VALUE"

class Path:
    def __init__(self, arr):
        self.elements = arr 



class Branch:
    def __init__(self, model='', dic={}):
        self.model = model
        self.dic = dic

    def add(self, path, tm, val):
        if len(path) == 0:
            print "empty path"
            return
        
        dic_next = self.dic

        for i , element in enumerate(path):
            if (i < len(path) - 1) :
               if element in dic_next:
                   dic_next = dic_next[element]
               else:
                   dic_next[element] = {}
                   dic_next = dic_next[element]
        

         dic_next[path[-1]] = val 

    def get(self, path):
         
         dic_next = self.dic
         for element in path:
             if element in dic_next:
                 dic_next = dic_next[element]
             else:
                 return
         return dic_next
    

class PathVal:
    def __init__(self, path, value):
        self.path = path
        self.value = value

