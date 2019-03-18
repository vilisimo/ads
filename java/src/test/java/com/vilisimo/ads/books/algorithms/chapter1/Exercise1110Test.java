package com.vilisimo.ads.books.algorithms.chapter1;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class Exercise1110Test {

    @Test
    public void transformsTwoRowsThreeColumnsToTable() {
        //given
        var input = new boolean[][] { {true, false, true}, {true, true, true}};

        //when
        var result = Exercise1110.toTable(input);

        assertThat(result, is(" 012\n0* *\n1***"));
    }

    @Test
    public void transformsThreeRowsTwoColumnsToTable() {
        //given
        var input = new boolean[3][2];

        //when
        var result = Exercise1110.toTable(input);

        assertThat(result, is(" 01\n0  \n1  \n2  "));
    }

    @Test
    public void doesNotConstructTablesForZeroWidthHeightArrays() {
        //given
        var zeroWidth = new boolean[2][0];
        var zeroHeight = new boolean[0][2];

        //when
        var wTable = Exercise1110.toTable(zeroWidth);
        var hTable = Exercise1110.toTable(zeroHeight);

        //then
        assertThat(wTable, is(""));
        assertThat(hTable, is(""));
    }
}