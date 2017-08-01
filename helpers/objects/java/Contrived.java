package helpers.objects.java;

import java.util.Objects;

/**
 * Class used in searching algorithms to show how collections
 * of custom objects can also be searched.
 */
public final class Contrived implements Comparable<Contrived> {
    private final int number;
    private final char letter;

    public Contrived(int number, char letter) {
        this.number = number;
        this.letter = letter;
    }

    private final int sum() {
        return this.number + this.letter;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }

        if (other == null || this.getClass() != other.getClass())  {
            return false;
        }

        Contrived contrived = (Contrived) other;

        return number == contrived.number && letter == contrived.letter;
    }

    @Override
    public int hashCode() {
        return Objects.hash(number, letter);
    }

    @Override
    public int compareTo(Contrived other) {
        if (this.sum() == other.sum()) {
            return 0;
        } else if (this.sum() > other.sum()) {
            return 1;
        }

        return -1;
    }

    @Override
    public String toString() {
        return "Contrived: " + this.number + ":" + this.letter;
    }
}