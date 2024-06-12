This is a metafont for computer braille for 8-dot displays. Prerequisites:

- install a LaTeX distribution, like latex-live
- a Go compiler, which is templating the font file, to make it much much shorter and more consistent

The ASCII table is mapped to dots like this:

|   |     _0|     _1|     _2|     _3|     _4|     _5|     _6|     _7|     _8|     _9|     _A|     _B|     _C|     _D|     _E|     _F|
|---|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 0_| ⡀ <br> NUL | ⡮ <br> SOH | ⡐ <br> STX | ⡼ <br> ETX | ⡫ <br> EOT | ⡩ <br> ENQ | ⡯ <br> ACK | ⡄ <br> BEL | ⡷ <br>  BS | ⡾ <br> TAB | ⡡ <br>  LF | ⡬ <br>  VT | ⡠ <br>  FF | ⡤ <br>  CR | ⡨ <br>  SO | ⡌ <br>  SI |
| 1_| ⡴ <br> DLE | ⡂ <br> DC1 | ⡆ <br> DC2 | ⡒ <br> DC3 | ⡲ <br> DC4 | ⡢ <br> NAK | ⡖ <br> SYN | ⡶ <br> ETB | ⡦ <br> CAN | ⡔ <br>  EM | ⡱ <br> SUB | ⡰ <br> ESC | ⡣ <br>  FS | ⡿ <br>  GS | ⡜ <br>  RS | ⡹ <br>  US |
| 2_| ⠀ <br> SPC | ⠮ <br>   ! | ⠐ <br>   " | ⠼ <br>   # | ⠫ <br>   $ | ⠩ <br>   % | ⠯ <br>   & | ⠄ <br>   ' | ⠷ <br>   ( | ⠾ <br>   ) | ⠡ <br>   * | ⠬ <br>   + | ⠠ <br>   , | ⠤ <br>   - | ⠨ <br>   . | ⠌ <br>   / |
| 3_| ⠴ <br>   0 | ⠂ <br>   1 | ⠆ <br>   2 | ⠒ <br>   3 | ⠲ <br>   4 | ⠢ <br>   5 | ⠖ <br>   6 | ⠶ <br>   7 | ⠦ <br>   8 | ⠔ <br>   9 | ⠱ <br>   : | ⠰ <br>   ; | ⠣ <br>   < | ⠿ <br>   = | ⠜ <br>   > | ⠹ <br>   ? |
| 4_| ⡈ <br>   @ | ⡁ <br>   A | ⡃ <br>   B | ⡉ <br>   C | ⡙ <br>   D | ⡑ <br>   E | ⡋ <br>   F | ⡛ <br>   G | ⡓ <br>   H | ⡊ <br>   I | ⡚ <br>   J | ⡅ <br>   K | ⡇ <br>   L | ⡍ <br>   M | ⡝ <br>   N | ⡕ <br>   O |
| 5_| ⡏ <br>   P | ⡟ <br>   Q | ⡗ <br>   R | ⡎ <br>   S | ⡞ <br>   T | ⡥ <br>   U | ⡧ <br>   V | ⡺ <br>   W | ⡭ <br>   X | ⡽ <br>   Y | ⡵ <br>   Z | ⡪ <br>   [ | ⡳ <br>   \ | ⡻ <br>   ] | ⡘ <br>   ^ | ⠸ <br>   _ |
| 6_| ⠈ <br>   ` | ⠁ <br>   a | ⠃ <br>   b | ⠉ <br>   c | ⠙ <br>   d | ⠑ <br>   e | ⠋ <br>   f | ⠛ <br>   g | ⠓ <br>   h | ⠊ <br>   i | ⠚ <br>   j | ⠅ <br>   k | ⠇ <br>   l | ⠍ <br>   m | ⠝ <br>   n | ⠕ <br>   o |
| 7_| ⠏ <br>   p | ⠟ <br>   q | ⠗ <br>   r | ⠎ <br>   s | ⠞ <br>   t | ⠥ <br>   u | ⠧ <br>   v | ⠺ <br>   w | ⠭ <br>   x | ⠽ <br>   y | ⠵ <br>   z | ⠪ <br>   { | ⠳ <br>  \| | ⠻ <br>   } | ⠘ <br>   ~ | ⡸ <br> DEL |
| 8_| ⣀ <br> UNK | ⣮ <br> UNK | ⣐ <br> UNK | ⣼ <br> UNK | ⣫ <br> UNK | ⣩ <br> UNK | ⣯ <br> UNK | ⣄ <br> UNK | ⣷ <br> UNK | ⣾ <br> UNK | ⣡ <br> UNK | ⣬ <br> UNK | ⣠ <br> UNK | ⣤ <br> UNK | ⣨ <br> UNK | ⣌ <br> UNK |
| 9_| ⣴ <br> UNK | ⣂ <br> UNK | ⣆ <br> UNK | ⣒ <br> UNK | ⣲ <br> UNK | ⣢ <br> UNK | ⣖ <br> UNK | ⣶ <br> UNK | ⣦ <br> UNK | ⣔ <br> UNK | ⣱ <br> UNK | ⣰ <br> UNK | ⣣ <br> UNK | ⣿ <br> UNK | ⣜ <br> UNK | ⣹ <br> UNK |
| A_| ⢀ <br> UNK | ⢮ <br>   ¡ | ⢐ <br>   ¢ | ⢼ <br>   £ | ⢫ <br>   ¤ | ⢩ <br>   ¥ | ⢯ <br>   ¦ | ⢄ <br>   § | ⢷ <br>   ¨ | ⢾ <br>   © | ⢡ <br>   ª | ⢬ <br>   « | ⢠ <br>   ¬ | ⢤ <br>   ­ | ⢨ <br>   ® | ⢌ <br>   ¯ |
| B_| ⢴ <br>   ° | ⢂ <br>   ± | ⢆ <br>   ² | ⢒ <br>   ³ | ⢲ <br>   ´ | ⢢ <br>   µ | ⢖ <br>   ¶ | ⢶ <br>   · | ⢦ <br>   ¸ | ⢔ <br>   ¹ | ⢱ <br>   º | ⢰ <br>   » | ⢣ <br>   ¼ | ⢿ <br>   ½ | ⢜ <br>   ¾ | ⢹ <br>   ¿ |
| C_| ⣈ <br>   À | ⣁ <br>   Á | ⣃ <br>   Â | ⣉ <br>   Ã | ⣙ <br>   Ä | ⣑ <br>   Å | ⣋ <br>   Æ | ⣛ <br>   Ç | ⣓ <br>   È | ⣊ <br>   É | ⣚ <br>   Ê | ⣅ <br>   Ë | ⣇ <br>   Ì | ⣍ <br>   Í | ⣝ <br>   Î | ⣕ <br>   Ï |
| D_| ⣏ <br>   Ð | ⣟ <br>   Ñ | ⣗ <br>   Ò | ⣎ <br>   Ó | ⣞ <br>   Ô | ⣥ <br>   Õ | ⣧ <br>   Ö | ⣺ <br>   × | ⣭ <br>   Ø | ⣽ <br>   Ù | ⣵ <br>   Ú | ⣪ <br>   Û | ⣳ <br>   Ü | ⣻ <br>   Ý | ⣘ <br>   Þ | ⢸ <br>   ß |
| E_| ⢈ <br>   à | ⢁ <br>   á | ⢃ <br>   â | ⢉ <br>   ã | ⢙ <br>   ä | ⢑ <br>   å | ⢋ <br>   æ | ⢛ <br>   ç | ⢓ <br>   è | ⢊ <br>   é | ⢚ <br>   ê | ⢅ <br>   ë | ⢇ <br>   ì | ⢍ <br>   í | ⢝ <br>   î | ⢕ <br>   ï |
| F_| ⢏ <br>   ð | ⢟ <br>   ñ | ⢗ <br>   ò | ⢎ <br>   ó | ⢞ <br>   ô | ⢥ <br>   õ | ⢧ <br>   ö | ⢺ <br>   ÷ | ⢭ <br>   ø | ⢽ <br>   ù | ⢵ <br>   ú | ⢪ <br>   û | ⢳ <br>   ü | ⢻ <br>   ý | ⢘ <br>   þ | ⣸ <br>   ÿ |

The basic idea is 0x20 through 0x5F is all of the old 6-dot standard. We capitalize all the letters by turning on dot 7. Then we copy the lower half of it down to 0x00 to 0x1F, which is mostly control sequences and unprintable obsolete codes, with dot 7 toggled. A similar thing is done with the top half. The top-half is copied into 0x60 to 0x7F, with dot7 toggled.  And then DEL and underscore are swapped, so that everything in the old 6-dot standard is a visible character on a qwerty keyboard. After this is done, an exact copy is made into 0x80 and dot 8 is enabled. Roughly, this is 7-dot Braille over Printable ASCII.  Codes with a dot 8 are more useful for helping with input than with output.


Build and run
===========

```
./clean  # remove all of the build turds. some things do not work without a clean build
./build  # final build artifacts: test.pdf and c8brl.pdf
```

If it worked, then test.pdf will have a paragraph of Braille in it.

!(gilgameshprologue.png)[gilgameshprologue.png]

> TODO: I do not yet know how to convert this to web fonts, where you can make Javascript and HTML apps that show text in computer braille, yet copy/paste as normal ASCII. The Braille font is just plaintext that looks like Braille, which is completely different from Unicode Braille characters.

When working in 6-dot braille, dot 7 and dot 8 are masked off.

In computer Braille, this table is used to map a byte to Unicode Braille dots, like this:

```
echo Phone | brascii
⡏⠓⠕⠝⠑
```

But in UEB, the mapping is not one-to-one. A sequence of dots will coincidentally map to something in the 6-dot range.

```
(base) >echo 'Ph"O' | brascii -sixdot
⠏⠓⠐⠕
```

That is the word "Phone" written in contracted UEB, spelled like "Ph[One]", UEB is a shortcut language for a roughly 20% reduction in the number of characters typed.
It is the standard for English Braille, but most Braille Displays boot up using Computer Braille, which is what the table at the top of this document describes. The main reason to use contracted braille is to stay within 6-dots. But because 6 dots cannot hold enough information to represent 7-bit ASCII, a stream of Braille characters will cause most punctuation to take multiple cells.
