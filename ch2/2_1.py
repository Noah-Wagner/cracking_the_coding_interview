# Cracking the Coding Interview: 2.1
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

sample_values = [1, 2, 3, 1, 2, 4, 5, 5]

def create_linked_list():
    creation_node = ListNode(0)
    ptr = creation_node
    for value in sample_values:
        ptr = ListNode(value)
        ptr = ptr.next
    print("Original Node Values: " + str(sample_values))
    return creation_node

def print_linked_list(head):
    head_vals = []
    while head != None:
        head_vals.append(head.val)
        head = head.next
    print("Printed values: " + str(head_vals))



# ------------- Problem ------------- #

head = create_linked_list()

def remove_duplicates(head):
    node_map = dict()
    orig_head = head
    while head != None:
        key = head.val
        if key in node_map:
            head.val = None
            head = head.next
        else:
            node_map[key] = key
    print("NodeMap: " + str(node_map))
    return orig_head

test = create_linked_list()
print_linked_list(test)
