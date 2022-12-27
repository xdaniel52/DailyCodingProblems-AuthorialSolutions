"""
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. 
An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. 
Return it as a pair of (start, end) timestamps. You can assume 
the building always starts off and ends up empty, i.e. with 0 people inside
"""

def find_busiest_period(data):
    best_end_id = 1
    busiest_count = data[0]['count']
    current_count = data[0]['count']
    for i in range(1,len(data)):
        if data[i]['type'] == "enter":
            current_count+=data[i]['count']
        else:
            if current_count > busiest_count:
                busiest_count = current_count
                best_end_id = i              
            current_count-=data[i]['count']
            
    return (data[best_end_id-1]['timestamp'],data[best_end_id]['timestamp'])        

entries_exits = []
entries_exits.append({"timestamp": 1526579928, "count": 3, "type": "enter"})
entries_exits.append({"timestamp": 1526580382, "count": 2, "type": "exit"})
entries_exits.append({"timestamp": 1526599999, "count": 1, "type": "enter"})
entries_exits.append({"timestamp": 1526600071, "count": 2, "type": "enter"})
entries_exits.append({"timestamp": 1526612384, "count": 2, "type": "exit"})
entries_exits.append({"timestamp": 1526614755, "count": 2, "type": "exit"})

print(find_busiest_period(entries_exits))