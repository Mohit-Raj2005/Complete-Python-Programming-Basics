#sorting a list in ascending and descending order 
#reversing a list

fruits=["banana","mango","papaya","orange","apple"]
print("before sorting:",fruits)
fruits.sort()    #sort() function sorts the list in alpha numeric order (by default ascending order)
print("sorted list:",fruits)


num=[2,5,3,1,4]
print("before sorting:",num)
num.sort()
print("after ascending sort",num)
#sort(reverse=True) this function sorts the list in reverse order
num.sort(reverse=True)
print("after reverse sorting:",num)

#reverse() funcction is used to reverse a list
alpha=["a","b","c","d","e"]
print("before rverse:",alpha)
alpha.reverse()
print("after reverse:",alpha)



