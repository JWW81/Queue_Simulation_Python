'''
-------------------------------------------------------
queue_simulation_test
-------------------------------------------------------
Author:  Lee Glendenning
ID:            120289190
Email:      glen9190@wlu.ca
Version: 2013-01-29
-------------------------------------------------------
'''

import queue_simulation

print("Welcome to the After Hours Club.")
print()
print("Please enter the following parameters:")
total_time = int(input("  Total time for simulation (minutes): "))
max_arrival_time = int(input("  Maximum time between patron arrivals (minutes): "))
max_service_time = int(input("  Maximum service time (minutes): "))
max_queue_size = int(input("  Maximum queue size: "))
number_servers = int(input("  Number of servers: "))
print()

queue_simulation.line_up2(total_time, max_arrival_time, max_service_time, max_queue_size, number_servers)
