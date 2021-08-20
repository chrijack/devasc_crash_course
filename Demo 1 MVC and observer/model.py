import json

class Device:
   def __init__(self, routername = None, ip = None):
      self.routername = routername
      self.ip = ip
   #returns Device name
   def name(self):
      return ("Name : %s IP address: %s \n" % (self.routername,self.ip))
        
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(cls):
      database = open('db.txt', 'r')
      result = []
      json_list = json.loads(database.read())
      for item in (json_list):
          device = Device(item , json_list[item])
          result.append(device)
      return result