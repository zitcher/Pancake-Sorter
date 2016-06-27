#Pancake AI flipper
#AI should stack from smallest to largest
#You can insert a spatulat and "flip" everything above it (in earlier indecies)
#array of sizes of pancakes stacked randomly

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

        #returns true if no ancestors hold the same value
        def unique(self, value = "Replaceme"):
                if(value == "Replaceme"):
                        value = self.getValue()
                if(self.getParent() == None):
                        return True
                if(self.getParent().getValue() ==  value):
                        return False
                return self.getParent().unique(value)
        
        def getValue(self):
                return self.value

        def getParent(self):
                return self.parent

        def getChildren(self):
                return self.children

#main control function to find flip steps
def spatulaSortAI(aStack):
        goal = aStack[:] #make goal into a copy of stack
        goal.sort() #we want it sorted bc that's our goal

        startNode = Node(aStack, None)#the top of our tree
        
        #What we can try to do
        fringe = [startNode]

        #depth left most search
        while(True):
                if not fringe:
                        return "Failed to sort"

                #our strategy is to targest the highest level so
                target = 0

                #now to carry out expanding target if applicable
                currentNode = fringe[target]
                if(currentNode.unique()):
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
        toFlip = aList[:] #this is what we have to flip

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
        flippedList = flip(aNode.getValue()[:], slot)
        return Node(flippedList, aNode)

##test = Node([1,5], None)
##child1 = flipNode(test,1)
##child2 = flipNode(child1,1)
##
##print child2.showPath()
##print child2.unique()


print(spatulaSortAI([5,1,2,3,6,9,33,4]))
