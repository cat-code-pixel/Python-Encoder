# Cryptography Program

import random

IL = "Hello World" # Input Line

EL = "" # Encoded Line
DL = "" # Decoded Line

A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
",", "!", ".", ";", "?", ":", "~", "`", "-", "_", "/", "<", ">", "|",
"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "] # Characters

# Make Randomized List of Characters
RK = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
",", "!", ".", ";", "?", ":", "~", "`", "-", "_", "/", "<", ">", "|",
"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "] # Characters
random.shuffle(RK)

# Encoder

num = 0

for b in range(len(IL)):

	for c in range(len(A)):

		if IL[b] == A[c]:
			num = c

	EL = EL + RK[num]

# Decoder

num2 = 0

for d in range(len(EL)):

	for e in range(len(RK)):

		if EL[d] == RK[e]:
			num2 = e

	DL = DL + A[num2]

print(IL)
print(EL)
print(RK)
print(DL)