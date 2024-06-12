This is a metafont for computer braille for 8-dot displays.

It happens to be that Freedom Scientific versus Orbit Research have minor differences in how 8-dot braille is rendered. I think Orbit Research made a mistake in mapping it; because when I first mapped it, I got Freedom Scientific's mapping by following the most logical way of extending 6-dot. But Orbit Research displays deviate from this, and have an exception where DEL is swapped with "_"; and it looks like a mistake. I followed the Orbit Research way of mapping it, before I actually got an FS Focus 80. So, I need to do this in code, because it's far too much work to do it manually.

So far, I just have printable ASCII mapped; but I will continue and get all 256 values mapped. If the mapping is a permutation, then it permits the reading of binary data completely normally. There is a braille space, that has to be the cell size, a literal tab (visually seen), and the same for CR and LF. There is even no issue in printing the NUL byte.

The c8brl.mf file is a Go template to get rid of the repetitive code in the mf file.
