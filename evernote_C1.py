'''
Implement a circular buffer of size N. Allow the caller to append, remove and list the contents of the buffer. Implement the buffer to achieve maximum performance for each of the operations.

The new items are appended to the end and the order is retained i.e elements are placed in increasing order of their insertion time. When the number of elements in the list elements exceeds the defined size, the older elements are overwritten.

There are four types of commands.

"A" n - Append the following n lines to the buffer. If the buffer is full they replace the older entries.

"R" n - Remove first n elements of the buffer. These n elements are the ones that were added earliest among the current elements.

"L" - List the elements of buffer in order of their inserting time.

"Q" - Quit.

Your task is to execute commands on circular buffer.

Input format

First line of input contains N , the size of the buffer.

A n - append the following n lines to the buffer.

R n - remove first n elements of the buffer.

L - list the buffer.

Q - Quit.

Output format

Whenever L command appears in the input, print the elements of buffer in order of their inserting time. Element that was added first should appear first.
'''

from collections import deque

N = raw_input()
N = int(N)
remove = True
menu = raw_input()

d = deque()

while(menu != 'Q'):
	if(menu[0] == 'A' or menu[0] == 'R'):
		if (len(menu) < 3 or menu[1] != ' '):
			print "Invalid input. Try again"
			menu = raw_input()
			continue
		try:
			lines_to_move = int(menu[2:])
			if lines_to_move < 0:
				print "Invalid input. Try again"
				menu = raw_input()
				continue
		except ValueError:
			print "Invalid input. Try again"
			menu = raw_input()
			continue

		if(menu[0] == 'A'):
			remove = False
		else:
			remove = True
		while(lines_to_move > 0):
			if (not remove):
				line_in = raw_input()
				if(len(d) < N):
					d.append(line_in)
				else:
					d.popleft()
					d.append(line_in)
			else:
				if len(d) > 0:
					d.popleft()
			lines_to_move-=1
	elif(menu == 'L'):
		for item in d:
			print item
	else:
		#Invalid input
		#exit()
		print "Invalid input"
		menu = raw_input()
		continue
	menu = raw_input()
