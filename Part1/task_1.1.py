objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
lstobject = set()
for i in range(len(objects)):
  lstobject.add(id(objects[i]))
ans = len(lstobject)
print(ans)
