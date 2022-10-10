#Print leaders in Array
#Leader - An element is leader if it is greater than all the elements to its right side

#Method - 1 : Brute Force (Two Loops)
#Time Complexity - O(n * n)
#Space Complexity - O(1)

def PrintLeadersBruteForce(a,size):
  for i in range(0,size):
      for j in range(i+1,size):
          if a[i] <= a[j]:
              break
      if j == size - 1  and a[i] >= a[j]:
          print(a[i],end =" ")

#Method - 2 : optimal solution 1  but no order:
# set rightmost element as leader
#1. print leader
#2. traverse right -> left and compare next element for greater element
#2. if leader change print max

# Time Complexity - O(n)
# Space Complexity - O(1)

def PrintLeadersOptimal1(a,size):
    leader = a[size - 1]
    print(leader, end= " ")
    for i in range(size - 2,-1,-1):
        if a[i] >= leader :
            leader = a[i]
            print(leader,end= " ")


#Method - 2 : optimal solution 1 with order
# Time Complexity - O(n)
# Space Complexity - O(n)

def PrintLeadersOptimal2(a,size):
    leader = a[size - 1]
    stack = []
    stack.append(leader)
    for i in range(size - 2,-1,-1):
        if a[i] >= leader :
            leader = a[i]
            stack.append(a[i])
    while len(stack) > 0:
        print(stack.pop(),end =" ")

if __name__ == "__main__":
    a = [1,2,3,4,5,8,2,3,2,1]
    #PrintLeadersBruteForce(a,len(a))
    #PrintLeadersOptimal1(a,len(a))
    PrintLeadersOptimal2(a,len(a))



