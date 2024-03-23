import random


#Generate 500 random numbers between 0 and 10000
list = random.sample(range(0, 10000), 10)
print(list)


#sort the list via bubble sort
def bubble_sort(list):
    for x in range(len(list)):
        i=0
        while i < (len(list)-1):
            if list[i]>list[i+1]:
                list[i], list[i+1]  = list[i+1], list[i]
            i = i+1
    print(list)

bubble_sort(list)


