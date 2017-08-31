package structures.queue;

import org.junit.Before;
import org.junit.Test;

import java.util.NoSuchElementException;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

public class StackQueueTest {

    private Queue<String> queue;

    @Before
    public void setUp() {
        queue = new StackQueue<>();
    }

    @Test
    public void enqueueAddsElement() {
        queue.enqueue("Placeholder");

        String result = queue.dequeue();

        assertThat(result, is("Placeholder"));
    }

    @Test(expected = NullPointerException.class)
    public void enqueueDoesNotAllowNulls() {
        queue.enqueue(null);
    }

    @Test
    public void dequeueReturnsFirstElement() {
        queue.enqueue("Placeholder");
        queue.enqueue("Another");

        String result = queue.dequeue();

        assertThat(result, is("Placeholder"));
    }

    @Test(expected = NoSuchElementException.class)
    public void dequeuingEmptyQueueThrowsException() {
        queue.dequeue();
    }

    @Test
    public void peekReturnsLastElement() {
        queue.enqueue("Placeholder");

        assertThat(queue.peek(), is("Placeholder"));
    }

    @Test(expected = NoSuchElementException.class)
    public void peekOnEmptyQueueThrowsException() {
        queue.peek();
    }

    @Test
    public void emptyQueueHasSizeZero() {
        assertThat(queue.size(), is(0));
    }

    @Test
    public void addingElementIncrementsSize() {
        int initial = queue.size();

        queue.enqueue("Placeholder");

        assertThat(initial, is(queue.size() - 1));
    }

    @Test
    public void dequeuingElementDecrementsSize() {
        queue.enqueue("Placeholder");
        int initial = queue.size();

        queue.dequeue();

        assertThat(initial, is(queue.size() + 1));
    }

    @Test
    public void emptyQueueIsEmpty() {
        assertTrue(queue.isEmpty());
    }
}