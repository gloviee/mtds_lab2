from array_list import ArrayList

if __name__ == "__main__":
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print("After appends:", lst)

    lst.insert('x', 1)
    print("After insert:", lst)

    lst.delete(2)
    print("After delete:", lst)

    lst.append('a')
    lst.deleteAll('a')
    print("After deleteAll('a'):", lst)

    lst.append('m')
    lst.append('n')
    lst.append('o')
    print("Get index 1:", lst.get(1))

    cloned = lst.clone()
    print("Cloned:", cloned)

    lst.reverse()
    print("Reversed:", lst)

    print("Find first 'n':", lst.findFirst('n'))
    print("Find last 'n':", lst.findLast('n'))

    lst2 = ArrayList()
    lst2.append('z')
    lst2.append('y')
    lst.extend(lst2)
    print("Extended:", lst)

    lst.clear()
    print("Cleared:", lst)
