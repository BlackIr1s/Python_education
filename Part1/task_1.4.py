name = {}
parent_name = {}
def create(namespace, parent):
    if namespace not in parent_name:
        parent_name[namespace] = [parent]
    else:
        parent_name[namespace].append(parent)
def  add(namespace,var):
    if namespace not in name:
        name[namespace] = [var]
    else:
        name[namespace].append(var)
def get(namespace, var):
    print(namespace, name[namespace], var)
    if var == name[namespace]:
        return namespace
    else:
        get(parent_name[namespace], var)
n = int(input())
for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd == 'add':
        add(namesp, arg)
    else:
        print(get(namesp, arg))





