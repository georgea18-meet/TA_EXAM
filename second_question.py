#define two lists
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#define an empty list for storing shared values
c = []

#iterate through one of the lists and check for each element whether it's a shared value or not
'''it checks whether the length of the list is greater than zero because we remove all elements that are
equal to the current element (including that element) in order to avoid duplicates'''
while len(a)>0:

    #we always take the first element because after removing the previous element we end up with the next element
    #being in the index 0
    i = a[0]

    #check whether it exists in the other list as well
    if b.count(i)>0:

        #add it to the list of shared elements
        c.append(i)

    #remove all values equal to i form the first list in order to avoid duplicates
    for j in range(a.count(i)):
        a.remove(i)

print(c)
