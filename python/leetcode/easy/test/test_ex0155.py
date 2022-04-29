from leetcode.easy.ex0155 import InitialMinStack, TupleMinStack


class TestInitialMinStack:
    def test_pushes_element(self):
        stack = InitialMinStack()
        stack.push(1)

        assert stack.elements[-1] == 1


    def test_pops_element(self):
        stack = InitialMinStack()
        stack.push(1)

        stack.pop()

        assert not stack.elements


    def test_top_element_returns_last_element(self):
        stack = InitialMinStack()
        stack.push(1)
        stack.push(2)

        assert stack.top() == stack.elements[-1]


    def test_returns_minimum_element(self):
        stack = InitialMinStack()
        stack.push(1)
        stack.push(-3)
        stack.push(3)
        stack.push(-5)
        stack.push(0)

        assert stack.getMin() == -5


    def test_handles_combination_of_operations(self):
        stack = InitialMinStack();
        stack.push(-2);
        stack.push(0);
        stack.push(-3);
        assert stack.getMin() == -3

        stack.pop();
        assert stack.top() == 0
        assert stack.getMin() == -2


class TestTupleMinStack:
    def test_pushes_element(self):
        stack = TupleMinStack()
        stack.push(1)

        assert stack.elements[-1][0] == 1


    def test_pops_element(self):
        stack = TupleMinStack()
        stack.push(1)

        stack.pop()

        assert not stack.elements


    def test_top_element_returns_last_element(self):
        stack = TupleMinStack()
        stack.push(1)
        stack.push(2)

        assert stack.top() == stack.elements[-1][0]


    def test_returns_minimum_element(self):
        stack = TupleMinStack()
        stack.push(1)
        stack.push(-3)
        stack.push(3)
        stack.push(-5)
        stack.push(0)

        assert stack.getMin() == -5


    def test_handles_combination_of_operations(self):
        stack = TupleMinStack();
        stack.push(-2);
        stack.push(0);
        stack.push(-3);
        assert stack.getMin() == -3

        stack.pop();
        assert stack.top() == 0
        assert stack.getMin() == -2
