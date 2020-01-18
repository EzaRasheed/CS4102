# CS4102 Fall 2019 -- Homework 8
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: er6qt
# Collaborators: zh2yn, zz9ek
# Sources: Introduction to Algorithms, Cormen
#################################
from collections import defaultdict

class Marriage:
    lukePath = []
    lorelaiPath = []

    def __init__(self):
        return

    def getLukePath(self):
        return self.lukePath

    def getLorelaiPath(self):
        return self.lorelaiPath

    # This is the method that should set off the computation
    # of marriage.  It takes as input a list lines of input
    # as strings.  You should parse that input and then compute
    # the shortest paths that both Luke and Lorelai should take.
    # The class fields of lukePath and lorelaiPath should be filled
    # with their respective paths.  The getters above will be called
    # by the grader script.
    #
    # @return the length of the shortest paths (in rooms)
    def compute(self, file_data):
        # lukePath = []
        # lorelaiPath = []
        t_nodes = file_data[0] # total nodes
        begin_luke, end_luke = file_data[1].split() #get first and last node of Luke from file (1st list)
        begin_lorelai, end_lorelai = file_data[2].split() #get first and last node of Lorelai from file (2nd list)

        if (begin_luke == end_luke) and (begin_lorelai == end_lorelai): # check if beginning and end nodes are the same for both people
            done = True
            self.lukePath.append(end_luke)
            print(len(self.lukePath))
            print("[", end_luke, "]")
            print("[", end_lorelai, "]")

        # Add starting nodes to their respective paths
        self.lukePath.append(int(begin_luke))
        self.lorelaiPath.append(int(begin_lorelai))
        self.lukePath.append(int(end_luke))
        self.lorelaiPath.append(int(end_lorelai))

        #create an Object Graph1 with a list that holds the edges in the graph
        g = Graph1()
        edges = []

        #gets all adjacency lists(adjacent nodes) given in the input file
        for i in file_data[3:]:
            edges.append(i.strip('\n'))

        # form adjacency list
        adj_list = []
        for i in edges:
            if (i != " "):
                adj_list.append(i.split(" "))

        # go through number of vertices
        for vertex in range(0, int(t_nodes)):
            #each line
            for node in adj_list[vertex]:
                g.addEdge(vertex, int(node))
            g.addEdge(vertex, vertex)

        # call breath first search on graph to get respective paths
        self.lukePath, self.lorelaiPath = g.bfs(self.lukePath[0], self.lukePath[1], self.lorelaiPath[0], self.lorelaiPath[1]) #Change
        return len(self.lukePath) # getting "None" output, so just replacing it with a blank space

class Graph1:
    def __init__(self): # graph containing list
        self.graph = defaultdict(list)

    def addEdge(self, frm, to): #graph can append nodes/edges
        self.graph[frm].append(to)

    def printList(self): #printing graph
        return dict.__repr__(self.graph)

    def adjacent(self, frm, to): # checking to see if graph has an edge
        if to in self.graph[frm]:
            return True
        else:
            return False

    # main function where bfs algorithm is implemented to get shortest paths
    def bfs(self, stLuke, enLuke, stLore, enLore):
        Luke_Queue = [[stLuke]]
        Lorelai_Queue = [[stLore]]

        LukePath = list()
        LorelaiPath = list()

        done = False #set to false to check if we have gotten to our ending nodes

        # if (stLuke == enLuke) and (stLore == enLore):
        #     done = True
        #     LukePath.append(enLuke)
        #     print(len(LukePath))
        #     print("[", enLuke, "]")
        #     print("[", enLore, "]")

        while not done: # as long as we have not reached end nodes
            while Luke_Queue: # while queue for Luke is not empty
                Luke_st = Luke_Queue.pop(0) #add first node to path by popping it off
                nodeL = Luke_st[-1]
                adj_nodes = self.graph[nodeL] #get the neighboring(adjacent) nodes

                for adj in adj_nodes: #add all the adjacent nodes to a new list
                    path = list(Luke_st)
                    path.append(adj)
                    Luke_Queue.append(path)
                    if adj == enLuke:
                        current_val = True
                        LukePath.append(path)
                break

            while Lorelai_Queue: # while queue for Lorelai is not empty, do relatively same thing as done for Luke 
                Lorelai_st = Lorelai_Queue.pop(0)
                nodeLo = Lorelai_st[-1]
                adj_nodes_Lorel = self.graph[nodeLo]

                for adj in adj_nodes_Lorel:
                    path = list(Lorelai_st)
                    path.append(adj)
                    Lorelai_Queue.append(path)
                    if adj == enLore:
                        current_val = True
                        LorelaiPath.append(path)
                break

            #conditions that check/ensure that neither is in the other’s line-of-sight

            if len(LukePath) > 0 and len(LorelaiPath) > 0 and current_val:
                current_val = False

                for Luke_vx in LukePath: # for each vertex in Luke's path
                    for Lorelai_vx in LorelaiPath: # and for each vertex in Lorelai's path
                        if len(Luke_vx) == len(Lorelai_vx): # check if they are the same
                            shortest_path = True # True means we have found the shortest length path
                            for node in range(0, len(Luke_vx)):
                                if (self.adjacent(Luke_vx[node], Lorelai_vx[node])):
                                    shortest_path = False
                                    break
                                elif (Luke_vx[node] == Lorelai_vx[node]):
                                    shortest_path = False
                                    break

                            if shortest_path: # if shortest path is found, done is changed to True, and the function is completed
                                done = True
                                (len(Luke_vx))
                                return([*Luke_vx], [*Lorelai_vx]) #Change


                        # if there is a case where Luke's path is longer than Lorelai's, append last node in Lorelai's
                        # path to have both paths be the same length
                        elif len(Luke_vx) > len(Lorelai_vx):
                            LorelaiPath.pop(LorelaiPath.index(Lorelai_vx))
                            break

                        # if there is a case where Lorelai's path is longer than Luke's, append last node in Luke's
                        # path to have both paths be the same length
                        elif len(Luke_vx) < len(Lorelai_vx):
                            LukePath.pop(LukePath.index(Luke_vx))
                            break