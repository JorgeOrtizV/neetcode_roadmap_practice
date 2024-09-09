"""
Description:

Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

Example:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

"""

class MinStack:
    def __init__(self):
        self.stack = list()
        # Have an extra stack to keep track of the min elements
        self.minStack = list()

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def push(self, val):
        self.stack.append(val)
        # The top of min stack will be the smallest element at the timestep
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        #return min(self.stack) # I don't think this runs in constant time
        return self.minStack[-1]

if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())