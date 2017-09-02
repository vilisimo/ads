import unittest

from helpers.contrived import Contrived
from structures.stack import Stack, EmptyStack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_adds_item(self):
        self.stack.push(1)

        self.assertEqual(self.stack._items[0], 1)

    def test_push_does_not_accept_none(self):
        with self.assertRaises(TypeError):
            self.stack.push(None)

    def test_pop_removes_item(self):
        self.stack.push(1)
        item = self.stack.pop()

        self.assertEqual(item, 1)

    def test_pop_on_empty_throws_exception(self):
        with self.assertRaises(EmptyStack):
            self.stack.pop()

    def test_push_increments_index(self):
        start_index = self.stack._index
        self.stack.push(Contrived('a', 1))

        self.assertEqual(start_index, self.stack._index - 1)

    def test_pop_decrements_index(self):
        self.stack.push(1)
        pushed_index = self.stack._index
        self.stack.pop()

        self.assertEqual(self.stack._index + 1, pushed_index)

    def test_len_on_empty_list(self):
        self.assertEqual(len(self.stack), 0)

    def test_len_on_one_element(self):
        self.stack.push('a')

        self.assertEqual(len(self.stack), 1)

    def test_push_and_pop_affect_len(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()

        self.assertEqual(len(self.stack), 1)

    def test_peek_into_empty_stack_throws_exception(self):
        with self.assertRaises(EmptyStack):
            self.stack.peek()

    def test_peek_returns_last_addition(self):
        self.stack.push('a')
        self.stack.push('b')

        self.assertEqual(self.stack.pop(), 'b')

    def test_peek_does_not_decrement_size(self):
        self.stack.push('a')
        self.stack.peek()

        self.assertEqual(len(self.stack), 1)

    def test_is_empty_returns_true_when_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_returns_false_when_not_empty(self):
        self.stack.push(1)

        self.assertFalse(self.stack.is_empty())

    def test_next_picks_last_item(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(next(self.stack), 2)

    def test_iteration_starts_from_the_last_item(self):
        items = [1, 2]
        reversed_items = reversed(items)

        self.stack.push(items[0])
        self.stack.push(items[1])

        for item in self.stack:
            self.assertEqual(item, next(reversed_items))
