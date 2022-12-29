def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode=ll.head
        visited=set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next=currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode=currentNode.next
        return ll

def nthtolast(ll,n):
    pointer1=ll.head
    pointer2=ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next

    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1


