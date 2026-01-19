
Custom challenges- Reverse engineering


# 1. Joy division
- crack the provided .elf file to obtain the flag

## Solution:
- so first the file palantinpackflag.txt is being manipulated and is saved in a file flag.txt.
- reading through using ghidra we understand that flipbites manipulates bytes and function expand expands the size of conte. so first we reduce size of content and unflip the bits.
- for even indexes it does bitwise NOT operation and for even index it does bitwise XOR operation starting 0x69 and adding 0x20 every time it occurs
- First it allocates a new buffer which is twice the size of input and then it splits the bytes into two parts. It then combines the parts using & operator with a key in combination which is generated every time it is expanded. The dynamic key starts with 0x69, and then multiplied by 0x20 and then the combination used bvar1, so we swap order of the high and low halfs
- the python script reverses the function by first reducing size of bits followed by flipping them.

```
def reverse_flipBits(data):
    result = bytearray()
    key = 0x69
    var = False

    for b in data:
        if not var:
            result.append(~b & 0xFF)
        else:
            result.append(b ^ key)
            key = (key + 0x20) & 0xFF

        var = not var

    return bytes(result)


def reverse_expand_once(data):
    result = bytearray()
    key = 0x69
    var = False

    for i in range(0, len(data), 2):
        a = data[i]
        b = data[i+1]

        key_hi = (key >> 4) & 0xF
        key_lo = key & 0xF

        if not var:
            lo = a & 0x0F
            hi = b & 0xF0
            original = hi | lo
        else:
            hi = a & 0xF0
            lo = b & 0x0F
            original = hi | lo

        result.append(original)

        key = (key * 0x0B) & 0xFF
        var = not var

    return bytes(result)


def reverse_expand_n_times(data, n):
    for _ in range(n):
        data = reverse_expand_once(data)
    return data

with open("flag (1).txt", "rb") as f:
    expanded = f.read()

step1 = reverse_expand_n_times(expanded, 3)
original = reverse_flipBits(step1)
print(original.decode)
```

## Flag:
```
sunshine{C3A5ER_CR055ED_TH3_RUB1C0N}
```
## Concepts learnt:
- i learnt more about python functions and how to write scripts to obtain flags
- i learn about how to reverse files using ghidra and yunderstand the functions using registers and various other aspects of functions embedded in the assembly language
***


# 2. Worthy.knight
- crack the provided .elf file

## Solution:
- i put the file in hxd and figured out it is a .elf file type so i started reverse engineering by uploading it to ghidra for the output
- first there are various varibles initialised followed by initializing the string variable and then it takes an input after the prompt. The first condition is that it checks if there are 10 characters. Now the catch is the program checks pairwise so first it checks if both characters are alphabetical or else it rejects the input. 
- next it checks if both the characters are uppercase or lowercase so they must be of opposite case and since loop increments by 2 it runs 5 times.
- pair one is when character 1 and chracter 2 is xored to obtain a specific value so by that we find the first two characters of the flag
- pair two checks the next two characters which do they same thing so hence we obtain those characters as well
- in the third pair first the bytes are reversed so 6,5 are being coded using md5 which takes in two bytes and hashes them to a 16 byte output, converts it to lowercase hex characters. It loops over 16 bytes each into two hex characters. Since we need two byte combinations and the ascii of letter range from 65-122 we can create a python script to brute force and get the two letters of the md5 hash.
- the fourth pair and fifth pair are again the same as the first two where two are xored to obtain a specific output so we obtain those letters as well

