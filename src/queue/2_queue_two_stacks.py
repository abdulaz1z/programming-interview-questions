class QueueTwoStacks(object):
    """
    A queue implemented using two stacks.

    https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks
    """
    def __init__(self):
        self.inbox = []  # a stack
        self.outbox = []  # another stack
        self.size = 0

    def enqueue(self, x):
        self.inbox.append(x)
        self.size += 1

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        self.size -= 1
        return self.outbox.pop()

    def get_size(self):
        return self.size

if __name__ == "__main__":
    queue = QueueTwoStacks()
    queue.enqueue("NSBE")
    queue.enqueue("SHPE")
    queue.enqueue("LEHMAN")

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    queue.enqueue("Github")
    print(queue.dequeue())
