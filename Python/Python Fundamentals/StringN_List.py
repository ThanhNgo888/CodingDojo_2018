# visit docs.python.org
#1. Find and Replace built-in methods
words = "It's thanksgiving day. It's my birthday, too!"
#find string method
#the position of the first instance of the word "day" is 18
print words.find("day")#day is a string object
print words.replace("day", "month")

#2. Min and Max
x = [2,54,-2,7,12,98]
print (min(x))
print (max(x))

#3. First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[-1]
y = x[0], x[-1]
print y

#4. New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort();
print "Sorted list: ", x
half = len(x)/2 #split a list into half
print x[:half], x[half:]
firstHalf =x[:half]
print firstHalf
secondHalf = x[half:]
secondHalf.insert(0,firstHalf)
print "New List: ",secondHalf