```
import hashlib

for a in range(122):
    for b in range(122):
        if hashlib.md5(bytes([a, b])).hexdigest() == "33a3192ba92b5a4803c9a9ed70ea5a9c":
            print(a, b, chr(a), chr(b))

```
## Flag:
```
KCTF{NjkSfTYaIi}
```
## Concepts learnt:
- MD5 is a hash function:
it takes a sequence of bytes and produces a fixed 16-byte output. every different 2-byte input gives a completely different 16-byte output. 
## Resources:
-[md5 hash](https://www.avast.com/c-md5-hashing-algorithm)
***


# 3. Time
- crack the provided .elf file

## Solution:
- This is a conventional number guessing game basically and upto us to find out the right number to obtain the flag. The code calls the function time which basically returns current calendar time of the system. This time is measured as the number of seconds passed since 00:00:00
- i researhed about how to compile and run these type of files using gdb and installed it on the system. 
- first we run the time.elf file and then we use break which pauses the code wherever there is an srand rand function so that we can inspect the time anf use it for the answer. Then we run the program and enter that specific number we obtained when we paused the file. The value basically exits in the memroy so we followe that and we use ito and obtain the flag

```
gdb ./time.elf
Reading symbols from ./time...
(No debugging symbols found in ./time)

(gdb) break rand
Breakpoint 1 at 0x400790

(gdb) run
Starting program: /mnt/c/Users/user/downloads/time
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, rand () at ./stdlib/rand.c:26
26      ./stdlib/rand.c: No such file or directory.

(gdb) finish
Run till exit from #0  rand () at ./stdlib/rand.c:26
0x000000000040095f in main ()
Value returned is $1 = 473914306

Value returned is $1 = 473914306
(gdb) continue
Continuing.
Welcome to the number guessing game!
I'm thinking of a number. Can you guess it?
Guess right and you get a flag!
Enter your number: 473914306
Your guess was 473914306.
Looking for 473914306.
You won. Guess was right! Here's your flag:
Flag file not found!  Contact an H3 admin for assistance.
```
## Flag:
```
You won. Guess was right! Here's your flag:
Flag file not found!  Contact an H3 admin for assistance.
```
## Concepts learnt:
- GDB = GNU Debugger. It’s a tool that lets us run a program under controlled conditions, pause it, inspect, change execution state, step through instructions, set breakpoints, and call functions and more.
- Programs can have bugs or behaviour that only appears at runtime. A debugger lets a developer observe the program while it’s running — you can see the live values of variables and the flow of execution.

## Resources:
- [abour gdb](https://www.geeksforgeeks.org/c/gdb-step-by-step-introduction/)


# 4. VeridisQuo
- crack the apk file to obtain the flag

## Solution:
- i used a command line tool called apktool d it unpacked everything and gives us images and things like how the app runs and the .dex files. Apktool makes these .dex files readable by converting them into smali, which is Android’s version of assembly. Then we use a tool called JADX to convert the .dex files directly into Java source code.
- once we open it in jadex we see so many files out of which one files was byuctf and might contain the next steps and it contained a file called main activity

- ```setContentView(R.layout.activity_main);
  Utilities util = new Utilities;
  util.cleanUp();```
	
    this Sets the user interface layout for this activity. It links the Java code to the XML layout file named activity_main.xml, which defines the visual elements of the screen. Then it creates a new instance of the Utilities class, passing this the Utilities class likely contains helper functions and then the cleanUp() method on the Utilities object.(this prompt has been obtain from AI since i had to understand the java code)

- so then i opened utilities.java and it contains many flag parts from 1 to 28 indicating the flag is split into numbered pieces and since in the main function layout was set to activity_main we shall open activity_main.xml file and read it so i search for it and it is present in Res/layout/activity_main.xml and hence we find the characters but are arranged in an order by VALUES OF HOW FAR THEY APPEAR FROM THE BOTTTOM so greated the number higher it appears on the screen.
- so i look through the numbers given for each character given on the screen  using the margin bottom and layout width and accordingly order the charcters as well as using some common sense to obtain a meaningful flag.

## Flag:
```
byuctf{android_piece_0f_c4ke}
```
## Concepts learnt:
- i learnt how to use the tool called apktool which essecntially breaks and provides all the files in an apk file.
- i learnt what and how apk files are generally made where androidManifest.xml is typically the identity card and other things like lib and res contain resoucres and libraries used by the application.
- i learnt about jadex which simplies the output of apktool as well as a software called android studio which is an IDE for building apps and os for the android platform

## Resources:
- [reverse engineering apk](https://medium.com/@prathunan777/reverse-engineering-android-apps-ctf-challenge-baa3a9cbe7d5)
- [about apk](https://www.studytonight.com/android/android-app-package-structure)
***


# 5. Dusty-noob
- open the three rust files to obtain the flag

## Solution:
- at first i put the file in ghidra and the main function has line ```_ZN3std2rt10lang_start17h91ff47afc442db24E``` which is the naming method used for the function ```_ZN10shinyclean4main17h4b15dd54e331d693E``` and this is for the main function shinyclean so we go to that function
- in thet function the abstack_c7 is initialized with byte constants and now these bytes are indivdiually xored with 0x3f and produces another byte array
- now this byte array is compared with PID a process id assigned and checks if it is equal to a specific value then it prints the new bbyte array so basically the new byte array is the flag
- now i took the initiliazed charcaters individually and xored them with 0x3f to obtain the flag
```
7b ^ 3f = 44 - D
5e ^ 3f = 61 - a
48 ^ 3f = 77 - w
58 ^ 3f = 67 - g
7c ^ 3f = 43 - C
6b ^ 3f = 54 - T
79 ^ 3f = 46 - F
44 ^ 3f = 7b - {
79 ^ 3f = 46 - F
6d ^ 3f = 52 - R
0c ^ 3f = 33 - 3
0c ^ 3f = 33 - 3
60 ^ 3f = 5f - _
7c ^ 3f = 43 - C
0b ^ 3f = 34 - 4
6d ^ 3f = 52 - R
60 ^ 3f = 5f - _
68 ^ 3f = 57 - W
0b ^ 3f = 34 - 4
0a ^ 3f = 35 - 5
77 ^ 3f = 48 - H
1e ^ 3f = 21 - !
42 ^ 3f = 7d - }
```

## Flag:
```
DawgCTF{FR33_C4R_W45H!}
```
## Concepts learnt:
- i learnt about rust as a whole and how they are reverse engineered thought this challenge didnt need that much
## Resources:
-[rust reverse engineering](https://medium.com/@InfoSecTube/building-and-reversing-a-simple-rust-binary-a-step-by-step-guide-aeb85adcb024)

***


# 6. Dusty_intermediate
- understanding what the program does
## Solution:
- . Creates channels:
_ZN3std4sync4mpsc7channel - creates a channel ( channel includes a sender that sends inputs to a supposed worker thread and reciever which receives it back, all this data is stored in variables such as 'ustack' 238)

[mpsc::channel() to communicate between threads]

2 Channels were created -

_ZN3std4sync4mpsc7channel...E(&uStack_218) _ZN3std4sync4mpsc7channel...E(&uStack_1d8)

2. Gets our input:
(_ZN3std2io5stdio6_print17he7d505d4f02a1803E(auStack_1a0) : prompts for an input

it then reads the output into a string buffer which is auStack_1b8 , using _ZN3std2io5stdio5Stdin9read_line...E

3. Spawns a Worker Thread (Flag Processing):
It spawns a new thread using _ZN3std6thread5spawn17hc82cf960114777baE(&uStack_168,&uStack_150).

The uStack_150 structure passed to the thread contains the Sender from the first channel (uStack_228) and the Sender from the second channel (uStack_1f8).

It then iterates through the bytes of the user's input and sends each byte (uStack_1) to the first channel's Sender (&uStack_238).

while( true ) { ... _ZN3std4sync4mpsc15Sender$LT$T$GT$4send...E(&uStack_238); }: This loop sends each byte of the user input into the channel to be processed by the worker thread.

Finally, it sends a terminating value (likely 0) to the channel to signal the end of the input: _ZN3std4sync4mpsc15Sender$LT$T$GT$4send17h389f8f24c1d1c8a7E(&uStack_238,0);.

4. Comparing the hardcoded byte array and flag check
The main thread joins the worker thread (_ZN3std6thread19JoinHandle...4join...E). This means it waits for the worker thread to finish its processing.

It then enters a loop to receive bytes from the second channel's Receiver (&uStack_1e8).

while( true ) { ... bStack_cb = _ZN3std4sync4mpsc17Receiver$LT$T$GT$4recv...E(&uStack_1e8); ... _ZN5alloc3vec16Vec$LT$T$C$A$GT$4push...E(auStack_e8); }: The bytes received from the worker thread are collected into a Vec called auStack_e8. This comparison loop shows that the received bytes (auStack_e8), which are the result of the worker thread processing the user's input, must exactly match a hardcoded array of bytes, acStack_a5.
First it checks if i > 0x15 ( i>21), if it is then it fails and breaks, so the input must be =<22) So the input must produce a auStack_e8 that matches acStack_a5 for all indices 0..len-1 and must not exceed the max allowed length

so for the program to give us the flag, we need to input the bytes according to a loop, that transforms input into the values which when compared to the signed bytes

```
acStack_a5[0] = -0x16;
 acStack_a5[1] = -0x27;
 acStack_a5[2] = '1';
 acStack_a5[3] = '\"';
 acStack_a5[4] = -0x2d;
 acStack_a5[5] = -0x1a;
 acStack_a5[6] = -0x69;
 acStack_a5[7] = 'p';
 acStack_a5[8] = '\x16';
 acStack_a5[9] = -0x5e;
 acStack_a5[10] = -0x58;
 acStack_a5[0xb] = '\x1b';
 acStack_a5[0xc] = 'a';
 acStack_a5[0xd] = -4;
 acStack_a5[0xe] = 'v';
 acStack_a5[0xf] = 'h';
 acStack_a5[0x10] = '{';
 acStack_a5[0x11] = -0x55;
 acStack_a5[0x12] = -0x48;
 acStack_a5[0x13] = '\'';
 acStack_a5[0x14] = 0x96;
 auStack_b8 = auVar6;
```
It receives bytes from a channel (these are bytes the other thread sent from the input)
For each received byte b it does:
local_121 = local_121 + b
then it copies a 256-byte table from DAT_00161298 into a local buffer
(memcpy(local_118, &DAT_00161298, 0x100)).
it looks up table[ local_121 ] and sends that byte to the sender (so the other thread receives the mapped byte).
The loop repeats until either the receiver closes or it has processed 0x15 (21) inputs, then it returns.

to invert this process we need to
```table[(0x75 + x) & 0xff] == y
where
x = (idx - 0x75) & 0xff
```
```
from collections import defaultdict

table_hex = [
"0x9f","0xd2","0xd6","0xa8","0x99","0x76","0xb8","0x75","0xe2","0x0e","0x50","0x67","0xc9","0x3a","0xa0","0xb5",
"0x15","0xee","0x59","0xbe","0x7d","0xa3","0xfb","0x51","0xdf","0x7c","0xd9","0x0d","0xe7","0x2d","0xad","0x28",
"0xed","0xdc","0x3d","0x14","0x13","0x79","0xaf","0x27","0xd1","0xd5","0xa1","0xf9","0x37","0xc0","0xef","0x25",
"0x38","0x77","0xff","0x1b","0x40","0x60","0x8f","0x45","0x6f","0x08","0x6d","0xd3","0x35","0x3f","0xb4","0x2f",
"0xd7","0x34","0x5f","0x05","0xbb","0x11","0x3e","0x84","0x5b","0x00","0xf5","0x29","0x36","0x2c","0x63","0x2b",
"0x70","0x68","0x02","0xae","0xc4","0x95","0x10","0x89","0xb0","0x2e","0x55","0xcc","0xbc","0x80","0xa6","0xf3",
"0xd8","0x5a","0x62","0x61","0x9a","0xa5","0xfe","0x3c","0xb2","0x7e","0xbf","0xa7","0xeb","0x41","0x7a","0xfa",
"0x53","0x47","0xdd","0x6b","0x54","0x65","0x9d","0x0b","0x73","0x94","0x81","0x1d","0x4c","0xac","0x46","0xde",
"0x43","0x9c","0xfd","0x7f","0x6a","0x7b","0x07","0x01","0xf7","0xe5","0xb3","0xcd","0x1f","0xc7","0x58","0xe6",
"0x4d","0x31","0x4a","0xd0","0x98","0x93","0x20","0xc5","0x1e","0x6c","0x8c","0x09","0x78","0xbd","0x03","0x23",
"0x82","0xdb","0x12","0x16","0x96","0xc8","0xce","0xf4","0xe0","0xa4","0x04","0xca","0x49","0x87","0xc2","0x32",
"0x6e","0xf1","0x39","0x1c","0x85","0x5e","0x92","0xf8","0xab","0xea","0x8d","0xc1","0x86","0x17","0x8a","0xb1",
"0xf2","0x4f","0xfc","0xe1","0xcb","0xb6","0x42","0xba","0xa9","0x88","0x66","0x4e","0x18","0xf6","0x64","0xaa",
"0x2a","0x8b","0xf0","0xa2","0xec","0x97","0x5c","0xe3","0xcf","0x91","0x0c","0x1a","0x30","0x5d","0x69","0x56",
"0xe4","0x9b","0x0f","0x90","0xc6","0x72","0x48","0x06","0x33","0x9e","0x0a","0x83","0x8e","0x52","0x19","0xe8",
"0x44","0xda","0x26","0xd4","0x3b","0x4b","0x74","0x24","0x22","0xb7","0xc3","0x21","0xe9","0xb9","0x71","0x57"
]


if len(table_hex) != 256:
    print("ERROR: expected 256 bytes in table_hex, got", len(table_hex))
    raise SystemExit(1)

table = [int(x,16) for x in table_hex]


target = [0xEA,0xD9,0x31,0x22,0xD3,0xE6,0x97,0x70,
          0x16,0xA2,0xA8,0x1B,0x61,0xFC,0x76,0x68,
          0x7B,0xAB,0xB8,0x27,0x96]

rev = defaultdict(list)
for idx,val in enumerate(table):
    rev[val].append(idx)

for i,t in enumerate(target):
    if t not in rev:
        print(f"Target byte {i} (0x{t:02x}) not found in table. Aborting.")
        raise SystemExit(1)


acc = 0x75
inputs = []
acc_indices = []
for t in target:
    j = rev[t][0]
    inp = (j - acc) & 0xff
    inputs.append(inp)
    acc_indices.append(j)
print = ''.join(f"\\x{x:02x}" for x in inputs)
```
## Flag:
```
DawgCTF{4LL_RU57_N0_C4R!}
```
***


# 7. Dusty_pro
- understand the file
## Solution:
The program XOR's a 25 byte constant with the 4 bytes of the input int we provide when we run the program repeatedly, then computes sha256 of the result it gets and compares it with a stored ASCII hex.
```
abStack_1b1[0]  = 0xcf;
abStack_1b1[1]  = 0x09;
abStack_1b1[2]  = 0x1e;
abStack_1b1[3]  = 0xb3;
abStack_1b1[4]  = 200;
abStack_1b1[5]  = 0x3c;
abStack_1b1[6]  = 0x2f;
abStack_1b1[7]  = 0xaf;
abStack_1b1[8]  = 0xbf;
abStack_1b1[9]  = 0x24;
abStack_1b1[10] = 0x25;
abStack_1b1[11] = 0x8b;
abStack_1b1[12] = 0xd9;
abStack_1b1[13] = 0x3d;
abStack_1b1[14] = 0x5c;
abStack_1b1[15] = 0xe3;
abStack_1b1[16] = 0xd4;
abStack_1b1[17] = 0x26;
abStack_1b1[18] = 0x59;
abStack_1b1[19] = 0x8b;
abStack_1b1[20] = 200;
abStack_1b1[21] = 0x5c;
abStack_1b1[22] = 0x3b;
abStack_1b1[23] = 0xf5;
abStack_1b1[24] = 0xf6;
```
Since the past 2 challenges had the part of the flag 'DawgCTF{' that gives us 8 bytes and since XOR is reversible we can do:
```
key[0] = 0xcf ^ ord('D') = 0x8b 
key[1] = 0x09 ^ ord('a') = 0x68
key[2] = 0x1e ^ ord('w') = 0x69
key[3] = 0xb3 ^ ord('g') = 0xd4
```
Converting [8b 68 69 d4] to little endian we get 3563677835
and inputing this gives us the flag
## Flag:
```
Dawgctf{4LL_RU57_N0_C4R!}
```
***