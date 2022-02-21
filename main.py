from random import seed
from random import randint
import array as arr

o=0
i = 0 # i is counter of repeating
j=0
while i<1000:

  flag = 0
  a=b=c=0
  doors = arr.array('i', [])
  while flag!=2 :   # flag to inform that the array has been constructed correctley
        a = randint(0, 1)
        b = randint(0, 1)
        c = randint(0, 1)
        flag=a+b+c
  i+=1
  doors.append(a)
  doors.append(b)
  doors.append(c)
  choice=randint(0,2)
  index=choice
  choice=doors[choice]
  host=0
  while(1):
      host = randint(0, 2)
      host_index=host
      host = doors[host]
      if host!=0 and host_index!=index:
        doors.remove(host)
        break
      else :
        continue
  if (choice == 0):
      o=o+1   # o is winning times when not switching
  if (choice == doors[0]): # switching th player choice
      choice = doors[1]
  else:
      choice = doors[0]
    # print (s)
  if (choice == 0):
      j=j+1   #j is winning times when switching
answer=j/i
print("the propobility of winning when switching",answer)
answer=o/i
print("the propobility of winning without switching",answer)