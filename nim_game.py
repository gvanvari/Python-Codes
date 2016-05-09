
# NIM GAME, CS 9053 Introduction to Java Assignment 1
# Gaurav Vanvari, gv591, N10100546

import random
from random import choice

# Function to randomly create a number of heaps where the number must either be 3, 5 or 7
def heap_creator():
    global heap_size
    heap_size = random.choice([3,5,7])
    print "Heap of size %d is created" %(heap_size)

# Function to randomly assign the initial number of objects within the heap where the number can be either 9, 11 or 13
def user_play():
    print 'Status of heap currently',
    print heap
    
    print "Enter the heap from you want to take the number"                
    heap_choice = raw_input()
    heap_choice=int(heap_choice)
    print "Enter the value you want to subtract"
    val_choice = raw_input()
    val_choice=int(val_choice)

    # Checking whether user has entered valid Heap number and value to be subtracted is not out of bound
    if ((heap_choice <= heap_size) and (val_choice <= heap[heap_choice-1])):
        heap[heap_choice-1] = heap[heap_choice-1] - val_choice

        print 'Heap status after Gaurav played his turn is:',
        print heap

        # Checking whether all the values in heap are 0 or not
        # The player taking the last object(s) is the winner
        if all(values==0 for values in heap):
            print 'Gaurav won... Exiting now'
            exit()
        else:
            print 'PCs turn'
            computer_play()
    else:
        
        print "Invalid Heap choice or Enter a smaller number"
        user_play()    

def computer_play():
    print 'Status of the heap currently',
    print heap

    sub = 0
    # Using List Comprehension the if-elif construct can be replaced by 1 statement
    heap_comp_choice=random.choice([i for i, value in enumerate(heap) if value!=0])  # if(heap_size == 3):
                                                                                     #    heap_comp_choice = random.choice([0,1,2])
                                                                                     # elif(heap_size == 5):
                                                                                     #     heap_comp_choice = random.choice([0,1,2,3,4])
                                                                                     # elif(heap_size == 7):
                                                                                     #     heap_comp_choice = random.choice([0,1,2,3,4,5,6])
        
    sub = random.randint(1,heap[heap_comp_choice])
    heap[heap_comp_choice] = heap[heap_comp_choice] - sub
    
    print 'Heap status after PC played its turn is ',
    print heap

    # The player taking the last object(s) is the winner
    if all(values==0 for values in heap):
        print 'PC won...  Exiting now'
        exit()
    
    else:
        print 'Your turn please'
        user_play()

# Function to randomly assign the first player, either the human or the computer
def player_assignment():
    global turn
    turn = random.choice([0,1])
    if turn==0:
        print "User Turn"
        user_play()
    else:
        print "PC Turn"
        computer_play()

heap_creator()

heap = []                       
for i in range(heap_size):
    val = random.choice([9,11,13])
    heap.append(val)   
print heap

player_assignment()



