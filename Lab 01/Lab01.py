file_input = open("lab1_input.txt", "r")
# read = file_input.line()

Start_node = input("Start node: ")
Destination = input("Destination: ")

main_graph = {}

# added lines in the input file for looping range
total_lines = file_input.readline()
loop_count = int(total_lines)

for i in range(loop_count):
    child_dict = {}
    line = file_input.readline().strip().split()
    # read = file_input.line()

    node = line[0]
    heuristic = int(line[1])

    for i in range(2, len(line), 2):
        child_dict[line[i]] = int(line[i+1])

    update_graph = {"parent_heuristic":heuristic, "child_node":child_dict}
    main_graph[node] = update_graph
    # heuristic ---> parent er h value
    # child_dict ---> sobgular child asee
    # print(child_dict)

p_Queue = [[366, Start_node]]
path_calc = []

while True:
    p_Queue.sort() # sorting for small h val of the child
    hand = p_Queue.pop(0)
    path_calc.append(hand) # path
    # print(p_Queue)


    if hand[1] == Destination:
        break

    child = main_graph[hand[1]]["child_node"]
    # print("child_node--->", child)

    for key, value in child.items():
        # print(key)
        prev_path = (hand[0] - main_graph[hand[1]]["parent_heuristic"])
                                # current H value
        total_path = (prev_path + value)
        gh_x = total_path + main_graph[key]["parent_heuristic"]
                            # Child h value
        p_Queue.append([gh_x, key])  # p_Queue --> all childs of the parent


# Parent finding
if path_calc[-1][1] != Destination:
    print("NO PATH FOUND")

else:
    rev_count = len(path_calc)-1
    path = ""
    for i in range(rev_count, -1, -1):
        if path_calc[rev_count][1] in main_graph[path_calc[i-1][1]]["child_node"]:
            path = f"{path_calc[i-1][1]} --> {path}"
            rev_count = i-1

print("==============================================")
print(f"Path: {path}{path_calc[-1][1]} \nTotal Distance: {path_calc[-1][0]} km")
