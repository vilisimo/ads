import pytest

from leetcode.easy.ex0083 import InitialSolution, ImprovedSolution, ListNode


class TestInitialSolution:
    def test_removes_single_duplicate(self):
        ln3 = ListNode(val=2, next=None)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert not result.next.next

    def test_removes_multiple_same_duplicates(self):
        ln3 = ListNode(val=1, next=None)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_removes_duplicate_by_leaving_single_node(self):
        ln2 = ListNode(val=1, next=None)
        ln1 = ListNode(val=1, next=ln2)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_removes_surrounding_duplicates(self):
        ln5 = ListNode(val=3, next=None)
        ln4 = ListNode(val=3, next=ln5)
        ln3 = ListNode(val=2, next=ln4)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert result.next.next.val == 3
        assert not result.next.next.next

    def test_removes_trailing_duplicates(self):
        ln3 = ListNode(val=2, next=None)
        ln2 = ListNode(val=2, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert not result.next.next

    def test_handles_single_node(self):
        ln1 = ListNode(val=1, next=None)

        result = InitialSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_handles_empty_input(self):
        result = InitialSolution().deleteDuplicates(None)

        assert not result


class TestImprovedSolution:
    def test_removes_single_duplicate(self):
        ln3 = ListNode(val=2, next=None)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert not result.next.next

    def test_removes_multiple_same_duplicates(self):
        ln3 = ListNode(val=1, next=None)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_removes_duplicate_by_leaving_single_node(self):
        ln2 = ListNode(val=1, next=None)
        ln1 = ListNode(val=1, next=ln2)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_removes_surrounding_duplicates(self):
        ln5 = ListNode(val=3, next=None)
        ln4 = ListNode(val=3, next=ln5)
        ln3 = ListNode(val=2, next=ln4)
        ln2 = ListNode(val=1, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert result.next.next.val == 3
        assert not result.next.next.next

    def test_removes_trailing_duplicates(self):
        ln3 = ListNode(val=2, next=None)
        ln2 = ListNode(val=2, next=ln3)
        ln1 = ListNode(val=1, next=ln2)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert result.next.val == 2
        assert not result.next.next

    def test_handles_single_node(self):
        ln1 = ListNode(val=1, next=None)

        result = ImprovedSolution().deleteDuplicates(ln1)

        assert result.val == 1
        assert not result.next

    def test_handles_empty_input(self):
        result = ImprovedSolution().deleteDuplicates(None)

        assert not result
