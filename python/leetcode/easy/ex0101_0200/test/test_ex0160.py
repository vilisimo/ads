from leetcode.easy.ex0101_0200.ex0160 import ListNode, InitialSolution, TwoPointerSolution


def test_finds_no_intersection_in_single_node_lists():
    top = ListNode(1)
    bot = ListNode(2)

    assert not InitialSolution().getIntersectionNode(top, bot)
    assert not TwoPointerSolution().getIntersectionNode(top, bot)

def test_finds_no_intersection_in_longer_linked_lists():
    top03 = ListNode(12)
    top02 = ListNode(11)
    top02.next = top03
    top01 = ListNode(10)
    top01.next = top02

    bot03 = ListNode(22)
    bot02 = ListNode(21)
    bot02.next = bot03
    bot01 = ListNode(20)
    bot01.next = bot02

    assert not InitialSolution().getIntersectionNode(top01, bot01)


def test_finds_intersection_when_both_lists_are_same_node():
    top = bot = ListNode(1)

    assert InitialSolution().getIntersectionNode(top, bot) == top
    assert TwoPointerSolution().getIntersectionNode(top, bot) == top


def test_finds_intersection_of_short_lists():
    mid = ListNode(1)

    top01 = ListNode(10)
    top01.next = mid
    bot01 = ListNode(20)
    bot01.next = mid

    assert InitialSolution().getIntersectionNode(top01, bot01) == mid
    assert TwoPointerSolution().getIntersectionNode(top01, bot01) == mid


def test_finds_intersection_of_unequal_lists():
    mid = ListNode(1)

    top02 = ListNode(11)
    top02.next = mid
    top01 = ListNode(10)
    top01.next = top02

    bot04 = ListNode(23)
    bot04.next = mid
    bot03 = ListNode(22)
    bot03.next = bot04
    bot02 = ListNode(21)
    bot02.next = bot03
    bot01 = ListNode(20)
    bot01.next = bot02

    assert InitialSolution().getIntersectionNode(top01, bot01) == mid
    assert TwoPointerSolution().getIntersectionNode(top01, bot01) == mid


def test_finds_intersection_of_unequal_lists_and_long_mid():
    mid03 = ListNode(3)
    mid02 = ListNode(2)
    mid02.next = mid03
    mid01 = ListNode(1)
    mid01.next = mid02

    top02 = ListNode(11)
    top02.next = mid01
    top01 = ListNode(10)
    top01.next = top02

    bot04 = ListNode(23)
    bot04.next = mid01
    bot03 = ListNode(22)
    bot03.next = bot04
    bot02 = ListNode(21)
    bot02.next = bot03
    bot01 = ListNode(20)
    bot01.next = bot02

    assert InitialSolution().getIntersectionNode(top01, bot01) == mid01
    assert TwoPointerSolution().getIntersectionNode(top01, bot01) == mid01

def test_finds_no_intersection_when_intersect_at_different_places():
    mid03 = ListNode(3)
    mid02 = ListNode(2)
    mid02.next = mid03
    mid01 = ListNode(1)
    mid01.next = mid02

    top02 = ListNode(11)
    top02.next = mid01
    top01 = ListNode(10)
    top01.next = top02

    bot04 = ListNode(23)
    bot04.next = mid02
    bot03 = ListNode(22)
    bot03.next = bot04
    bot02 = ListNode(21)
    bot02.next = bot03
    bot01 = ListNode(20)
    bot01.next = bot02

    assert InitialSolution().getIntersectionNode(top01, bot01) == mid02
    assert TwoPointerSolution().getIntersectionNode(top01, bot01) == mid02
