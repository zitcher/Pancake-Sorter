#Pancake AI flipper
#AI should stack from smallest to largest
#You can insert a spatulat and "flip" everything above it (in earlier indecies)
#array of sizes of pancakes stacked randomly

from random import randint

#node of tree, has a value, a parent node, and children node
class Node(object):
        def __init__(self, value, parent):
                self.value = value
                self.parent = parent
                self.children = []

        #when object instance is printed, prints value list
        def __repr__(self):
                return self.getValue().__str__()

        #adds a child node
        def addChild(self, child):
                assert type(child) is Node
                self.getChildren().append(child)

        #shows this branch of the tree all the way up to the original parent
        def showPath(self, branch = []):
                branch.insert(0,self.getValue())
                try:
                        return self.getParent().showPath(branch)
                except AttributeError as error:
                        return branch
        
        def getValue(self):
                return self.value

        def getParent(self):
                return self.parent

        def getChildren(self):
                return self.children

#main control function to find flip steps
def spatulaSortAI(aStack):
        goal = list(aStack) #make goal into a list so it can be sorted
        goal.sort() #we want it sorted bc that's our goal
        goal = tuple(goal) #must be a tuple
        
        startNode = Node(aStack, None)#the top of our tree
        
        #What we can try to do
        fringe = [startNode]

        #what has been tried
        closedSet =  set()
        
        #Our Search
        while(True):
                #If fringe is empty our search has failed
                if not fringe:
                        return "Failed to sort"

                #our strategy
                target = 0 #Breadth Search
                #target = len(fringe)-1 #Depth Search
                #target = randint(0, len(fringe)-1) #dumb search

                #now to carry out expanding target if applicable
                currentNode = fringe[target]
                if(currentNode.getValue() not in closedSet):
                        closedSet.add(currentNode.getValue())
                        #check if we have reached goal before expanding
                        if(currentNode.getValue() == goal):
                                return currentNode.showPath()

                        #expand
                        for i in range(1, len(currentNode.getValue())):
                                       fringe.append(flipNode(currentNode, i))
                                       
                #delete fringe that was expanded
                del fringe[target]   
                
        
#returns a flipped list
def flip(aList, slot):
        toFlip = list(aList[:]) #this is what we have to flip

        try:
                #this flips
                front = 0
                for i in range(slot, -1, -1): #for loop goes from slot to 0
                        toFlip[front], toFlip[i] = toFlip[i], toFlip[front]
                        front+=1
                        if abs(front - i) <= 1:
                                break
                return toFlip
        except IndexError as error:
                print("There is no pancake in the "  + str(slot) + " slot.")
                raise error

#returns a flipped node, linked to parent node
def flipNode(aNode, slot):
        flippedTuple = tuple(flip(aNode.getValue()[:], slot)) #Must convert list to tuple bc sets only take immutable types
        return Node(flippedTuple, aNode)

##test = Node([1,5], None)
##child1 = flipNode(test,1)
##child2 = flipNode(child1,1)
##
##print child2.showPath()
##print child2.unique()


print(spatulaSortAI((2,1,3,5,7,6)))
