class process:
    def __init__(self, id, holding, waiting):
        self.id = id
        self.holding = holding
        self.waiting = waiting

def probe(pList, cur, start):
    for i in pList:
        if(cur.waiting == i.holding):
            print(f"Process-{cur.id} sends message ({start},{cur.id},{i.id})")
            if(i.id == start):
                print("Deadlock detected")
                return
            else:
                probe(pList, i, start)
    

pList = []
initial = int(input("Enter number of processes: "))
for i in range(initial):
    hld = str(input(f"What resource is process-{i} holding? : ")) # Blank for none
    wai = str(input(f"What resource is process-{i} waiting for? : ")) # Blank for none
    if hld == "":
        hld = False
    if wai == "":
        wai = False
    pList.append(process(i, hld, wai))

det = int(input("Process id that initiates probe : "))
cur = [x for x in pList if x.id == det][0]
start = cur.id

probe(pList, cur, start)


# 3
# 0
# 2
# 1
# 0
# 2
# 1
# 0

# Enter number of processes: 3
# What resource is process-0 holding? : 0
# What resource is process-0 waiting for? : 2
# What resource is process-1 holding? : 1
# What resource is process-1 waiting for? : 0
# What resource is process-2 holding? : 2
# What resource is process-2 waiting for? : 1
# Process id that initiates probe : 0
# Process-0 sends message (0,0,2)
# Process-2 sends message (0,2,1)
# Process-1 sends message (0,1,0)
# Deadlock detected