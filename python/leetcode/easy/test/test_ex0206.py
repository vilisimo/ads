from leetcode.easy.ex0206 import (
    InitialIterativeSolution,
    RecursiveSolution,
    ListNode,
)


class TestInitialIterativeSolution:
    def test_recognizes_null_node(self):
        assert not InitialIterativeSolution().reverseList(None)

    def test_reverses_one_node_list(self):
        root = ListNode(val=1)

        result = InitialIterativeSolution().reverseList(root)

        assert result == root
        assert not result.next

    def test_reverses_two_node_list(self):
        n1 = ListNode(val=1)
        root = ListNode(val=1, next=n1)

        result = InitialIterativeSolution().reverseList(root)

        assert result == n1
        assert result.next == root
        assert not result.next.next

    def test_reverses_three_node_list(self):
        n2 = ListNode(val=1)
        n1 = ListNode(val=1, next=n2)
        root = ListNode(val=1, next=n1)

        result = InitialIterativeSolution().reverseList(root)

        assert result == n2
        assert result.next == n1
        assert result.next.next == root
        assert not result.next.next.next


class TestRecursiveSolution:
    def test_recognizes_null_node(self):
        assert not RecursiveSolution().reverseList(None)

    def test_reverses_one_node_list(self):
        root = ListNode(val=1)

        result = RecursiveSolution().reverseList(root)

        assert result == root
        assert not result.next

    def test_reverses_two_node_list(self):
        n1 = ListNode(val=1)
        root = ListNode(val=1, next=n1)

        result = RecursiveSolution().reverseList(root)

        assert result == n1
        assert result.next == root
        assert not result.next.next

    def test_reverses_three_node_list(self):
        n2 = ListNode(val=1)
        n1 = ListNode(val=1, next=n2)
        root = ListNode(val=1, next=n1)

        result = RecursiveSolution().reverseList(root)

        assert result == n2
        assert result.next == n1
        assert result.next.next == root
        assert not result.next.next.next
