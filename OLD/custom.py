#misc methods
def parseBool(str): #string to variable
    if str.lower() in ('true', 'yes', '1', 't', 'y'):
        return True
    elif str.lower() in ('false', 'no', '0', 'f', 'n'):
        return False 
    else:
        raise Exception('Boolean value expected')

def changeBase(num, origin, out):
    return True

#file-object classes
class Cookie: #fortune cookies
  Fortune = ""
  Numbers = ""
  Learn = False
  Chinese = ""
  English = ""

  def __init__(self,  raw):
    inputs = raw.split('|')
    Fortune = inputs[0]
    Numbers = inputs[1]
    Learn = parseBool(inputs[2])
    if(Learn == true):
      Chinese = inputs[3]
      English = inputs[4]
    elif (Learn == false):
      Chinese = null
      English = null
    
  def fileToArr():
      arrList = []
      with open('fortunecookies.txt') as file:
          arrList.append(Cookie(file.readline())
      return arrList

class Pun: #puns
  Phrase = ""
  Keywords = []
  def __init__(self, raw):
    #TODO
  def fileToArr():
    #TODO
    
#writing prompts