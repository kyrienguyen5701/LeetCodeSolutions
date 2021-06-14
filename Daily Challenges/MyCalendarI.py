'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''

import bisect

class MyCalendar:
    def __init__(self):
        self.schedules = []

    def book(self, start, end):
        if end <= start:
            return False
        i = bisect.bisect_right(self.schedules, start)
        if i % 2:            # start is in some stored interval
            return False
        j = bisect.bisect_left(self.schedules, end)
        if i != j:
            return False
        self.schedules[i:i] = [start, end]
        return True

'''
Runtime: 192 ms - 96.66%
Memory: 15 MB - 39.79%
'''

'''
Comment: First time using bisect Lib
'''