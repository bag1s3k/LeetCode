array1 = [
    "Mia", 
    "Tim", 
    "Bea", 
    "Zoe", 
    "Jan",
    "Ada",
    "Leo", 
    "Sam",
    "Lou",
    "Max",
    "Ted"
]

array2 = [
    "Mia", 
    "Tim",
    "Bea",
    "Zoe",
    "Sue",
    "Len",
    "Moe",
    "Lou",
    "Rae",
    "Max",
    "Tod"
]

array = array2;
l = len(array)
hashtable = [[] for _ in range(l)]

def hashfunc(s: str, l: int):
    sum = 0
    for c in list(s): 
        sum += ord(c)

    return sum % l

for s in array:
    i = hashfunc(s, l)

    hashtable[i].append(s)

print(hashtable)
print(hashtable[hashfunc("Mia", l)])