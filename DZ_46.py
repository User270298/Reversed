import gc


class Node:
    def __init__(self, data, next=None, last=None):
        self.__data = data
        self.__next: Node = next
        self.__last: Node = last

    def __str__(self):
        return f" {self.__data} : {self.__next} "

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v):
        if v is None:
            raise TypeError("Not use None")
        self.__data = v

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, v):
        if not isinstance(v, type(self)):
            raise TypeError("Is not Node")
        self.__next = v

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, v):
        if not isinstance(v, type(self)):
            raise TypeError("Is not Node")
        self.__last = v

    def del_next(self):
        self.__next = None

    def del_last(self):
        self.__last = None


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head: Node = head
        self.tail: Node = tail
        self.len: int = 0

    def append(self, v) -> Node:
        new_node = Node(v)
        if self.head is None:
            self.head = self.tail = new_node
            self.len += 1
            return new_node
        self.tail.next = new_node
        self.tail = new_node
        new_node.last = self.tail
        self.len += 1
        return new_node

    def pop(self):
        if self.head is None:
            return
        temp_next = self.head
        while temp_next.next.next is not None:
            temp_next = temp_next.next
        temp_next.del_next()
        self.tail = temp_next
        self.len -= 1

    def search(self, v):
        lastbox = self.head
        while lastbox:
            if v == lastbox.data:
                return True
            else:
                lastbox = lastbox.next
        return False

    def replace(self, v, change):
        lastbox = self.head
        while lastbox:
            if v == lastbox.data:
                lastbox.data = change
            else:
                lastbox = lastbox.next
        return v

    def len(self):
        return self.len

    def __str__(self):
        if self.head is None:
            return "тут пусто"
        return self.head.__str__()


class Reversed:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def append_to_start(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
            return new_node
        new_node.next = self.head
        self.head.last = new_node
        self.head = new_node
        return new_node

    def delete_start(self):
        if self.head is None:
            return
        temp = self.head.next
        self.head.del_last()
        self.head = temp


    def __str__(self):
        if self.head is None:
            return "тут пусто"
        return self.head.__str__()


lst = LinkedList()
lst.append(4)
lst.append(33)
lst.append(123)
print(lst)
print(lst.search(12))
lst.replace(1234, 999)
print(lst)
lst.replace(123, 999)
print(lst)
rev = Reversed()
rev.append_to_start(145)
rev.append_to_start(477)
rev.append_to_start(234)
rev.append_to_start(234)
print(rev)
rev.delete_start()
rev.delete_start()
print(rev)
