#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Element is not an integer, skip silently
            continue
        except IndexError:
            # Index out of range, stop iteration
            break
    print()
    return count

