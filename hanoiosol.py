"""
The solution implemented below uses the concept of binary conversion of m moves and moving from the most significant bits
to least significant bits. The thing to understand first is that the first peg is considered to be right of the last peg,
 and the last peg is considered to be left of the first peg. 

Disk positions may be determined more directly from the binary (base-2) 
representation of the move number (the initial state being move #0, with all digits 0, and the final state being with all digits 1),
using the following rules:

There is one binary digit (bit) for each disk.
The most significant (leftmost) bit represents the largest disk.
A value of 0 indicates that the largest disk is on the initial peg, 
while a 1 indicates that it's on the final peg (right peg if number of disks is odd and middle peg otherwise).
The bitstring is read from left to right, and each bit can be used to determine the location of the corresponding disk.
A bit with the same value as the previous one means that the corresponding disk is stacked on top the previous disk on the same peg.
(That is to say: a straight sequence of 1s or 0s means that the corresponding disks are all on the same peg.)
A bit with a different value to the previous one means that
the corresponding disk is one position to the left or right of the previous one.
Whether it is left or right is determined by this rule:
Assume that the initial peg is on the left.
Also assume "wrapping" – so the right peg counts as one peg "left" of the left peg, and vice versa.
Let n be the number of greater disks that are located on the same peg
as their first greater disk and add 1 if the largest disk is on the left peg. 
If n is even, the disk is located one peg to the right, 
if n is odd, the disk located one peg to the left (in case of even number of disks and vice versa otherwise).

Time complexity -> 
As it can be seen that convert_bin function calls itself recursively but reduces by 2 in every step so it has a complexity of O(logn)
Coming to the tower of hanoi function , largest_binary_moves runs logn times similarly the moves_binary runs logn times. 
then there are two for loops running individaully for n number of moves. so that makes it O(n)+O(n)i.e O(n).
So the overall complexity of the program is O(n)*O(logn)= O(nlogn). 
"""





import sys

def convert_bin(a):
	string_conv = '01'
	if a < 2:
		return string_conv[a]
	else:
		return convert_bin(a//2) + string_conv[a%2]

def tower_hanoi(n, m): 
    # n = no of disks, m = moves made
    largest_binary_moves = convert_bin((2**n)-1)
    append_this = ''
    moves_binary = convert_bin(m)
    
    for i in range(0, len(largest_binary_moves)-len(moves_binary)):
        append_this += '0'
    
    moves_binary = append_this + moves_binary
        
    target_peg = 0 #Start with left peg
    
    result = [0,0,0]
    
    for i in range(0,len(moves_binary)): 
        #moving from the most significant bit to the least significant bit
        if moves_binary[i] == '1': 
        	# if the value of m is greater than half of the moves that are necessary 
            if n%2 == 1: 
            	# checking the number of disks on stack (whether odd or even) ---> if odd ?
                result[(target_peg+1)%3] += 1 
                # one peg is added to the right of the target peg
                target_peg = (target_peg+2)%3 
                #target peg is left shifted 
                n-=1
            else: 
            	#  ---> if even ?
                result[(target_peg+2)%3] += 1 
                #one peg is added to the right of the target peg
                target_peg = (target_peg+1)%3 
                #target peg is right shifted
                n-=1
        else: 
            result[target_peg] += 1
            n -= 1
            
    return result

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    r = tower_hanoi(n, m)
    print(r[0], r[1], r[2])
