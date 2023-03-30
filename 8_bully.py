class Process:
    def __init__(self,pid):
        self.pid=pid
        self.isLive= True
def printProcess(live,dead):
    print("\tThe coordinator process is : ",coProc)
    if len(live)>0:
        print("\tThe live Processes are : ",end=" ")
        for i in live.keys():
            print(i,",",end=" ")
    else:
        print("\tThere are no live Process")
    print()
    if len(dead)>0:
        print("\tThe dead Processes are : ",end=" ")
        for i in dead.keys():
            print(i,",",end=" ")
    else:
        print("\tThere are no dead Process")
    print()
n = int(input("Enter the number of Process at Initial State :"))
liveProcess=dict()
deadProcess=dict()
for i in range(n):
    liveProcess[i]=Process(i)
coProc=max(liveProcess.keys())
printProcess(liveProcess,deadProcess)
choice=0
while True:
    print()
    print()
    print("-----------Bully Algorithm---------------")
    print("1. Add a Process")
    print("2. Crash a Process")
    print("3. Print the Current Active Processes")
    print("4. Exit")
    choice=int(input("Enter your Choice :"))
    if choice==1:
        pid = int(input("\tEnter the pid of the process to add:"))
        if pid in liveProcess:
            print("\tThe process with this pid is already active")
        else:
            liveProcess[pid]=Process(pid)
            if pid in deadProcess:
                deadProcess.pop(pid)
            coProc = max(liveProcess.keys())
            print("\tThe process is added successfully")
    elif choice==2:
        pid = int(input("\tEnter the pid of the process to Crash:"))
        if pid in deadProcess:
            print("\tThe process with this pid is already Crashed")
        elif pid in liveProcess:
            print("\tThe process with this pid is Crashing")
            liveProcess[pid].isLive = False
            deadProcess[pid]=liveProcess.pop(pid)
            init=int(input("\tEnter the process id who initiates the election :"))
            while True:
                if init not in liveProcess:
                    print("\tThe selected process is crashed")
                else :
                    hasHigherProcess = False
                    for i in liveProcess.keys():
                        if i>init:
                            print("\t\tElection MSG sent",init," --> ",i)
                            hasHigherProcess=True
                    if hasHigherProcess:
                        for i in liveProcess.keys():
                            if i>init:
                                print("\t\tOK MSG sent",i," --> ",init)
                        tempNextMax = 999999
                        for i in liveProcess.keys():
                            if i>init and i<tempNextMax:
                                tempNextMax = i
                        init = tempNextMax
                    else:
                        coProc = max(liveProcess.keys())
                        print("\t\t\t***Finally Process",coProc,"becomes Coordinator***")
                        for i in liveProcess.keys():
                            if i<coProc:
                                print("\t\tCo-ordinator MSG sent",coProc," --> ",i)
                        print("\t\tEnd of Election")
                        break
                    
        else:
            print("\tThere is no such process in the system")
    elif choice==3:
        printProcess(liveProcess,deadProcess)
    elif choice==4:
        break
    else:
        print("\tEnter a valid choice.....")

