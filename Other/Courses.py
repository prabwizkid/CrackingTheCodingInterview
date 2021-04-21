'''

You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"


Sample input 2:
prereqs_courses2 = [
	["Data Structures", "Algorithms"],
	["Algorithms", "Foundations of Computer Science"],
	["Foundations of Computer Science", "Logic"]
]


Sample output 2:
	"Algorithms"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]


Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input


'''

prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

prereqs_courses2 = [
    ["Data Structures", "Algorithms"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Foundations of Computer Science", "Logic"]
]

prereqs_courses3 = [
    ["Data Structures", "Algorithms"]
]

import sys
sys.path.insert(1, '../DataStructures')

from LinkedList import LinkedList
ll = LinkedList()
def sortcourses(courses):
    iteration = True
    for course in courses:
        print(course[0], course[1])
        if ll.isNode(course[0]) and ll.isNode(course[1]):
            print("1--------")
            index0 = ll.getIndex(course[0])
            index1 = ll.getIndex(course[1])
            if index0 + 1 == index1:
                iteration = False
            ll.delete(index0)
            ll.insertAt(course[0], index1)
            ll.show()
        elif ll.isNode(course[1]):
            print("2--------")
            index1 = ll.getIndex(course[1])
            ll.insertAt(course[0], index1)

            ll.show()
        elif ll.isNode(course[1]):
            print("3--------")
            index0 = ll.getIndex(course[1])
            ll.insertAt(course[0], index0 + 1)

            ll.show()
        else:
            print("4--------")
            ll.insertEnd(course[0])
            ll.insertEnd(course[1])

            ll.show()
    for i in range(10):
        print("iteration")
        return sortcourses(courses)

sortcourses(prereqs_courses1)
print("-------- Final ---------")
ll.show()