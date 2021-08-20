from model import Device
import view as view

def showAll():
   #gets list of all Device objects
   devices_in_db = Device.getAll()
   #calls view
   return view.showAllView(devices_in_db)

def start():
   view.startView()
   answer = input()
   if answer == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()