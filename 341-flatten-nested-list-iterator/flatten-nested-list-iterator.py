# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.stack = []
        self.create_stack()
    
    def create_stack(self):
        for i in range(len(self.nestedList)-1, -1, -1):
            self.stack.append(self.nestedList[i])
        print(self.stack)
    
    def next(self) -> int:
        ele = self.stack.pop()
        return ele.getInteger()        
    
    def hasNext(self) -> bool:
        while self.stack:
            ele = self.stack[-1]
            if ele.isInteger():
                return True
            else:
                self.stack.pop()
                ele_list = ele.getList()
                for i in range(len(ele_list)-1, -1, -1):
                    self.stack.append(ele_list[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())