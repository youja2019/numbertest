import random, timeit, numpy as np


def insertion_sort1(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nxt_element = arr[i]
        # Compare the current element with next one

        while (arr[j] > nxt_element) and (j >= 0):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = nxt_element
        
def insertion_sort2(arr):
   for index in range(1,len(arr)):
     currentvalue = arr[index]
     position = index

     while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1

     arr[position]=currentvalue


arrMaster = []
for i in range(100):
    arrMaster.append(random.sample(range(1, 1001), 1000))

test1_times = []
test2_times = []


print("test 1")
for i in arrMaster:  # first method
    testArr = i

    s = timeit.default_timer()
    insertion_sort1(testArr)
    e = timeit.default_timer()
    test1_times.append(e - s)
    print(e - s)

print("\ntest 2")

for i in arrMaster:  # second method
    testArr = i

    s = timeit.default_timer()
    insertion_sort2(testArr)
    e = timeit.default_timer()
    test2_times.append(e - s)
    print(e - s)

# prints relevant info
print("test 1\nmean:", np.mean(test1_times), "\nstandardDev: ", np.std(test1_times, ddof=1), "\ntest2\nmean:", np.mean(test2_times), "\nstandardDev: ", np.std(test2_times, ddof=1))
