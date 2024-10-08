def display_menu():
    print("Choose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    # TODO: Prompt the user for a value to append to the list
    # Use the append() method to add the value to the list
    # Print the updated list
    val = input('Type a value to add to the list: ')
    lst.append(val)
    print(lst)


def handle_extend(lst):
    # TODO: Prompt the user for values to extend the list (comma-separated)
    # Use the extend() method to add these values to the list
    # Print the updated list
    val = input('Type a value (comma-separated) to extend to the list: ').split(',')
    lst.extend(val)
    print(lst)


def handle_insert(lst):
    # TODO: Prompt the user for an index and a value to insert at that index
    # Use the insert() method to add the value at the specified index
    # Print the updated list
    ind = int(input('Type an index to insert value to the list: '))
    val = input('Type a value to insert to the list at that index: ')
    lst.insert(ind, val)
    print(lst)


def handle_remove(lst):
    # TODO: Prompt the user for a value to remove from the list
    # Use the remove() method to delete the first occurrence of the value
    # Handle the case where the value is not found in the list
    # Print the updated list
    val = input('Type a value to remove from the list: ')
    lst.remove(val)
    print(lst)


def handle_pop(lst):
    # TODO: Prompt the user for an index to pop (optional, leave empty to pop last item)
    # Use the pop() method to remove the item at the specified index or the last item if no index is provided
    # Handle the case where the index is out of range
    # Print the updated list
    val = int(input('Type an index to pop value from the list\nor leave empty to pop the last: '))
    if not val:
        lst.pop()
    else:
        lst.pop(val)
    print(lst)


def handle_clear(lst):
    # TODO: Use the clear() method to remove all items from the list
    # Print the updated list
    lst.clear()
    print(lst)


def handle_index(lst):
    # TODO: Prompt the user for a value to find its index
    # Use the index() method to find the index of the value
    # Handle the case where the value is not found in the list
    # Print the index of the value
    val = input('Type a value to find its index in the list: ')
    if not lst.index(val):
        print('The index isn\'t in the list')
    else:
        print(lst.index(val))


def handle_count(lst):
    # TODO: Prompt the user for a value to count its occurrences in the list
    # Use the count() method to count how many times the value appears in the list
    # Print the count of the value
    val = input('Type a value to count its occurrences in the list: ')
    print(lst.count(val))


def handle_sort(lst):
    # TODO: Use the sort() method to sort the list in ascending order
    # Print the updated list
    lst.sort(key=int)
    print(lst)


def handle_reverse(lst):
    # TODO: Use the reverse() method to reverse the order of the list
    # Print the updated list
    lst.reverse()
    print(lst)


def handle_copy(lst):
    # TODO: Use the copy() method to create a shallow copy of the list
    # Print the copied list
    copy_List = lst.copy()
    print('This is your copy list:', copy_List)


def main():
    initial_values = input('Enter initial list values (comma-separated): ')
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input('Enter your choice (1-12): ')
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print('Exiting the application.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
