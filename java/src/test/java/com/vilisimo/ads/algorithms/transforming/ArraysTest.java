package com.vilisimo.ads.algorithms.transforming;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class ArraysTest {

    @Test
    public void transformsTwoRowsThreeColumnsToTable() {
        //given
        var input = new boolean[2][3];
        input[0][0] = true;
        input[0][1] = false;
        input[0][2] = true;
        input[1][0] = true;
        input[1][1] = true;
        input[1][2] = true;

        //when
        var result = Arrays.toTable(input);

        assertThat(result, is(" 012\n0* *\n1***"));
    }

    @Test
    public void transformsThreeRowsTwoColumnsToTable() {
        //given
        var input = new boolean[3][2];

        //when
        var result = Arrays.toTable(input);

        assertThat(result, is(" 01\n0  \n1  \n2  "));
    }

    @Test
    public void doesNotConstructTablesForZeroWidthHeightArrays() {
        //given
        var zeroWidth = new boolean[2][0];
        var zeroHeight = new boolean[0][2];

        //when
        var wTable = Arrays.toTable(zeroWidth);
        var hTable = Arrays.toTable(zeroHeight);

        //then
        assertThat(wTable, is(""));
        assertThat(hTable, is(""));
    }
}