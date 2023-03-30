class process:
    def __init__(self, id, holding, waiting):
        self.id = id
        self.holding = holding
        self.waiting = waiting

class resource:
    def __init__(self, id, site):
        self.id = id
        self.site = site
        self.heldBy = False


def detectCycle(Processes,Resources, cur, start):
    for i in Processes:
        if(cur.waiting == i.holding and cur.waiting in Resources ):
            if(i.id == start):
                return True
            else:
                if(detectCycle(Processes,Resources, i, start)):
                    return True
    return False

def checkDeadlockSite(Processes,Resources, site):
    print("Processes checked: ", end = "")
    list(map(lambda x: print(x.id, end = " "), Processes))
    print("\n")
    for i in Processes:
        if(i.holding != None and i.waiting!=None):
            if i.holding.site == site and i.waiting.site == site:
                if(detectCycle(Processes,Resources, i, i.id)):
                    return True
    return False

def checkDeadlockTop(Processes,Resources):
    print("\nChecking for cycles in coordinator")
    print("Processes checked: ", end = "")
    list(map(lambda x: print(x.id, end = " "), Processes))
    print("\n")
    for i in Processes:
        if(detectCycle(Processes,Resources, i, i.id)):
            return True

def checkDeadlockLocal(Processes, Resources, num):
    print(f"\nChecking for cycles in local coordinator - {num}")
    print("Processes checked: ", end = "")
    list(map(lambda x: print(x.id, end = " "), Processes))
    print("\n")
    for i in Processes:
        if(detectCycle(Processes,Resources, i, i.id)):
            return True


Resources = []
total = 0
s1 = int(input("No. of resources in site 1: "))
for i in range(s1):
    Resources.append(resource(i, 1))
total+=s1
s2 = int(input("No. of resources in site 2: "))
for i in range(total, total+s2):
    Resources.append(resource(i, 2))
total+=s2
s3 = int(input("No. of resources in site 3: "))
for i in range(total, total+s3):
    Resources.append(resource(i, 3))
total+=s3
s4 = int(input("No. of resources in site 4: "))
for i in range(total, total+s4):
    Resources.append(resource(i, 4))
total+=s4

s1 = [x for x in Resources if x.site == 1]
s2 = [x for x in Resources if x.site == 2]
s3 = [x for x in Resources if x.site == 3]
s4 = [x for x in Resources if x.site == 4]
print("Resources in site 1:")
list(map(lambda x: print(x.id, end = " "), s1))
print("\nResources in site 2:")
list(map(lambda x: print(x.id, end = " "), s2))
print("\nResources in site 3:")
list(map(lambda x: print(x.id, end = " "), s3))
print("\nResources in site 4:")
list(map(lambda x: print(x.id, end = " "), s4))


Processes = []
initial = int(input("\nEnter number of processes: "))
for i in range(initial):
    hld = str(input(f"What resource is process-{i} holding? : ")) # Blank for none
    wai = str(input(f"What resource is process-{i} waiting for? : ")) # Blank for none
    if hld == "":
        hld = None
    else: 
        hld = [x for x in Resources if x.id == int(hld)][0]
        hld.heldBy = i
    if wai == "":
        wai = None
    else:
        wai = [x for x in Resources if x.id == int(wai)][0]

    Processes.append(process(i, hld, wai))

s1Plist = []
s2Plist = []
s3Plist = []
s4Plist = []
for x in Processes:
    h = x.holding
    w = x.waiting
    if(h!=None and w!=None):
        if(h.site == 1 or h.site == 1):
            s1Plist.append(x)
        if(w.site == 2 or w.site == 2):
            s2Plist.append(x)
        if(h.site == 3 or h.site == 3):
            s3Plist.append(x)
        if(w.site == 4 or w.site == 4):
            s4Plist.append(x)
        


if(checkDeadlockSite(s1Plist,s1, 1)):
    print("Deadlock detected in site 1")
elif(checkDeadlockSite(s2Plist,s2, 2)):
    print("Deadlock detected in site 2")
elif(checkDeadlockSite(s3Plist,s3, 3)):
    print("Deadlock detected in site 3")
elif(checkDeadlockSite(s4Plist,s4, 4)):
    print("Deadlock detected in site 4")

elif(checkDeadlockLocal(s1Plist+s2Plist,s1 + s2, 1)):
    print("Deadlock detected in local coordinator 1")
elif(checkDeadlockLocal(s3Plist+s4Plist,s3 + s4, 2)):
    print("Deadlock detected in local coordinator 2")
elif(checkDeadlockTop(Processes,Resources)):
    print("Deadlock detected in top level")


# 2
# 3
# 1
# 1
# 7
# 0
# 2
# 1
# 0
# 2
# 1
# 4
# 3
# 5
# 3
# 6
# 5
# 4
# 6



# No. of resources in site 1: 2
# No. of resources in site 2: 3
# No. of resources in site 3: 1
# No. of resources in site 4: 1
# Resources in site 1:
# 0 1 
# Resources in site 2:
# 2 3 4
# Resources in site 3:
# 5
# Resources in site 4:
# 6
# Enter number of processes: 7
# What resource is process-0 holding? : 0
# What resource is process-0 waiting for? : 2
# What resource is process-1 holding? : 1
# What resource is process-1 waiting for? : 0
# What resource is process-2 holding? : 2
# What resource is process-2 waiting for? : 1
# What resource is process-3 holding? : 4
# What resource is process-3 waiting for? : 3
# What resource is process-4 holding? : 5
# What resource is process-4 waiting for? : 3
# What resource is process-5 holding? : 6
# What resource is process-5 waiting for? : 5
# What resource is process-6 holding? : 4
# What resource is process-6 waiting for? : 6
# Processes checked: 0 1

# Processes checked: 0 3 4

# Processes checked: 4

# Processes checked: 6


# Checking for cycles in local coordinator - 1
# Processes checked: 0 1 0 3 4


# Checking for cycles in local coordinator - 2
# Processes checked: 4 6


# Checking for cycles in coordinator
# Processes checked: 0 1 2 3 4 5 6

# Deadlock detected in top level