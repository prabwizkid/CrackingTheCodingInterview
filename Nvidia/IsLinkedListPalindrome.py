# LinkedList Palindrome 

# Implement function is_palindrome() to check if a linked list is a palindrome
# Return true if palindrome… false if not

# Example:
# 1 -> 2 -> 3 -> 2 -> 1 is a palindrome
# 1 -> 2 -> 4 -> 3 -> 1 is not

# Input: head of linked list
# Output: true/false

def is_pali(head):
    x_p = head
    y_p = head
    temp = head

    mid_node = None

    if (head.next != None):
        while (x_p.next != None):
            push(Stack(), x_p.next)
            x_p = x_p.next.next
            y_p = y_p.next

        if (x_p != None):
            mid_node = y_p
            y_p = y_p.next

        second_half = y_p

        while (second_half.next != None):
            if (second_half.next != pop(Stack())):
                return False

    return True




