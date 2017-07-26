package searching.linear.java;

import java.util.Objects;

public final class Contrived {
    private final int number;
    private final char letter;

    public Contrived(int number, char letter) {
        this.number = number;
        this.letter = letter;
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
}