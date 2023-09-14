java_prompt_new='''I want to generate micropython code which can run on arduino board code which follow object oriented programming rules of python using logic of Assembly Language code which is given in plain text format.
I am proving some example retated to this task.

Example 1:
User:
Here is the logic for the given Assembly code:

The code is setting up traffic light control. It declares some constants for the light transition states. Red is the least significant bit, yellow is middle, and green is most significant in each 3 bit group. 

It initializes the lights to all red by outputting 249h. 

It then delays for 5 seconds.

It enters a loop where it:

1. Outputs transition1 which sets north and south to green. 

2. Delays for 2 minutes.

3. Outputs transition2 which sets all to yellow.

4. Delays for 1 minute. 

5. Outputs transition3 which sets east and west to green.

6. Delays for 2 minutes.

7. Outputs transition4 which sets all to yellow. 

8. Delays for 1 minute.

9. Loops back to step 1.

So this implements a typical traffic light sequence, cycling the green lights between the different directions and having intermediate yellow states. The delays control the timing of the light changes. Overall it implements a basic traffic light controller in Assembly.



micropython code:
import machine
import time

# Define constants for light states
RED = 0b0000_0011_0000_1100
YELLOW = 0b0000_0111_1001_1110
GREEN = 0b0000_1000_0110_0001

NORTH_SOUTH_GREEN = GREEN << 4
EAST_WEST_GREEN = GREEN << 8
ALL_YELLOW = YELLOW << 4 | YELLOW << 8

# Initialize the traffic light controller
def init_traffic_light():
    global light_state
    light_state = RED

def set_traffic_light(state):
    machine.out(4, state)

def delay_microseconds(microseconds):
    start = time.ticks_us()
    while time.ticks_diff(time.ticks_us(), start) < microseconds:
        pass

# Main loop
def main():
    while True:
        set_traffic_light(NORTH_SOUTH_GREEN)
        delay_microseconds(120_000_000)
        
        set_traffic_light(ALL_YELLOW)
        delay_microseconds(60_000_000)
        
        set_traffic_light(EAST_WEST_GREEN)
        delay_microseconds(120_000_000)
        
        set_traffic_light(ALL_YELLOW)
        delay_microseconds(60_000_000)

# Initialize and start the traffic light
init_traffic_light()
main()

Example 2:
User:
Here is the logic for the provided Assembly code:

The code includes the emu8086.inc library which provides useful functions like printing strings and numbers. 

It declares segments for data and code. The data segment contains variables to store the number of students, their IDs, marks, and messages to print. The code segment contains the main program logic.

It first sets the data segment and defines some print functions from the library. 

Then it prints a message and reads in the number of students into the variable N.

It prints another message and reads the student IDs into the ID array in a loop. 

Similarly it reads the student marks into the MARKS array.

It sorts the marks in descending order using bubble sort. The outer loop goes N-1 times and inner loop swaps adjacent elements if the current element is less than the next one. The IDs are swapped along with marks to keep them in sync.

After sorting, it prints a header and then prints the ID and marks of each student in a loop.

So in summary, it takes input for student info, sorts the marks, and prints a sorted report. The key steps are reading input, sorting, and printing output.

Micropython code:
import utime

# Define constants and variables
NUM_STUDENTS = 0 
ID = [0] * 100
MARKS = [0] * 100

# Print functions using micropython.py
print = micropython.py.print
print_str = micropython.py.print_str

# Input number of students
print_str('Enter number of students: ')
NUM_STUDENTS = int(input())

# Input IDs
print_str('Enter student IDs:')
for i in range(NUM_STUDENTS):
    ID[i] = int(input())
    
# Input marks   
print_str('Enter student marks:')
for i in range(NUM_STUDENTS):
    MARKS[i] = int(input())

# Bubble sort marks and IDs
for i in range(NUM_STUDENTS-1):
    for j in range(0, NUM_STUDENTS-i-1):
        if MARKS[j] < MARKS[j+1]:
            MARKS[j], MARKS[j+1] = MARKS[j+1], MARKS[j]
            ID[j], ID[j+1] = ID[j+1], ID[j]
            
# Print sorted student info            
print_str('ID\tMarks')
for i in range(NUM_STUDENTS):
    print(ID[i], '\t', MARKS[i])


Now the User will come and will provide business logic, please generate correct and running python code based on the business logic provided by the user as shown in above example. Also include proper comments in the code. 
'''
