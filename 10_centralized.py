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
    print(f"\nChecking for cycles in site {site}")
    print("Processes checked: ", end = "")
    list(map(lambda x: print(x.id, end = " "), Processes))
    print("\n")
    for i in Processes:
        if(i.holding != None and i.waiting!=None):
            if i.holding.site == site and i.waiting.site == site:
                if(detectCycle(Processes,Resources, i, i.id)):
                    return True
    return False

def checkDeadlock(Processes,Resources):
    print("\nChecking for cycles in coordinator")
    print("Processes checked: ", end = "")
    list(map(lambda x: print(x.id, end = " "), Processes))
    print("\n")
    for i in Processes:
        if(detectCycle(Processes,Resources, i, i.id)):
            return True

Resources = []
s1No = int(input("No. of resources in site 1: "))
for i in range(s1No):
    Resources.append(resource(i, 1))
s2No = int(input("No. of resources in site 2: "))
for i in range(s1No, s1No+s2No):
    Resources.append(resource(i, 2))

s1Resources = [x for x in Resources if x.site == 1]
s2Resources = [x for x in Resources if x.site == 2]
print("Resources in site 1:")
list(map(lambda x: print(x.id, end = " "), s1Resources))
print("\nResources in site 2:")
list(map(lambda x: print(x.id, end = " "), s2Resources))


Processes = []
NoOfProcesses = int(input("\nEnter number of processes: "))
for i in range(NoOfProcesses):
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
for x in Processes:
    h = x.holding
    w = x.waiting
    if(h!=None and w!=None):
        if(h.site == 1 or w.site == 1):
            s1Plist.append(x)
        if(h.site == 2 or w.site == 2):
            s2Plist.append(x)


if(checkDeadlockSite(s1Plist,s1Resources, 1)):
    print("Deadlock detected in site 1")
elif(checkDeadlockSite(s2Plist,s2Resources, 2)):
    print("Deadlock detected in site 2")
elif(checkDeadlock(Processes,Resources)):
    print("Deadlock detected in central coordinator")

# 2
# 1
# 3
# 0
# 2
# 1
# 0
# 2
# 1



# No. of resources in site 1: 2
# No. of resources in site 2: 1
# Resources in site 1:
# 0 1 
# Resources in site 2:
# 2 
# Enter number of processes: 3
# What resource is process-0 holding? : 0
# What resource is process-0 waiting for? : 2
# What resource is process-1 holding? : 1
# What resource is process-1 waiting for? : 0
# What resource is process-2 holding? : 2
# What resource is process-2 waiting for? : 1

# Checking for cycles in site 1
# Processes checked: 0 1 2 


# Checking for cycles in site 2
# Processes checked: 0 2 


# Checking for cycles in coordinator
# Processes checked: 0 1 2 

# Deadlock detected in central coordinator