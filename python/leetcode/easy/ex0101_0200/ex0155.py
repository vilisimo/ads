# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
#   MinStack() initializes the stack object.
#   void push(int val) pushes the element val onto the stack.
#   void pop() removes the element on the top of the stack.
#   int top() gets the top element of the stack.
#   int getMin() retrieves the minimum element in the stack.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation:
#   MinStack minStack = new MinStack();
#   minStack.push(-2);
#   minStack.push(0);
#   minStack.push(-3);
#   minStack.getMin(); // return -3
#   minStack.pop();
#   minStack.top();    // return 0
#   minStack.getMin(); // return -2

# Constraints:
#   -2^31 <= val <= 2^31 - 1
#   Methods pop, top and getMin operations will always be called on non-empty stacks.
#   At most 3 * 10^4 calls will be made to push, pop, top, and getMin

class InitialMinStack:
    def __init__(self):
        self.elements = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        prevmin = self.minimums[-1] if self.minimums else float('inf')
        minval = min(prevmin, val)
        self.minimums.append(minval)

    def pop(self) -> None:
        self.elements.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


class TupleMinStack:
    def __init__(self):
        self.elements = []

    def push(self, val: int) -> None:
        prevmin = self.elements[-1][1] if self.elements else float('inf')
        minval = min(prevmin, val)
        self.elements.append((val, minval))

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1][0]

    def getMin(self) -> int:
        return self.elements[-1][1]
