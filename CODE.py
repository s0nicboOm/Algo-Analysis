
from datetime import datetime
import time
import sys
sys.setrecursionlimit(1500000)

from tqdm import tqdm
def timeconvert(q):
    r=q
    r1=r[:19]
    r2=r[20:]
    r2=r2
    epoch = datetime(1900, 1, 1,0,0,0)  
    d1=datetime.strptime(r1,"%Y-%m-%dT%H:%M:%S") # Converting the entire timestamp into seconds
    diff1 = d1-epoch
    b=diff1.total_seconds()
    d2=datetime.strptime(r2,"%H:%M")  # Converting the timezone in terms of seconds
    diff2 = d2-epoch
    a=diff2.total_seconds()
    return b-a # Returning the entire timestamp as a single value with the timezone in seconds
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i][-1] < R[j][-1]:  # Comparison on the basis of the 
                arr[k] = L[i]        # last element in each list
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i][-1]>nlist[i+1][-1]: # Comparison on the basis of the 
                temp = nlist[i]             # last element in each list
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[int((low+high)/2)][-1]     # Selecting the middle element as pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j][-1] <= pivot: # Comparison on the basis of the last element with pivot
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


r = int(input("enter 1:Quicksort 2:Mergesort 3:Bubblesort\n"))
stime=[]
ltime=[]
for u in range(1,6): # Taking total no. of 5 runs where the 1st run is used to get cache
    final=[]
    result=[]
    st=time.time()
    with open("C:/Users/sanch/Desktop/CSC 505/syslog10k.log", "r") as f: 
        data = f.readlines() # Selecting the file from local directory
    totalrows=0
    for line in data:
        if(totalrows==50000):
            break;
        words = line.split()
        totalrows=totalrows+1
        rest=[]
        for i in range(0,len(words)):
            rest.append(words[i])
        final.append(rest)
    et=time.time()
    print("Data Loading time", et-st)
    if(u!=1): # Excluding the first run's data into load time consideration
        ltime.append(et-st)
    for i in range(0,len(final)): # Storing the numerical value of timestamp in
        final[i].append(timeconvert(final[i][0]))  # seconds as the last element
    st=time.time()
    if(r==1):
        quickSort(final,0,len(final)-1)
    if(r==2):
        mergeSort(final)
    if(r==3):
        bubbleSort(final)
    for i in range(0,len(final)): # Removing the numerical value of timestamp 
        final[i]=final[i][:-1] # in seconds from the sorted data   
    for i in final:
        result.append(" ".join(map(str,i)))
    et=time.time()
    print("Data sorting time", et-st)
    if(u!=1): # Excluding the first run's data into sort time consideration
        stime.append(et-st)
    print("total no. of lines =",totalrows)

print("average loading time=", (sum(ltime))/4) # Taking the mean of runs 2 to 5 for load time
print("average sorting time=", (sum(stime))/4) # Taking the mean of runs 2 to 5 for sort time