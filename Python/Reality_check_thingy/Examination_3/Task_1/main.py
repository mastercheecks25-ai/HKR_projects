import pickle
from datetime import date

def display_menu():
    print("---- Menu ----\n1) Add suspect\n2) Add accomplice\n3) Display all suspects\n4) Find potential accomplices\nR)Remove suspect\nL)Check remove log\nE) Exit")

def display_suspect(suspect, graph):
    print (f"{suspect}:")
    for i in graph[suspect]:
        print(f"    {i}")

def display_all_suspects(graph):
    print("---- All suspects ----")
    for i in graph:
        print(f"{i}:")
        for j in graph[i]:
            print(f"    {j}")

def find_potential_accomplices(suspect, graph):
    fof = set()
    for i in graph[suspect]:
            if i in graph:
                for j in graph[i]:
                    if j not in graph[suspect] and j != suspect:
                        fof.add(j)
    return{suspect: fof}

def display_potential_accomplices(suspect, graph):
    print("---- Potential accomplices ----")
    print("Already known accomplices:")
    display_suspect(suspect, graph)
    print("")
    print("Potential new accomplices:")
    pos = find_potential_accomplices(suspect, graph)
    print(f"{suspect}:")
    for i in pos[suspect]:
        print(f"    {i}")

def load_from_file(filename):
    with open(filename, "rb") as file:
        graph = pickle.load(file)
    return(graph)

def save_to_file(graph, filename):
    with open(filename, "wb") as file:
        pickle.dump(graph, file)

def unique_names(logs):
    new_log = set()
    for i in logs:
        for j in logs[i]:
            new_log.add(j)
    return(new_log)

def main():
    
    try:
        filename = input("filename: ")
        graph = load_from_file(filename)
        print("*** Graph loaded from file. ***")
        logs = {}
    except:
        graph = {}
        logs = {}
        print("*** File not found. Starting with empty graph. ***")
    while True:
        display_menu()
        choice = input("Your choice: ")
        if choice == "1":
            suspect = input("Suspect: ")
            graph[suspect] = set()
        elif choice == "2":
            suspect = input("Suspect: ")
            accomplice = input("Accomplice: ")
            graph[suspect].add(accomplice)
            if accomplice in graph:
                graph[accomplice].add(suspect)
        elif choice == "3":
            display_all_suspects(graph)
        elif choice == "4": 
            suspect = input("Suspect: ")
            display_potential_accomplices(suspect, graph)
        elif choice == "E" or choice == "e":
            break
        elif choice == "R":
            suspect = input("Suspect: ")
            del graph[suspect]
            for i in graph:
                if suspect in graph[i]:
                    graph[i].remove(suspect)
            if  date.today().strftime("%Y-%m-%d") not in logs:
                logs[date.today().strftime("%Y-%m-%d")] = [suspect]
            else:
                logs[date.today().strftime("%Y-%m-%d")].append(suspect)
            save_to_file(graph, filename)
            save_to_file(logs, "remove_log.ser")
        elif choice == "L":
            try:
                logs = load_from_file("remove_log.ser")
                new_log = unique_names(logs)
                warn = 0
                for j in new_log:
                    count = 0
                    for i in logs:
                        count += logs[i].count(j)

                    if count > 1:
                        warn += count - 1
                if warn > 0:
                    print(f"WARNING: There are {warn} duplicate removals.")
            except:
                print("ERROR: The log file could not be found.")

    
if __name__ == '__main__':
    main()