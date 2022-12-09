import json 

class a:
    def __init__(self,name):
        self.name = name
        
dictionary ={ 
    "name" : "sathiyajith", 
    
} 
json_object = json.dumps(dictionary, indent = 1) 
outfile = open("sample.json", "w") 
outfile.write(json_object) 

with open('sample.json', 'r') as openfile: 
    json_object = json.load(openfile) 
    d = a("Nome")
    d = json_object
    print()
