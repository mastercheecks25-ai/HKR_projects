import pickle


def display_menu():
    print("---- Menu ----\n1) Add suspect\n2) Add accomplice\n3) Display all suspects\n4) Find potential accomplices\ns) Statistics\nE) Exit")

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

def count_accomplices(graph):
    count = {}
    for i in graph:
        count[i] = len(graph[i])
    return count

def does_not_know(graph):
    nknow = {}
    for i in graph:
        nknow[i] = set()
        for k in graph:
            if k not in graph[i] and k != i:
                nknow[i].add(k)
    return nknow
                    

            

def main():
    try:
        filename = input("filename: ")
        graph = load_from_file(filename)
        print("*** Graph loaded from file. ***")
    except:
        graph = {}
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
        elif choice == "S":
            ############################grade 3#####################################
            num = 0
            acc = 0
            for i in graph:
                num += 1
                acc += len(graph[i])
            avg = acc/num
            print(f"Total number of suspects         : {num}")
            print(f"Number of accomplices on average : {avg:.1f}")
            #########################grade 4#########################################
            count = count_accomplices(graph)
            for i in count:
                if count[i] > 1:
                    print(f"{i:<10}: {count[i]} accomplices")
                else:
                    print(f"{i:<10}: {count[i]} accomplice")
            #########################grade 5#########################################
            print("Name      : Does not know")
            print("-------------------------")
            nkow = does_not_know(graph)
            for i in nkow:
                print(f"{i:<10}: {", ".join(sorted(nkow[i]))}")

            
    
if __name__ == '__main__':
    main()



