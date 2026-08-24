def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move Disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move Disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')
#------------OUTPUT---------#
Enter number of disks: 3
Move Disk 1 from A to C
Move Disk 2 from A to B
Move Disk 1 from C to B
Move Disk 3 from A to C
Move Disk 1 from B to A
Move Disk 2 from B to C
Move Disk 1 from A to C
