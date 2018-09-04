#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.
 
#During the design of your algorithm and your implementation, you should use git:
#Write the text of your algorithm in a file called sequence.py
#Expect the result of git status
#Use git add . to move changes to the staging area.
#Commit your changes with git commit -m “Algorithm written for sequence”
#Then start implementing your algorithm
#During your implementation, make sure you do git status, git add, and git commit regularily.
#You can see a log of all your commits with git log.
#When you have finished your implementation:
#Push your changes to the remote repo with: git push
#Inspect your commits on github

n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 4
t0 = 1
t1 = 2
t2 = 3
tn = 6
if n == 1:
    print(t0)
elif n == 2:
    print(t0)
    print(t1)
else:
    print(t0)
    print(t1)
    print(t2)

while counter < n+1:
    print(tn)
    counter += 1
    if counter < n+1:
        t0 = tn+t1+t2
        print(t0)
        counter += 1
        if counter < n+1:
            t1 = tn+t0+t2
            print(t1)
            counter += 1
            if counter < n+1:
                t2 = tn+t0+t1
                print(t2)
                counter += 1
                tn = t0+t1+t2





