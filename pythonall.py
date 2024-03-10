##Python- Question: 1
from pprint import pprint

data = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}

def a_particular_style(data):
    ret = {}
    for k, v in data.items():
        if isinstance(v, dict):
            d = a_particular_style(v)
            ret.update(d)
            ret[k] = list(reversed(d))
        else:
            ret[k] = [v]
    return ret

pprint(a_particular_style(data))
#Python- Question: 2

def ok(v,x,c):
    n=len(v)
    count=1
    d=v[0]
    for i in range(1,n):
        if(v[i]-d>=x):
            d=v[i]
            count=count+1
        else:
            continue
    if(count>=c):
        return True

    return False

# Function to find the maximum possible
# minimum distance between two cows
def aggressive_cows(v,n,k):
    ans=-1
    maxi=0
    for i in range(n):
        maxi=max(maxi,v[i])

    # Loop from 1 to max limit of the
    # barn length (here = 10^9)

    for i in range(1,maxi+1):
        if(ok(v,i,k)):
            ans=i
        else:
            break

    return ans

# Driver code
K=3
arr=[1,2,4,8,9]
N=len(arr)

# Function call
ans=aggressive_cows(arr,N,K)
print(ans)
##Python- Question: 3
height,width=list(map(int,input().split()))
j=1
for i in range(height):
    if i<height//2 :
      print((".|."*j).center(width,"-"))
      j+=2
    elif i==height//2:
        print("WELCOME".center(width,"-"))
    elif i>height//2 :
      j-=2
      print((".|."*j).center(width,"-"))
      ## python question-3.1
      height,width=list(map(int,input().split()))
j=1
for i in range(height):
    if i<height//2 :
      print((".|."*j).center(width,"-"))
      j+=2
    elif i==height//2:
        print("WELCOME".center(width,"-"))
    elif i>height//2 :
      j-=2
      print((".|."*j).center(width,"-"))
      ## python question-4
      class Pair:
    def __init__(self, x, y):
        self.index1 = x
        self.index2 = y
 
# Function to find the all the unique quadruplets
# with the elements at different indices
def GetQuadruplets(nums, target):
    # Store the sum mapped to a list of pair indices
    map = {}
 
    # Generate all possible pairs for the map
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # Find the sum of pairs of elements
            sum = nums[i] + nums[j]
 
            # If the sum doesn't exist then update with the new pairs
            if sum not in map:
                map[sum] = [Pair(i, j)]
            # Otherwise, add the new pair of indices to the current sum
            else:
                map[sum].append(Pair(i, j))
 
    # Store all the Quadruplets
    ans = set()
 
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            lookUp = target - (nums[i] + nums[j])
 
            # If the sum with value (K - sum) exists
            if lookUp in map:
                # Get the pair of indices of sum
                temp = map[lookUp]
 
                for pair in temp:
                    # Check if i, j, k and l are distinct or not
                    if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
                        l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
                         
                        # Sort the list to avoid duplicacy
                        l1.sort()
                         
                        # Update the set
                        ans.add(tuple(l1))
 
    # Print all the Quadruplets
    print(*reversed(list(ans)), sep = '\n')
 
# Driver Code
arr = [1, 0, -1, 0, -2, 2]
K = 0
GetQuadruplets(arr, K)
## SQL QUESTION-1
### SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races)
## sql question-2
### select * from test_a except select * from test_b; 
## sql question-3
Select
   u.user_id,
   username,
   training_id,
   training_date,
   count (user_training_id) AS count
From users u JOIN training_details t ON t.user_id= u.user_id
Group By user_id, 
         username, 
         training_id,
         training_date
Having count(user_training_ id) > 1
Order By training_date DESC;
## question-4-sql
SELECT *
FROM YourTableName
LIMIT 3;
## question-05-deeplearning
Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {'Height': [170, 182, 175, 168, 180, 173, 160, 178],
        'Weight': [65, 72, 70, 58, 75, 62, 50, 68]}

df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation = df['Height'].corr(df['Weight'])

# Print correlation coefficient
print("Correlation between Height and Weight:", correlation)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Height'], df['Weight'])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Correlation between Height and Weight')
plt.grid(True)
plt.show()



