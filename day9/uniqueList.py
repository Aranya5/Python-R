# the element that is present only once
def unique(numlist):
  uniqueEle =[]
  for ele in numlist:
    c = numlist.count(ele)
    if c == 1:
      uniqueEle.append(ele)
  print("The unique elements in the list are:", uniqueEle)
  return


def duplicate(numlist):
  duplicates ={}
  for ele in numlist:
    c = numlist.count(ele)
    if c >= 2:
      duplicates[ele] = c
  print("The duplicate elements in the list are:", duplicates)
  return


def createUniqu(list):
  uniq_list = []
  for x in list:
    if x not in uniq_list:
      uniq_list.append(x)
  print(uniq_list)
  return

import random
list = []
for x in range(20):
  list.append(random.randint(1,9))
print("The original list is:", list)
unique(list)
duplicate(list)

print("Unique elemnts in the list are:")
createUniqu(list)