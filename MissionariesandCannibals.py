class State:
    def __init__(self,mleft,cleft,boat,mright,cright):
        self.mleft=mleft
        self.cleft=cleft
        self.boat=boat
        self.mright=mright
        self.cright=cright
        self.parent=None
    def isGoal(self):
        if(self.mleft==0 and self.cleft==0):
            return True
        else:
            return False
    def __equ__(self,other):
        if(self.mleft==other.mleft and self.mright==other.mright and self.cleft==other.cleft and self.cright==other.cright and self.boat==other.right):
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.cleft,self.cright,self.boat,self.mleft,self.mright))
    def isvalid(self):
        if(self.mleft>=0 and self.mright>=0 and self.cleft>=0 and self.cright>=0 and (self.mleft==0 or self.mleft>=self.cleft) and (self.mright==0 or self.mright>=self.cright)):
            return True
        else:
            return False
    def sucessor(self,cur_state):
        Children=[]
        if(cur_state.boat=='left'):
            new_state=State(cur_state.mleft,cur_state.cleft-2,"right",cur_state.mright,cur_state.cright+2)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft-2,cur_state.cleft,"right",cur_state.mright+2,cur_state.cright)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft-1,cur_state.cleft-1,"right",cur_state.mright+1,cur_state.cright+1)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft-1,cur_state.cleft,"right",cur_state.mright+1,cur_state.cright)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft,cur_state.cleft-1,"right",cur_state.mright,cur_state.cright+1)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
        else:
            new_state=State(cur_state.mleft,cur_state.cleft+2,"left",cur_state.mright,cur_state.cright-2)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft+2,cur_state.cleft,"left",cur_state.mright-2,cur_state.cright)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft+1,cur_state.cleft+1,"left",cur_state.mright-1,cur_state.cright-1)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft+1,cur_state.cleft,"left",cur_state.mright-1,cur_state.cright)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
            new_state=State(cur_state.mleft,cur_state.cleft+1,"left",cur_state.mright,cur_state.cright-1)
            if(new_state.isvalid()):
                new_state.parent=cur_state
                Children.append(new_state)
        return Children
    def bfs(self):
        initial=State(3,3,"left",0,0)
        if(initial.isGoal()):
            return initial
        frontier=list()
        explored=list()
        frontier.append(initial)
        while frontier:
            state=frontier.pop(0)
            if(state.isGoal()):
                return state
            children=self.sucessor(state)
            for child in children:
                if(child not in frontier) or child not in explored:
                    frontier.append(child)
        return None
    def printsol(self,solution):
        path=[]
        path.append(solution)
        Parent=solution.parent
        while Parent:
            path.append(Parent)
            Parent=Parent.parent
        path.reverse()
        for i in path:
            print(i.mleft," ",i.cleft," ",i.boat," ",i.mright," ",i.cright)
    def start(self):
        Solution = self.bfs()
        self.printsol(Solution)
state=State(3,3,"left",0,0)
state.start()
# import math
# # Missionaries and Cannibals Problem
# class State():
#     def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight,missionaryRight):
#         self.cannibalLeft = cannibalLeft
#         self.missionaryLeft = missionaryLeft
#         self.boat = boat
#         self.cannibalRight = cannibalRight
#         self.missionaryRight = missionaryRight
#         self.parent = None
#     def is_goal(self):
#         if self.cannibalLeft == 0 and self.missionaryLeft == 0:
#             return True
#         else:
#             return False
#     def is_valid(self):
#         if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
#             and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
#             and (self.missionaryLeft == 0 or self.missionaryLeft >=self.cannibalLeft) \
#             and (self.missionaryRight == 0 or self.missionaryRight >=self.cannibalRight):
#                 return True
#         else:
#             return False
#     def __eq__(self, other):
#         return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft== other.missionaryLeft \
#             and self.boat == other.boat and self.cannibalRight ==other.cannibalRight \
#             and self.missionaryRight == other.missionaryRight
#     def __hash__(self):
#         return hash((self.cannibalLeft, self.missionaryLeft, self.boat,self.cannibalRight, self.missionaryRight))
#     def successors(cur_state):
#         children = [];
#         if cur_state.boat == 'left':
#             new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft -2, 'right',
#                             cur_state.cannibalRight, cur_state.missionaryRight + 2)

#     ## Two missionaries cross left to right.
#             if new_state.is_valid():
#                     new_state.parent = cur_state
#                     children.append(new_state)
#                     new_state = State(cur_state.cannibalLeft - 2,cur_state.missionaryLeft, 'right',
#                                     cur_state.cannibalRight + 2, cur_state.missionaryRight)

#     ## Two cannibals cross left to right.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft- 1, 'right',
#                                 cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)

#     ## One missionary and one cannibal cross left to right.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft -1, 'right',
#                                 cur_state.cannibalRight, cur_state.missionaryRight + 1)

#     ## One missionary crosses left to right.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft - 1,cur_state.missionaryLeft, 'right',
#                                 cur_state.cannibalRight + 1, cur_state.missionaryRight)

#     ## One cannibal crosses left to right.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)

#         else:
#             new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft +2, 'left',
#                             cur_state.cannibalRight, cur_state.missionaryRight - 2)

#     ## Two missionaries cross right to left.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft + 2,cur_state.missionaryLeft, 'left',
#                                 cur_state.cannibalRight - 2, cur_state.missionaryRight)

#     ## Two cannibals cross right to left.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft+ 1, 'left',
#                                 cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)

#     ## One missionary and one cannibal cross right to left.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft +1, 'left',
#                                 cur_state.cannibalRight, cur_state.missionaryRight - 1)

#     ## One missionary crosses right to left.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)
#                 new_state = State(cur_state.cannibalLeft + 1,cur_state.missionaryLeft, 'left',
#                                 cur_state.cannibalRight - 1, cur_state.missionaryRight)

#     ## One cannibal crosses right to left.
#             if new_state.is_valid():
#                 new_state.parent = cur_state
#                 children.append(new_state)

#         return children
#     def breadth_first_search():
#         initial_state = State(3,3,'left',0,0)
#         if initial_state.is_goal():
#             return initial_state
#         frontier = list()
#         explored = set()
#         frontier.append(initial_state)
#         while frontier:
#             state = frontier.pop(0)
#             if state.is_goal():
#                 return state
#             explored.add(state)
#             children = successors(state)
#             for child in children:
#                 if (child not in explored) or (child not in frontier):
#                     frontier.append(child)

#         return None
#     def print_solution(solution):
#                 path = []
#                 path.append(solution)
#                 Parent = solution.parent
#                 while Parent:
#                     path.append(Parent)
#                     Parent = Parent.parent
                
#                 for t in range(len(path)):
#                     state = path[len(path) - t - 1]
#                     print ("(" + str(state.cannibalLeft) + "," +str(state.missionaryLeft) \
#                         + "," + state.boat + "," + str(state.cannibalRight) + "," + \
#                         str(state.missionaryRight) + ")")
#     def main(self):
#         solution = self.breadth_first_search()
#         print ("Missionaries and Cannibals solution:")
#         print ("(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
#         self.print_solution(solution)
#     # if called from the command line, call main()
#     if __name__ == "__main__":

#         main(self)