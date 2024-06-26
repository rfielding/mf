package main

import (
	"os"
	"fmt"
	"text/template"
)

var brailleAsciiPattern = []int{
        0b00000000, 0b00101110, 0b00010000, 0b00111100, 0b00101011, 0b00101001, 0b00101111, 0b00000100, 0b00110111, 0b00111110, 0b00100001, 0b00101100, 0b00100000, 0b00100100, 0b00101000, 0b00001100,
        0b00110100, 0b00000010, 0b00000110, 0b00010010, 0b00110010, 0b00100010, 0b00010110, 0b00110110, 0b00100110, 0b00010100, 0b00110001, 0b00110000, 0b00100011, 0b00111111, 0b00011100, 0b00111001,
        0b00001000, 0b00000001, 0b00000011, 0b00001001, 0b00011001, 0b00010001, 0b00001011, 0b00011011, 0b00010011, 0b00001010, 0b00011010, 0b00000101, 0b00000111, 0b00001101, 0b00011101, 0b00010101,
        0b00001111, 0b00011111, 0b00010111, 0b00001110, 0b00011110, 0b00100101, 0b00100111, 0b00111010, 0b00101101, 0b00111101, 0b00110101, 0b00101010, 0b00110011, 0b00111011, 0b00011000, 0b00111000,
}

// When looking at 0x20 through 0x5F as 6-dot, mask off dot 7 first,
// as there are only upper-case letters in braille ascii
var braillePerm = make([]int, 256)

func brailleInit() {
        // Copy in the standard braille ascii patern
        for i := 0; i < 64; i++ {
                braillePerm[0x20+i] = brailleAsciiPattern[i]
        }
        // Flip the case of the alphabet
        //for i := 0x41; i <= 0x5A; i++ {
        for i := 0x40; i <= 0x60; i++ {
                braillePerm[i] = braillePerm[i] ^ 0x40
        }
        // Copy lower half of standard to cover control codes
        for i := 0; i < 32; i++ {
                braillePerm[i] = (braillePerm[i+0x20]) ^ 0x40
        }
        // Copy upper half of standard to cover upper case
        for i := 0; i < 32; i++ {
                braillePerm[0x60+i] = braillePerm[0x40+i] ^ 0x40
        }
        // Swap 124 and 127 the underscore and delete,
        // a strange exception logically, but I see it in real terminals
	// without it, there are certain things that you cant write
        braillePermTmp := braillePerm[0x7F]
        braillePerm[0x7F] = braillePerm[0x5F]
        braillePerm[0x5F] = braillePermTmp

        // Duplicated it all in high bits
        for i := 0; i < 128; i++ {
                braillePerm[0x80+i] = braillePerm[i] ^ 0x80
        }
        // Reverse mapping
        for i := 0; i < 256; i++ {
                asciiPerm[braillePerm[i]] = i
                present[i]++
        }
        // Panic if codes are missing or duplicated
        for i := 0; i < 256; i++ {
                if present[i] != 1 {
                        panic(fmt.Sprintf("inconsistency at %d", i))
                }
        }

}

var asciiPerm = make([]int, 256)
var present = make([]int, 256)


func main() {
	// Make the ascii to dots tables
	brailleInit();
	tmpl, err := template.ParseFiles("c8brl.mf.tmpl")
	if err != nil {
		panic(fmt.Sprintf("could not parse template: %v", err))
	}
	err = tmpl.Execute(os.Stdout, braillePerm)
	if err != nil {
		panic(fmt.Sprintf("could not execute template: %v", err))
	}
}

