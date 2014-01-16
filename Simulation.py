"""
-------------------------------------------------------
simulation.py
-------------------------------------------------------
Author:  Lee Glendenning
ID:      120289190
Email:   glen9190@mylaurier.ca
Version: 2013-01-15
-------------------------------------------------------
"""
class Patron:

    def __init__(self, name, arrival_time):
        self.name = name
        self.arrival_time = arrival_time
        return

class Server:
    def __init__(self, max_service_time, current_patron, end_service_time):
        self.max_service_time = max_service_time
        self.patron = current_patron
        self.end_service_time = end_service_time
        return
