#!/usr/bin/env python3
'''
Representation of queue that will be used with the conversion for the frames
Locks will also be used to avoid race conditions as well as accidental deletion of
frames and so on
'''

import threading

class queueClass:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(10)

    def put(self, item):
        self.empty.acquire() #lock semaphore
        self.lock.acquire() #lock the lock
        self.queue.append(item) #add our new frames
        self.lock.release() #release the lock
        self.full.release()

    def get(self):
        self.full.acquire() #lock Semaphore
        self.lock.acquire() #lock the lock
        item_popped = self.queue.pop(0) #pop at the first position
        self.lock.release() #release the lock
        self.empty.release() #release the semaphore
        return item_popped

    def markEnd(self):
        self.put('end') #for when we finish the frames we are adding
