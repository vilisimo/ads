from leetcode.easy.ex0141 import ListNode, InitialSolution, FastSlowSolution


def test_does_not_find_cycle_with_no_nodes():
    assert not InitialSolution().hasCycle(None)
    assert not FastSlowSolution().hasCycle(None)



def test_does_not_find_cycle_with_one_node():
    assert not InitialSolution().hasCycle(ListNode(1))
    assert not FastSlowSolution().hasCycle(ListNode(1))



def test_does_not_find_cycle_with_two_nodes():
    first = ListNode(1)
    second = ListNode(2)
    first.next = second

    assert not InitialSolution().hasCycle(first)
    assert not FastSlowSolution().hasCycle(first)



def test_finds_cycle_with_two_nodes():
    first = ListNode(1)
    second = ListNode(2)
    first.next = second
    second.next = first

    assert InitialSolution().hasCycle(first)
    assert FastSlowSolution().hasCycle(first)


def test_finds_cycle_when_node_points_to_itself():
    first = ListNode(1)
    first.next = first

    assert InitialSolution().hasCycle(first)
    assert FastSlowSolution().hasCycle(first)



def test_finds_cycle_when_node_points_to_its_parent():
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    first.next = second
    second.next = third
    third.next = second

    assert InitialSolution().hasCycle(first)
    assert FastSlowSolution().hasCycle(first)


def test_finds_cycle():
    first = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    assert InitialSolution().hasCycle(first)
    assert FastSlowSolution().hasCycle(first)
