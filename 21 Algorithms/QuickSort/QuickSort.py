__author__ = 'adelli'

def quickSort(input = []):
    '''Quicksort Algorithm'''
    if input == []: return [] # Base case

    pivot = [element for element in input if element == input[0]]
    leftPartition = [element for element in input if element < pivot[0]]
    rightPartition = [element for element in input if element > pivot[0]]
    return quickSort(leftPartition) + pivot + quickSort(rightPartition)


sortedList = quickSort([2, 5,1, 7, 9, 3, 19, 7, 3, 8])
print(sortedList)

input = []
fh = open('input.txt','r')
for line in fh.readlines():
    input.append(int(line.strip()))

print(quickSort(input))