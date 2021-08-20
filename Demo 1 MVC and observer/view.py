from model import Device

def showAllView(list):
   print('In our database we have %i device entries:' % len(list))
   for item in list:
      print (item.name())
def startView():
   print('MVC Example')
   print('Do you want to see devices in my db?[y/n]')
def endView():
   print('Goodbye!')