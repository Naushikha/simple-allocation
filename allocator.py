import csv
import random
import math
import sys
import pickle

# Fancy function to generate random people
def genRanList(n):
    rList = []
    for i in range(n):
        score1 = random.randint(0, 10)
        score2 = random.randint(0, 10)
        score3 = random.randint(0, 10)
        first_name = random.choice(list(open('first_names.txt'))).strip()
        last_name = random.choice(list(open('last_names.txt'))).strip()
        name = first_name + ' ' + last_name
        organization = random.choice(list(open('organizations.txt'))).strip() 
        if (bool(random.getrandbits(1))): type = "T"
        else: type = "ES"
        # Need to make them into string to emulate csv behaviour
        rList.append([str(organization), str(name), str(score1), str(score2), str(score3), type])
    return rList

def writeList(pList, filename):
    with open(filename, 'wb') as fp:
        pickle.dump(pList, fp)

def readList(filename):
    with open (filename, 'rb') as fp:
        pList = pickle.load(fp)
    return pList

def writeListAsCSV(pList, filename):
    with open(filename, 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for p in pList:
            wr.writerow(p)

def printList(list):
    for x in range(len(list)):
        print(list[x])

# Filter function by Tamil
def byT(master_proctor): 
    if (master_proctor[5] == "T"): return True
    else: return False

# Filter function by English+Sinhala
def byES(master_proctor): 
    if (master_proctor[5] == "ES"): return True
    else: return False

# Sorting function by 1st Score
def byScore1(master_proctor):
    return int(master_proctor[2])

# Sorting function by 2nd Score
def byScore2(master_proctor):
    return int(master_proctor[3])

# Sorting function by 3rd Score
def byScore3(master_proctor):
    return int(master_proctor[4])

# Shuffle up the top selections
def shuffleTop(mpList, index):
    val = mpList[0][index] # Which score?
    until = 0
    for i in range(len(mpList)):
        if (mpList[i][index] == val): until = until + 1
        else: break
    # Shuffle the similar top ones so that its fairly random
    topMPs = mpList[:until]
    mpList = mpList[until:]
    random.shuffle(topMPs)
    topMPs.extend(mpList)
    return topMPs


# Expected format -> "Organization", "Master Proctor Name", "Session Score 1", "Session Score 2", "Session Score 3", "Proctor Group Type ES/T"
with open('mp.csv', newline='') as csvfile:
    master_proctors = list(csv.reader(csvfile)) # ,delimiter='\t'


# master_proctors = genRanList(1000)
# writeListAsCSV(master_proctors, 'example.csv')
# writeList(master_proctors, 'list1000.data')
master_proctors = readList('list1000.data')
# sys.exit()
t_master_proctors = list(filter(byT, master_proctors))
es_master_proctors = list(filter(byES, master_proctors))

printList(master_proctors)

print('')

print('SLMC-8 E+S:', end =" ")
s_8_es = math.ceil(int(input())/100)
print('SLMC-8 T:', end =" ")
s_8_t = math.ceil(int(input())/100)
print('SLMC-11 E+S:', end =" ")
s_11_es = math.ceil(int(input())/100)
print('SLMC-11 T:', end =" ")
s_11_t = math.ceil(int(input())/100)
print('SLMC-13 E+S:', end =" ")
s_13_es = math.ceil(int(input())/100)
print('SLMC-13 T:', end =" ")
s_13_t = math.ceil(int(input())/100)

print('')
print('SLMC-8 E+S Allocation')
es_master_proctors.sort(reverse=True, key=byScore1)
preparedData = shuffleTop(es_master_proctors, 2)
selectedMPs = preparedData[:s_8_es]
printList(selectedMPs)
print()

print('SLMC-8 T Allocation')
t_master_proctors.sort(reverse=True, key=byScore1)
preparedData = shuffleTop(t_master_proctors, 2)
selectedMPs = preparedData[:s_8_t]
printList(selectedMPs)
print()

print('SLMC-11 E+S Allocation')
es_master_proctors.sort(reverse=True, key=byScore2)
preparedData = shuffleTop(es_master_proctors, 3)
selectedMPs = preparedData[:s_11_es]
printList(selectedMPs)
print()

print('SLMC-11 T Allocation')
t_master_proctors.sort(reverse=True, key=byScore2)
preparedData = shuffleTop(t_master_proctors, 3)
selectedMPs = preparedData[:s_11_t]
printList(selectedMPs)
print()

print('SLMC-13 E+S Allocation')
es_master_proctors.sort(reverse=True, key=byScore3)
preparedData = shuffleTop(es_master_proctors, 4)
selectedMPs = preparedData[:s_13_es]
printList(selectedMPs)
print()

print('SLMC-13 T Allocation')
t_master_proctors.sort(reverse=True, key=byScore3)
preparedData = shuffleTop(t_master_proctors, 4)
selectedMPs = preparedData[:s_13_t]
printList(selectedMPs)
print()