import re
import Vocabulary as vb

if "define" in msg:
  indexes = [m.start() for m in re.finditer('`', msg)]
  query = msg[indexes[0]:indexes[1]])
  definition = type(json.loads(vb.meaning(query)))<class 'list'>
  print(definition[0])