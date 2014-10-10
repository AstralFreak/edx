'''Queue'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

class Queue(object):
    '''
    Queue of objects
    '''
    def __init__(self):
        '''
        Create an empty queue
        :return: Queue
        '''
        self.queue = []

    def insert(self, value):
        '''
        Insert an element at the end of the queue
        :param value: Element to be inserted
        '''
        self.queue.append(value)

    def remove(self):
        '''
        Remove the first element of the queue
        :return: First element of the queue
        '''
        if len(self.queue) > 0:
            item = self.queue[0]
            self.queue.remove(item)
            return item
        else:
            raise ValueError()