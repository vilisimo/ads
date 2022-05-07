import pytest

from leetcode.easy.ex0203 import DummyNodeSolution, InitialSolution, ListNode


class TestInitialSolution:
    def test_recognizes_empty_node(self):
        assert not InitialSolution().removeElements(None, 1)


    def test_removes_all_elements(self):
        n3 = ListNode(val=1)
        n2 = ListNode(val=1, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert not InitialSolution().removeElements(n1, 1)


    @pytest.mark.parametrize('target', [-1, 0, 4, 99])
    def test_leaves_list_alone_with_non_existent_element(self, target: int):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, target) == n1


    def test_removes_head(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, 1) == n2


    def test_removes_tail(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, 3) == n1
        assert not n2.next


    def test_removes_middle_node(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, 2) == n1
        assert n1.next == n3


    def test_removes_multiple_consecutive_nodes(self):
        n4 = ListNode(val=3)
        n3 = ListNode(val=2, next=n4)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, 2) == n1
        assert n1.next == n4


    def test_removes_multiple_non_consecutive_nodes(self):
        n5 = ListNode(val=4)
        n4 = ListNode(val=2, next=n5)
        n3 = ListNode(val=3, next=n4)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert InitialSolution().removeElements(n1, 2) == n1
        assert n1.next == n3
        assert n3.next == n5


class TestDummyNodeSolution:
    def test_recognizes_empty_node(self):
        assert not DummyNodeSolution().removeElements(None, 1)


    def test_removes_all_elements(self):
        n3 = ListNode(val=1)
        n2 = ListNode(val=1, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert not DummyNodeSolution().removeElements(n1, 1)


    @pytest.mark.parametrize('target', [-1, 0, 4, 99])
    def test_leaves_list_alone_with_non_existent_element(self, target: int):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, target) == n1


    def test_removes_head(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, 1) == n2


    def test_removes_tail(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, 3) == n1
        assert not n2.next


    def test_removes_middle_node(self):
        n3 = ListNode(val=3)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, 2) == n1
        assert n1.next == n3


    def test_removes_multiple_consecutive_nodes(self):
        n4 = ListNode(val=3)
        n3 = ListNode(val=2, next=n4)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, 2) == n1
        assert n1.next == n4


    def test_removes_multiple_non_consecutive_nodes(self):
        n5 = ListNode(val=4)
        n4 = ListNode(val=2, next=n5)
        n3 = ListNode(val=3, next=n4)
        n2 = ListNode(val=2, next=n3)
        n1 = ListNode(val=1, next=n2)

        assert DummyNodeSolution().removeElements(n1, 2) == n1
        assert n1.next == n3
        assert n3.next == n5
