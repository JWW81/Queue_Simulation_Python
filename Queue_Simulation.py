'''
-------------------------------------------------------
queue_simulation
-------------------------------------------------------
Author:  Lee Glendenning
ID:            120289190
Email:      glen9190@wlu.ca
Version: 2013-01-15
-------------------------------------------------------
'''
#imports
from queue_array import Queue
from simulation import Patron
from simulation import Server
import random
import copy

"""
-------------------------------------------------------
line_up
-------------------------------------------------------
Preconditions:
  total_time - user inputted total time for club to remain open (int)
  max_arrival_time - user inputted maximum time between patrons arriving (int)
  max_service_time - user inputted maximum time for bouncer to service patron (int)
  max_queue_size - user inputted cap for lineup due to fire code (int)
  number_servers - user inputted number of bouncers (int)
Postconditions:
   Prints information regarding simulation
-------------------------------------------------------
"""
def line_up2(total_time, max_arrival_time, max_service_time, max_queue_size, number_servers):
    #initialize counters, queue, bool
    q = Queue()
    patron_id = 1
    arriving = 0
    serving = 0
    max_queue = 0
    patrons_served = 0
    total_wait_time = 0
    turned_away = 0
    being_served = []

    #loop through user inputted total_time
    for time in range(0, total_time + 1):
        if time != 0:
            print("Time = {}".format(time))

        #determine when patrons join the queue
        if arriving == time:
            if len(q) == max_queue_size:
                turned_away += 1
            if time != 0 and len(q) < max_queue_size:
                print("  Action: patron {} joins the queue.".format(patron_id))
                patron = Patron(patron_id, copy.deepcopy(time))
                q.insert(patron)
                patron_id += 1
                if len(q) > max_queue:
                    max_queue = len(q)
            arriving += random.randint(1, max_arrival_time)

        #determine when servers finish with patrons
        popped_index = []
        if len(being_served) != 0:
            for i in range(len(being_served)):
                if being_served[i].end_service_time == time:
                    print("  Action: patron {} finishes being served.".format(being_served[i].patron))
                    popped_index.append(i)
                    patrons_served += 1
            if (len(popped_index) != 0):
                for i in range(len(popped_index), 0, -1):
                    being_served.pop(popped_index[i - 1])

        #determine when servers accept new patrons
        if len(being_served) < number_servers and q.is_empty() == False:
            print("  Action: patron {} starts the service.".format(q.peek().name))


            serving = time
            serving += random.randint(1, max_service_time)
            server = Server(max_service_time, q.peek().name, serving)

            being_served.append(server)


            total_wait_time += time - q.peek().arrival_time
            q.remove()

    #display results
    print("Club is now closed")
    print("End simulation")
    print()
    print("The maximum queue size (longest line of patrons): {}".format(max_queue))
    print("The number of patrons turned away: {}".format(turned_away))
    print("The number of patrons served: {}".format(patrons_served))
    print("The number of patrons left in the queue: {}".format(len(q)))
    print("The average time between arrivals (in minutes): {:.1f}".format(total_time / patron_id))
    #if statement to avoid dividing by 0 if no patrons are served
    if patrons_served != 0:
        print("The average wait time in the queue per patron (in minutes): {:.1f}".format(total_wait_time / patrons_served))
    else:
        print("The average wait time in the queue per patron (in minutes): None")
    return
