priority = {'ambulance': 1, 'bus': 2, 'car': 3}

n = int(input("Enter number of vehicles in queue: "))
queue = []
for i in range(n):
    v = input(f"Enter vehicle {i+1} (ambulance/bus/car): ")
    queue.append(v)

new_vehicle = input("Enter new vehicle arriving: ")
queue.append(new_vehicle)
n = len(queue)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if priority[queue[j]] > priority[queue[j + 1]]:
            queue[j], queue[j + 1] = queue[j + 1], queue[j]

print("Updated priority queue:", queue)
#----------output-----------#
Enter number of vehicles in queue: 3
Enter vehicle 1 (ambulance/bus/car): car
Enter vehicle 2 (ambulance/bus/car): car
Enter vehicle 3 (ambulance/bus/car): bus
Enter new vehicle arriving: ambulance
Updated priority queue: ['ambulance', 'bus', 'car', 'car']
Time Complexity: O(n^2)
