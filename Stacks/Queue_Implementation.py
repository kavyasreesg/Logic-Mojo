class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.empty():
            return None

        element = self.queue.pop(0)
        return element

    def empty(self):
        if len(self.queue) <= 0:
            return True
        return False


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
print(queue.queue)
