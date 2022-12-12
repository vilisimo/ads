from leetcode.easy.ex0000_0100.ex0021 import ListNode, InitialSolution


def test_merges_two_emtpy_lists():
    result = InitialSolution().mergeTwoLists(list1=None, list2=None)

    assert not result


def test_merges_two_lists_when_only_one_has_nodes():
    head = ListNode(val=1, next=None)

    result = InitialSolution().mergeTwoLists(list1=head, list2=None)
    assert result.val == 1
    assert not result.next

    result = InitialSolution().mergeTwoLists(list1=None, list2=head)
    assert result.val == 1
    assert not result.next


def test_merges_two_lists_with_one_node_each():
    first_head = ListNode(val=1, next=None)
    second_head = ListNode(val=1, next=None)

    result = InitialSolution().mergeTwoLists(list1=first_head, list2=second_head)
    
    assert result.val == 1
    assert result.next.val == 1
    assert not result.next.next


def test_merges_two_lists_in_non_decreasing_order():
    first_head = ListNode(val=2, next=None)
    second_head = ListNode(val=1, next=None)

    result = InitialSolution().mergeTwoLists(list1=first_head, list2=second_head)

    assert result.val == 1
    assert result.next.val == 2
    assert not result.next.next


def test_merges_two_lists_in_non_decreasing_order_when_multiple_nodes_present():
    first_tail = ListNode(val=3, next=None)
    first_head = ListNode(val=1, next=first_tail)
    second_tail = ListNode(val=2, next=None)
    second_head = ListNode(val=1, next=second_tail)

    result = InitialSolution().mergeTwoLists(list1=first_head, list2=second_head)

    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert not result.next.next.next.next
