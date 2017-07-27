package algorithms.searching.binary.java;

import java.util.Objects;

public final class Contrived implements Comparable<Contrived> {
    private final int number;
    private final char letter;

    public Contrived(int number, char letter) {
        this.number = number;
        this.letter = letter;
    }

    private int sum() {
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
}