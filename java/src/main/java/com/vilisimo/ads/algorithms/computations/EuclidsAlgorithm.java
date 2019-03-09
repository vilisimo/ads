package com.vilisimo.ads.algorithms.computations;

/**
 * GCD of two nonnegative integers p and q:
 *  - if q = 0, the answer = p
 *  - if not, divide p by q and take the remainder r
 *  - the answer is the greatest common divisor of q and r
 */
public class EuclidsAlgorithm {

    public static int calculateGcd(int p, int q) {
        if (q == 0) {
            return p;
        }

        return calculateGcd(q, p % q);
    }
}
