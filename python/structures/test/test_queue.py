import unittest

from structures.queue import Queue, EmptyQueue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue_adds_item(self):
        self.queue.enqueue("placeholder")

        self.assertEqual(len(self.queue), 1)

    def test_queue_does_not_accept_none(self):
        with (self.assertRaises(TypeError)):
            self.queue.enqueue(None)

    def test_enqueue_increases_size(self):
        self.queue.enqueue("placeholder")
        before = len(self.queue)

        self.queue.enqueue("placeholder 2")

        self.assertEqual(before + 1, len(self.queue))

    def test_dequeue_removes_item(self):
        self.queue.enqueue("placeholder")

        element = self.queue.dequeue()
        self.assertEqual(element, "placeholder")

    def test_dequeue_removes_first_item(self):
        self.queue.enqueue("placeholder")
        self.queue.enqueue("placeholder 2")

        self.assertEqual(self.queue.dequeue(), "placeholder")

    def test_dequeue_decreases_size(self):
        self.queue.enqueue("placeholder")
        before = len(self.queue)

        self.queue.dequeue()

        self.assertEqual(len(self.queue) + 1, before)

    def test_peek_returns_first_element(self):
        self.queue.enqueue("placeholder")
        self.queue.enqueue("placeholder 2")

        element = self.queue.peek()

        self.assertEqual(element, "placeholder")

    def test_peek_does_not_decrease_size(self):
        self.queue.enqueue("placeholder")
        size = len(self.queue)

        self.queue.peek()

        self.assertEqual(len(self.queue), size)

    def test_peek_throws_error_when_queue_is_empty(self):
        with self.assertRaises(EmptyQueue):
            self.queue.peek()

    def test_is_empty_on_empty_queue(self):
        self.assertTrue(self.queue.is_empty())

    def test_is_empty_on_not_empty_queue(self):
        self.queue.enqueue("placeholder")

        self.assertFalse(self.queue.is_empty())

    def test_iteration_starts_from_first_item(self):
        self.queue.enqueue("placeholder")
        self.queue.enqueue("placeholder 2")

        self.assertEqual(next(self.queue), "placeholder")

    def test_iteration_goes_from_head_to_tail(self):
        self.queue.enqueue("one")
        self.queue.enqueue("two")
        next(self.queue)

        self.assertEqual(next(self.queue), "two")

    def test_raises_stop_iteration(self):
        self.queue.enqueue("one")
        next(self.queue)

        with self.assertRaises(StopIteration):
            next(self.queue)
