import json
class dataHelper:
    def __init__(self) -> None:
        pass
    
    def saveRace(self,data:dict):
        try: Rfile = open('Races/'+data['Name']+'.race','x',encoding='utf-8')
        except: Rfile = open('Races/'+data['Name']+'.race','w',encoding='utf-8')
        json.dump(data,Rfile,indent=4)
        Rfile.close()
        
    def loadRace(self,name:str) -> dict:
        Rfile = open('Races/'+name+'.race','r',encoding='utf-8')
        data = json.load(Rfile)
        Rfile.close()
        return data

    def saveClass(self,data:dict):
        try: Rfile = open('Classes/'+data['Name']+'.clas','x',encoding='utf-8')
        except: Rfile = open('Classes/'+data['Name']+'.clas','w',encoding='utf-8')
        json.dump(data,Rfile,indent=4)
        Rfile.close()

    def loadClass(self,clas):
        Rfile = open('Classes/'+clas+'.clas','r',encoding='utf-8')
        data = json.load(Rfile)
        Rfile.close()
        return data

    def loadOverideClass(self,clas):
        Rfile = open('Classes Overide/'+clas+'.clas','r',encoding='utf-8')
        data = json.load(Rfile)
        Rfile.close()
        return data
    def saveSubclass(self,data:dict):
        pass
    def loadSubclass(self):
        pass