'''
Defnition: A queue is a ordered list in which insertions are done at done one end (rear) and deletions are done at another end (Front).
The first inserted element is the one to be deleted (FIFO -> First in first out)
'''
from utils.logger import Logger as log

class Queue:
    def __init__(self, limit):
        self.__limit = limit
        self.__queue = [None]*self.__limit
        self.__front = 0
        self.__rear = -1

    # return the size of the queue
    @property
    def size(self):
        return len(self.__queue)

    # returns the queue elements
    @property
    def get(self):
        return self.__queue

    # Queue is empty when size is 0
    @property
    def isEmpty(self): 
        return self.size == 0

    def enqueue(self, item):
        '''
        Algorithm:
        1. Check whether queue is full. If full, display appropriate message
        2. If not,
            a. increment rear by one
            b. Add the element at rear position in the elements array
        '''
        if self.__rear >= self.__limit-1:
            log.error('Queue over flow, {} not inserted'.format(item))
            return
        else:
            self.__rear += 1
            self.__queue[self.__rear] = item
            log.info('{} added to queue, current Queue: {}'.format(item, self.get))

    def dequeue(self):
        '''
        Algorithm:(if no element removed, i.e. with out pop up operation)
        1. Check whether the queue is empty. If it is empty, display appropriate message
        2. If not,
            a. Retrieve data at the front of the queue
            b. Increment front by 1
            c. Return the retrieved data
        Code:
            if self.isEmpty :
                log.error('Queue under flow')
            return
            else:
                element_to_remove = self.__queue[self.__front]
                self.__front += 1;
                return element_to_remove
        '''
        if self.isEmpty :
            log.error('Queue under flow')
            return
        else:
            element_to_remove = self.__queue[self.__front]
            for i in range(self.size-1):
                self.__queue[i] = self.__queue[i+1]
            self.__queue.pop()
            log.info('first enqueued element {} Dequeued from queue, current available elements in queue: {}'.format(element_to_remove, self.get))
            return element_to_remove
