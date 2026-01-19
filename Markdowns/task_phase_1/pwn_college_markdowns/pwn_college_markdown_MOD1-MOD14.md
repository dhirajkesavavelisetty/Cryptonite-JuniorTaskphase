PWN COLLEGE _ TASK PAHSE 1 (ALL MODULES INCLUDING INTRODUCTION)


Interacting with Dojo

1. 
# Challenge Name
Using the terminal

## My solve
**Flag:** ` pwn.college{MqHMbDt9t86sODeTZj7TW4menJs.0lMwQDOxwCM4gjNzEzW}`

- Enabling and utilising the terminal.

## What I learned
I learnt how to open and use the terminal

## References 
https://pwn.college/welcome/welcome/


2. 
# Challenge Name
Using the VS code workspace

## My solve
**Flag:** `pwn.college{k191eeyJ4oVxegWw9n701A-OIKr.QX2IzNzwCM4gjNzEzW}`

- Enabling and utilising the visual studio code

## What I learned
I learnt how to open and use the vs code application

## References 
https://pwn.college/welcome/welcome/


3.
# Challenge Name
Using the GUI desktop

## My solve
**Flag:** `pwn.college{wJhveFCYRwnES0G1tW6ne-9oGX2.QX3IzNzwCM4gjNzEzW}`

- Opening the desktop and obtaing terminal from the desktop

## What I learned
I learnt how to open the terminal from the desktop

## References 
https://pwn.college/welcome/welcome/


4.
# Challenge Name
Pasting into the desktop

## My solve
**Flag:** `pwn.college{skf0jMzs9_g9OhogP7hNMqBpJbg.QX4IzNzwCM4gjNzEzW}`

- I copied the secret token provided and pasted it on the virtual desktops clipboard and then pasted it further on the terminal to obtain the key

## What I learned
I learnt that we cannot directly copy paste it using shorcut keys and have to maually overwrite the clipboard in the desktop

## References 
https://pwn.college/welcome/welcome/


5.
# Challenge Name
Restarting challenges

## My solve
**Flag:** `pwn.college{ckggQOeJVCN1nUP3iLwJb2i-Bfq.QX1kDM1wCM4gjNzEzW}`

- The terminal failed as we typed the wrong password so we should restart the terminal and run it again and type out the correct password to obtain the flag

## What I learned
Sometimes the terminal might crash and it is important for us to restart the terminal and perform the task.

## References 
https://pwn.college/welcome/welcome/


6.
# Challenge Name
Getting help using in built AI

## My solve
**Flag:** `pwn.college{Ykqxvxq1fxH-xXnNYXAZEniGXGV.QXyIDN1wCM4gjNzEzW}`

- Ask the AI provided for the password and obtain the flag

## What I learned
The system provides a helpful system which can be used for help

## References 
https://pwn.college/welcome/welcome/



Module-1
Hello hackers

1.
# Challenge Name
Intro to commands

## My solve
**Flag:** `pwn.college{sMgGXxfmFsitrr4WvNFvz2uWau8.QX3YjM1wCM4gjNzEzW}`

- I just typed in the argument to return hello
```bash
 hello
```

## What I learned
This is the basic and first linux command and i learn that typing in any argument will return the argument.

## References 
https://pwn.college/linux-luminarium/hello/


2.
# Challenge Name
Intro to arguments
## My solve
**Flag:** `pwn.college{EFmLnfGSMvECxBem-COd3ti8Pqe.QX4YjM1wCM4gjNzEzW}`

- I typed in hello as the command and argument was hackers
```bash
hello hackers
```

## What I learned
I learnt that the first word is a command and the next word is an argument

## References 
https://pwn.college/linux-luminarium/hello/


3.
# Challenge Name
Command history

## My solve
**Flag:** `pwn.college{wPnLetqB4JaqH15Sl0UFgDahpq1.0lNzEzNxwCM4gjNzEzW}`

- I cicked the up arrow key and the enter to obain the flag
```bash
(Up-arrow-key)
```

## What I learned
Up and down arrow are a way of obtaining previous commands as the terminal maintains a history of the commands

## References 
https://pwn.college/linux-luminarium/hello/



Module-2
Pondering paths


1.
# Challenge Name
The root

## My solve
**Flag:** `pwn.college{kNe_uhYR7db7S-GQaT1QLOuxll3.QX4cTO0wCM4gjNzEzW}`

- we have to invoke the program by running the file so we type in backslash where the file system starts and type in the program to invoke and run it.

```bash
/pwn
```

## What I learned
learnt that backslash is where the file system starts and then typing in the program runs it providing the flag.

## References 
https://pwn.college/linux-luminarium/paths/


2.
# Challenge Name
program and absolute paths

## My solve
**Flag:** `pwn.college{sA6o6vaWpljM0g0_bIw5e5Vid-8.QX1QTN0wCM4gjNzEzW}`

- I had to run a program present in the challeneg directory so i typed out the path of the file
```bash
/challenge/run
```

## What I learned
i learn that to open and run a specific file we should mention the path clearly and this is called the path of the file

## References 
https://pwn.college/linux-luminarium/paths/


3.
# Challenge Name
Position thy self

## My solve
**Flag:** `pwn.college{MAPdicr-odcZh0cgRoDw7OQs2Ql.QX2QTN0wCM4gjNzEzW}`

the program was stored in another directory so i used the cd command twice to navigate to that directory and then excute the program.

```bash
cd /usr
cd /include
/challenge/run
```

## What I learned
i learnt that cd is a command which navigates to the specific directory to find the file
## References 
https://pwn.college/linux-luminarium/paths/


4.
## Challenge Name
position elsewhere

## My solve
**Flag:** `pwn.college{0LH_wkbTreLWJpxXYsQ0a3gk2UX.QX3QTN0wCM4gjNzEzW}`

- file was loccated in another directory so i used the cd command to navigate and run
```bash
cd /var
/challenge/run
```

## What I learned
i learnt that cd command stands for change directory
## References 
https://pwn.college/linux-luminarium/paths/


5.
# Challenge Name
postion yet somwhere

## My solve
**Flag:** `pwn.college{gcou8b83SI-WKJj2wH8q7IZSP5y.QX4QTN0wCM4gjNzEzW}`

- use the cd command and navigate to the specific directory
```bash
cd /proc/131/fd
/challenge/run
```

## What I learned
cd is a command use to navigate to diffrent directories

## References
https://pwn.college/linux-luminarium/paths/
 

6.
# Challenge Name
implicit relative paths

## My solve
**Flag:** `pwn.college{88-DDXIjHdgNIxA7NJv0HX4UuUJ.QX5QTN0wCM4gjNzEzW}`

- instead of the aboslute path i used the relative path where relative path is dependent on the cwd
```bash
challenge/run
```

## What I learned
i learn the difference between absolute and relative path
## References 
https://pwn.college/linux-luminarium/paths/


7.
# Challenge Name
explicit relative path

## My solve
**Flag:** `pwn.college{ASlf7179Itd2IfcFJyZUqgjSiPu.QXwUTN0wCM4gjNzEzW}`

-we try different paths and then come down that it should start with ./

```bash
./challenge/run
```

## What I learned
. and .. are two different implicit entries. . refers to the same directory and ..refers to the directory the current directory is present in
## References 
https://pwn.college/linux-luminarium/paths/


8.
# Challenge Name
implicit relative path


## My solve
**Flag:** `pwn.college{4AS0FzVsUfkQwK2EkbQgm4jHwoo.QXxUTN0wCM4gjNzEzW}`

- when we type in run in /challenge they system looks for run in the path but doesnt chekc current folder for safety reasons 
so we change the directroy and tell it to look in the current directory by adding a dot
```bash
cd /challenge
./run
```

## What I learned
i learnt that linux doesnt check in the current working directory and typing in run the shell loks for run in the path for security reasons so we should use a . and tell it to look for run in the current directory
## References 
https://pwn.college/linux-luminarium/paths/
chatgpt to understand it a little in detail


9.
# Challenge Name
home sweet home

## My solve
**Flag:** `pwn.college{A2YhCx6ArJferHtgA5Ye2mja-OK.QXzMDO0wCM4gjNzEzW}`

i provided and aboslute path as argument  and then typed in ~/a so this essentially creates a copy of the flag in the file named a and now path becomes /hom/hacker/a
```bash
/challenge/run ~/a
```

## What I learned
typing in the absolute path and then ~/<file name> copyies the flag from the fle to another file in the home directory with the given file name
## References 
Gemini



Module-3
Comprehending commands

1.
# Challenge Name
cat the command

## My solve
**Flag:** `pwn.college{8KhkNoBSABe-VZwXrl0X9tju6cQ.QXxcTN0wCM4gjNzEzW}`

- cat is a command used very often and i typed out cat flag to open the flag
```bash
cat flag
```

## What I learned
cat opens a file
## References 
https://pwn.college/linux-luminarium/commands/


2.
# Challenge Name
catting absolute paths

## My solve
**Flag:** `pwn.college{8tebHUPP4CRhdYzDihCVJhXtsDO.QX5ETO0wCM4gjNzEzW}`

- since flag was not present in the home directory so we type in the absolute path to read the flag
```bash
cat /flag
```

## What I learned
cat can be used directly when an absolute path is mentioned
## References 
https://pwn.college/linux-luminarium/commands/


3.
# Challenge Name
more catting

## My solve
**Flag:** `pwn.college{MszJimjHVUap99MAZznh5EOuT98.QXwITO0wCM4gjNzEzW}`

- since the flag is present in some random directory instead of using cd to naviagte i mentioned the absolute path of flag file
```bash
cat /usr/share/giac/flag
```

## What I learned
we can type out the absolute path to open a file instead od cd command
## References 
https://pwn.college/linux-luminarium/commands/


4.
# Challenge Name
grepping for a needle in a haystack

## My solve
**Flag:** `pwn.college{whQRctWHXhGa4VRi2s3jkJYeWBM.QX3EDO0wCM4gjNzEzW}`

- used the grep command to obtain the flag in a file of about thousand lines of text
```bash
grep pwn.college /challenge/run
```

## What I learned
grep command seraches for the specific line mentioned in a file of many lines and prints out the same
## References 
https://pwn.college/linux-luminarium/commands/


5.
# Challenge Name
comparing files

## My solve
**Flag:** `> pwn.college{Agt4ITnMyWE71nl_N4wTcsMjydj.01MwMDOxwCM4gjNzEzW}`

- i used the diff command and typed out the absoluet path of both files to obtain the real flag
```bash
diff /challenge/decoys_only.txt /challenge/decoys_and_real.txt
```

## What I learned
diff command find the difference between two files and also mentions which line the difference exists where a stands for add and c stands for change
## References 
https://pwn.college/linux-luminarium/commands/


6.
# Challenge Name
listing files

## My solve
**Flag:** `pwn.college{IBF6sMF-Sxr1sjrrpK7m7endrKq.QX4IDO0wCM4gjNzEzW}`

- i explored the challenge directory using ls command and found the file, then i opened the directory using cat option and opened to file
```bash
ls /challenge
cat /challenge/8130-renamed-run-10969
/challenge/8130-renamed-run-10969
```

## What I learned
ls is a command to look at the directories and files in a given directory
## References 
https://pwn.college/linux-luminarium/commands/


7.
# Challenge Name
touching files

## My solve
**Flag:** `pwn.college{kl_BCcmIb6BrevGJ5hH-I1_RpCU.QXwMDO0wCM4gjNzEzW}`

- i created two files using touch and typed out the path to obtain the flag
```bash
touch /tmp/pwn
touch /tmp/college
/challenge/run
```

## What I learned
touch is command to create a file
## References 
https://pwn.college/linux-luminarium/commands/


8.
# Challenge Name
removing files

## My solve
**Flag:** `pwn.college{8jSzgfQNPegXGbeYtZ8eR4ppuvS.QX2kDM1wCM4gjNzEzW}`

- typed out rm to remove the respective file
```bash
rm delete_me
/challenge/check
```

## What I learned
rm is a cmmond to delete a file
## References 
https://pwn.college/linux-luminarium/commands/


9.
# Challenge Name
moving files

## My solve
**Flag:** `pwn.college{o6_6uCMqBG08l47JcyDrk8bRk0C.0VOxEzNxwCM4gjNzEzW}`

- typing out mv command and the file to be moved followed by the location
```bash
mv /flag /tmp/hack-the-planet
/challenge/check
```

## What I learned
mv is a command for moving a file across directories
## References 
https://pwn.college/linux-luminarium/commands/


10.
# Challenge Name
hidden files

## My solve
**Flag:** `pwn.college{8-F-bNX2xvQ0c-3UpCrxTzvGXJp.QXwUDO0wCM4gjNzEzW}`

- i used the command ls -a to find the hidden flag and used cat to open the file to obtain the flag
```bash
ls -a
cat /.flag-274272336026953
```

## What I learned
linux doesnt show files starting with (.) using ls so we should use ls -a to obtain the files starting with that character
## References 
https://pwn.college/linux-luminarium/commands/


11.
# Challenge Name
filesystem quest

## My solve
**Flag:** `pwn.college{EY3TeqkgD4esr3e8TM_GkucI9YU.QX5IDO0wCM4gjNzEzW}`

explored various directories and used cd, ls, ls -a, cat to navigate into different places get the clues and obtain the flag
```bash
hacker@commands~an-epic-filesystem-quest:/usr/local/lib/python3.8/dist-packages/pwntools-5.0.0.dev0.dist-info$ cat .MESSAGE
```

## What I learned
files can be burried deep inside directories and it necessary to be patient
## References 
https://pwn.college/linux-luminarium/commands/


12.
# Challenge Name
making directories

## My solve
**Flag:** `pwn.college{Ed1uJYyY0xCLBGRxVer4YOn25jg.QXxMDO0wCM4gjNzEzW}`

make a directory using mkdir command
```bash
mkdir /tmp/pwn
touch college
/challenge/run
```

## What I learned
mkdir creates a new directory
## References 
https://pwn.college/linux-luminarium/commands/


13.
# Challenge Name
finding files

## My solve
**Flag:** `pwn.college{UF6RIGln8MEILf4kJwFHcBfU7nN.QXyMDO0wCM4gjNzEzW}`

- we type in the find command and then it drops down different files in the directory ending with flag. we specifically open each file using cat and obtain the flag
```bash
find / -name flag
cat /usr/local/lib/python3.8/dist-packages/matplotlib_inline-0.1.7.dist-info/flag
```

## What I learned
- find is a command where you can use it to navigate to a specific file
- The find command takes optional arguments describing the search criteria and the search location
- (1)(find) command seraches in the given directory
- (2)we can filter by name using (find -name <file>)
- (3)we can search in the whole file system (find / -name <file>)
## References 
https://pwn.college/linux-luminarium/commands/


14.
# Challenge Name
linking files

## My solve
**Flag:** `pwn.college{U_ilvm-wUPxSfNyvPEOFkQ3mEWZ.QX5ETN1wCM4gjNzEzW}`

- we should create a symoblic link here. The target file is /flag and link is /home/hacker/not-the-flag
so we create the link and run it.
```bash
ln -s /flag /home/hacker/not-the-flag
/challenge/catflag
```

## What I learned
- there are two types of links soft links and hard links
- A hard link is when you address your apartment using multiple addresses that all lead directly to the same place (e.g., Apt 2 vs Unit 2).
- A soft link is when you move apartments and have the postal service automatically forward your mail from your old place to your new place.
- to create a soft(symbolic link): The command syntax is ln -s <target_file><link_name>

``` hacker@dojo:~$hacker@dojo:~$ cat /tmp/myfile
    This is my file!

    hacker@dojo:~$ ln -s /tmp/myfile /home/hacker/ourfile
    
    hacker@dojo:~$ cat ~/ourfile
    This is my file!
```
## References 
https://pwn.college/linux-luminarium/commands/



Module-4
Digesting documentation

1.
# Challenge Name
learning from documentation

## My solve
**Flag:** pwn.college{oL764ncyZWolr-wz5lqMVq71obF.QX0ITO0wCM4gjNzEzW}`

- here we tell the system to give the flag as an argument for it to follow. the program is designed specifically give flag when it is asked to do so
```bash
/challenge/challenge/ --giveflag
```

## What I learned
a single program can have many different functions and it important to mention a specify the target to change its behaviour accordingly
## References 
https://pwn.college/linux-luminarium/man/

2.
# Challenge Name
learning complex usage

## My solve
**Flag:** `pwn.college{IU98BO-r82lT9JfkvoNP2yNp1wv.QX1ITO0wCM4gjNzEzW}`

- here i typed out the directory the flag is present in and then provide a command printfile which prints flag from the argument /flag
```bash
/challenge/challenge --printfile /flag
```

## What I learned
in complex usages there are ways of using the command like in the <find module> we indexed using name etc., similarly here we provide an argument to the command in the particular directory
## References 
https://pwn.college/linux-luminarium/man/


3.
# Challenge Name
reading manuals

## My solve
**Flag:** `pwn.college{I8rvQbE8hFb46g_fH0Spt0aPGym.QX0EDO0wCM4gjNzEzW}`

- i used the man command to open the manual where in the description it showed various commands that can be provided in which inputting the command with the number 884 provides the flag
```
man challenge
/challenge/challenge --rvbhbg 884
```

## What I learned
man stands for manual and provides in depth descrption about a specific command 
## References 
https://pwn.college/linux-luminarium/man/


4.
# Challenge Name
searching manuals

## My solve
**Flag:** `pwn.college{EMx2QQAEAvrBIg4iMqgvhYfUSay.QX1EDO0wCM4gjNzEzW}`

- at first i went through the manual using the man command and then typed in /flag and clicked n thrice to navigate to the right command further typing out the command to obtain the flag
```bash
man challenge
challenge/challenge --itcme
```

## What I learned
in the manual using ```/flag``` and using n help me navigate to the flag command and hence pressing q quits the command
the desrption is stored in a special file
## References 
https://pwn.college/linux-luminarium/man/


5.
# Challenge Name
searching for manuals

## My solve
**Flag:** `pwn.college{If6rsr1NoZ8m8Uk_65z3AF6KVXJ.QX2EDO0wCM4gjNzEzW}`

- since i dont know where to search for i start of by looking at the manual for manual
- i found out that <-k> option is used to search for keywords
- i searched for the manual of challenge using the <-k> command
- a new command popped up and then i opened the manual where it showed the command to obtain the flag and enter a specific number to obtain flag
```bash
man man
man -k challenge
man frsromkzwg
/challenge/challenge --frsrom 618
```
```       man -k [apropos options] regexp ... ```

## What I learned
- all of the manpages are gathered in a searchable database, so i can search the man page to find the hidden challenge man page
-  The man page also mentions apropos, which is a utility specifically used to search for keywords in the man page database.
- regexp stands for regular expression
## References 
https://pwn.college/linux-luminarium/man/


6.
# Challenge Name
helpful programs

## My solve
**Flag:** ` pwn.college{0meGMHHtmKfssHFzptU-bATPBc6.QX3IDO0wCM4gjNzEzW}`

- first i used the help command to open the page and followed the instructions
- next was to type out the fortune command followed by version command followed by print to get the secret number
- then i ran the -g command along with the secret number to obtain  the flag
```bash
/challenge/challenge --help
/challenge/challenge --fortune
/challenge/challenge -v
/challenge/challenge -p
/challenge/challenge -g 63
```

## What I learned
i learnt that ``` --help, -h, -?, /? ``` are different ways to tell the system that you need some help in moving forward and a help manual will be printed for reference.
## References 
https://pwn.college/linux-luminarium/man/

7.
# Challenge Name
help for builtins

## My solve
**Flag:** `pwn.college{gNJVZ1wD7UHAe2f6437RGGmatIT.QX0ETO0wCM4gjNzEzW}`

- i start by asking the system for help where it shows my the commands to run as well as the secret value
- i run the commands one by one and in the end key in the secret value to obtain the flag

```bash
help challenge
challenge --fortune
challenge --version
challenge --secret gNJVZ1wD
```

## What I learned
i learnt that some commands, rather than being programs with manual pages and help options, are built into the shell itself. These are called builtins. We can get help
on a specific one by passing it to the help builtin.

Built-ins are commands that are part of the shell itself. They are stored in the shell's memory and don't have a separate executable file on the file system. When you run a built-in, the shell executes it directly and instantly, without having to search for a program file.

Helpful programs (or external commands) are standalone executable files stored in directories on the file system, like /bin, /usr/bin, etc.. When you run a helpful program, the shell searches for its executable file in a list of directories defined by the $PATH environment variable. This search and loading process makes them slightly slower to start than built-ins.
## References 
https://pwn.college/linux-luminarium/man/
gemini





Module-5
File globbing

1.
# Challenge Name
matching with *

## My solve
**Flag:** `pwn.college{YprvcoHBFG4U3D0c-lms8SE04zo.QXxIDO0wCM4gjNzEzW}`

- i typed out cd command and two letters of the directory followed by * for the system to automatically figure out the serach and match the directory

```bash
cd /ch*
/challenge/run
```

## What I learned
<*> acts a wildcard and matches any part other than / or a leading (.)

## References 
https://pwn.college/linux-luminarium/globbing/


2.
# Challenge Name
matching with ?

## My solve
**Flag:** pwn.college{wufpv0DivR0FNqzySzi-tM_3FKE.QXyIDO0wCM4gjNzEzW}

-i type out all the characters of the directory excpet the few mentioned in the challenge so that the systemfinds  and inserts as it searches and matches the characters

```bash
cd /?ha??enge
/challenge/run
```

## What I learned
When it encounters a ? character in any argument, the shell will treat it as a single-character wildcard. This works like *, but only matches one character
## References 
https://pwn.college/linux-luminarium/globbing/


3.
# Challenge Name
matching with []

## My solve
**Flag:** `pwn.college{QcE2kbR7h-u7ieH1VtjoQjjq_cs.QXzIDO0wCM4gjNzEzW}`

- the challenge was to retreive files a,b,s,h so i typed out the command and enclosed each character of the name in square brakcets

```bash
/challenge/run file_[bash]
```

## What I learned
The square brackets are a limited form of ?, [] is a wildcard for some subset of potential characters, specified within the brackets.
For example, [pwn] will match the character p, w, or n. 
system picks the letter and searched one specific file with that character hence it searches for a single character unlike (*) >>IMP<<
## References 
https://pwn.college/linux-luminarium/globbing/


4.
# Challenge Name
matching paths with []

## My solve
**Flag:** `pwn.college{E7dW9_vsr_eVihbKPBozVmuG9OQ.QX0IDO0wCM4gjNzEzW}`

- i ran the run command with the complete path of the file using globs to search for those specific files b,a,s,h.
```bash
/challenge/run /challenge/files/file_[bash]

```

## What I learned
globbing happens on the basis of the path and we can expand the entire paths with the globbed arguments
## References 
https://pwn.college/linux-luminarium/globbing/


5.
# Challenge Name
multiple globs

## My solve
**Flag:** `pwn.college{I3jdlOTtLV0cPdIU12q-72VBZaL.0lM3kjNxwCM4gjNzEzW}`

- i run the program and then add two globs one before p and one after p as they match any characters before and after p

```bash
/challenge/run *p*
```

## What I learned
i learnt that multiple globs can be used like *fl* (*)can be null or even ag to complete the argument as flag
## References 
https://pwn.college/linux-luminarium/globbing/


6.
# Challenge Name
mixing globs

## My solve
**Flag:** `pwn.college{ESVal8T2foi3jWR2OpJ4ZyLdHry.QX1IDO0wCM4gjNzEzW}`

- i changed into the provided directory and then noted the first letter in these three words.
- i enclosed them in the square globs so that the system finds those words and (*) fills and seraches the rest of the word and hence the flag is obtained

```bash
/challenge/run [cep]*
```

## What I learned
- square brackets enclose characters where system choses the charcter and searches only one file with that provided character
## References 
https://pwn.college/linux-luminarium/globbing/


7.
# Challenge Name
exclusionary globbing

## My solve
**Flag:** `pwn.college{07_KEzg1DLDUa82uyXbfTZ97c7K.QX2IDO0wCM4gjNzEzW}`

- i typed out the command of run and then typed out square globs along with an excalmatory mark standing for not with letters p,w,n as mentioned and then an (*) so the system finds the words not having p, w, n and then obtain the flag.

```bash
/challnege/run [!pwn]*
```

## What I learned
- (!)/(^) stand for not and print out all other files except ones having p,w,n in ther file name
## References 
https://pwn.college/linux-luminarium/globbing/


8.
# Challenge Name
tab completion

## My solve
**Flag:** `pwn.college{syfUat3bee6L1Mu2T3V8lmkkNBR.0FN0EzNxwCM4gjNzEzW}`

- i opened the challenge directory using ls command and found the pwncollege directory but i was supposed to use the tab command so i typed our pwn and then tab so that the system understand what file i want to open and automatically obtained the argument

```bash
cat /challenge/pwn <tab> ---> /challenge/pwncollege__ 
```

## What I learned
- (*) might sometimes might lead to mistakes and expand uninteded files
- a safer alternative is using tab where it auto completes what we typed initially and is pretty usefull.
## References 
https://pwn.college/linux-luminarium/globbing/


9.
# Challenge Name
multiple options for tab completion

## My solve
**Flag:** `pwn.college{wXQ5Weu62-6LSqErOx6AsIB3S7M.0lN0EzNxwCM4gjNzEzW}`

- after typing in the directory i typed out p and ran the tab command to open the list.
- then i tried opening eahc file indivually using cat and found the flag in pwncollege-flag
```bash
/challenge/files/p <tab>
/challenge/files/pwncollege-flag
```

## What I learned
when there are multiple files starting with a prompt and tab is used bash opens every possible command while other terminals move throw various command up and down whenever tab is clicked
## References 
https://pwn.college/linux-luminarium/globbing/


10.
# Challenge Name
tab complettion on commands

## My solve
**Flag:** `pwn.college{I2TkmVQ0RermPV6Ak31QaYI6iGt.0VN0EzNxwCM4gjNzEzW}`

- i typed out pwncollege and then clicked on tab for the system to automatically finish the command for me
```bash
pwncollege <tab>
```

## What I learned
tab works for commands as well and understand what command you are typing out and fills in automatically
## References 
https://pwn.college/linux-luminarium/globbing/



Module-6
Practicing piping

1.
# Challenge Name
redirecting output

## My solve
**Flag:** `pwn.college{gxTp7YSsUNwOIMehoE--8HDcWCs.QX0YTN0wCM4gjNzEzW}`

- i used the echo command to print PWN in a new file names COLLEGE
```bash
echo PWN > COLLEGE
cat COLLEGE
```

## What I learned
(>) this command prints out the given text in a new file like
`echo hi > asdf
cat asdf
hi'
## References 
https://pwn.college/linux-luminarium/piping/


2.
# Challenge Name
redirecting more output

## My solve
**Flag:** `[FLAG] pwn.college{gYZ6Pcico71_71bzrQDNHChY0dK.QX1YTN0wCM4gjNzEzW}`

- i redirected the flag output to a new my flag file by using the (>) symbol
```bash
/challange/run > myflag
```

## What I learned
(>) doesnt only redirect echo output but can also direct various other commands
## References 
https://pwn.college/linux-luminarium/piping/


3.
# Challenge Name
appending output

## My solve
**Flag:** `pwn.college{YzroAZ6Wgl8OuFWVt-GpnbWft9k.QX3ATO0wCM4gjNzEzW}`

- as told by the challenge at first i ran the command and the system created a new the--flag file followed by (>>) to ensure that the second part of the flag present in the command is added to the-flag file

```bash
/challenge/run > /home/hacker/the-flag
/challenge/run >> /home/hacker/the-flag
```

## What I learned
- (>>) doesnt create a new file specifically and just runs the command in the next line of the creatoed or mentioned file
## References 
https://pwn.college/linux-luminarium/piping/


4.
# Challenge Name
redirecting errors

## My solve
**Flag:** `[FLAG] pwn.college{0CfQg_AuU51TVPWuGylCZAFaioh.QX3YTN0wCM4gjNzEzW}`

- i directed the output of the command to flag file by (>) and then errors to the instructions file using (2>)

```bash
/challenge/run > myflag 2> instructions
```

## What I learned
- A File Descriptor (FD) is a number that describes a communication channel in Linux
- ex: 
FD 0: Standard Input
FD 1: Standard Output (>)/(1>)
FD 2: Standard Error (2>)
## References 
https://pwn.college/linux-luminarium/piping/


5.
# Challenge Name
redirecting input

## My solve
**Flag:** `pwn.college{8dTQsocGWDKcfVs5oF3jWaDk0qD.QXwcTN0wCM4gjNzEzW}`

- i redirected the output college to the pwn file using (>) and then redirected input of the command to pwn using (<). 

```bash
echo COLLEGE > PWN
/challenge/run < PWN
```

## What I learned
- not only redirecting outputs but we can redirect inputs as well by using (<)
hacker@dojo:~$ echo yo > message
hacker@dojo:~$ cat message
yo
hacker@dojo:~$ rev < message
oy
## References 
https://pwn.college/linux-luminarium/piping/


6.
# Challenge Name
grepping stored results
ssu
## My solve
**Flag:** `pwn.college{QVN5oln8FKRlt-pWionFBVbrUo5.QX4EDO0wCM4gjNzEzW}`

- at first i redirected th output to a new file data.txt and grepped the file to obtain the flag

```bash
/challenge/run > /tmp/data.txt
grep flag /tmp/data.txt
```

## What I learned
- grep syntax: grep <text u wanna search> <name or path of the file>
## References 
https://pwn.college/linux-luminarium/piping/


7.
# Challenge Name
grepping live output

## My solve
**Flag:** `pwn.college{Y8K60ji5Loejk3T4A0u5am7J8Bc.QX5EDO0wCM4gjNzEzW}`

- here i redirect the output of the command to the pipe and then grep or search for the flag pwn
- the pipe is technically an intremediate file where the command's output is redirected and then we grep that pipe for the flag

```bash
/challenge/run | grep pwn
```

## What I learned
- the | (pipe) operator. Standard output from the command to the left of the pipe will be connected to (piped into) the standard input of the command to the right of the pipe
## References 
https://pwn.college/linux-luminarium/piping/


8.
# Challenge Name
grepping errors

## My solve
**Flag:** `pwn.college{UPB6q7xlCWfGF8tod_wgQevmJt6.QX1ATO0wCM4gjNzEzW}`

- so here using (2>) we redirect the standard error output to its standard output and then grep in the pipe for flag

```bash
/challenge/run 2>&1 | grep pwn
```

## What I learned
- The | operator redirects only standard output to another program, and there is no 2| form of the operator
- The shell has a >& operator, which redirects a file descriptor to another file descriptor
- 2>&1 to merge file descriptor 2 (standard error) into file descriptor 1 (standard output)
- Use the | operator to send the combined output to the grep command, which will search for the word "pwn"

## References 
https://pwn.college/linux-luminarium/piping/


9.
# Challenge Name
filtering with grep -v

## My solve
**Flag:** `pwn.college{cv9UJyYwiVsYtAQwDpw4jqjoRlp.0FOxEzNxwCM4gjNzEzW}`

- so i input the command into the pipe and then use the grep -v command to search for eveyrhting other than decoy to obtain the flag
```bash
/challenge/run | grep -v DECOY
```

## What I learned
grep along with -v searches for everything other than the entered argument cause sometimes the best way of searching for what we want is to search for what we dont want
## References 
https://pwn.college/linux-luminarium/piping/


10.
# Challenge Name
duplicating piped data with tee

## My solve
**Flag:** `pwn.college{siyYABFHe-K2Gprd5ROrvx6VPtM.QXxITO0wCM4gjNzEzW}`

- at first i piped the command and then used tee to redirect the output to a temporary file pwn_output
- now this output is used as input for /challenge/college
- then the command saved output to the temporary file created and pipes it to college, the program failed as it  needs some specific code
- now we open the file using cat and this reveals the data pwn is sending us which is a secret argument along with a secret code
- then run the initial command with the argument and secret code to obtain the flag

```bash
/challenge/pwn | tee pwn_output | /challenge/college
cat pwn_output
/challenge/pwn --secret siyYABFH | /challenge/college
```

## What I learned
- generally pipe is an intermediate and hence we cant see what command exactly ran so now the tee command duplicates data flowing through the pipe to any number of files provided
- ex: '''hacker@dojo:~$ echo hi | tee pwn college
hi
hacker@dojo:~$ cat pwn
hi
hacker@dojo:~$ cat college
hi
hacker@dojo:~$```
here tee command made stored the output in the pipe, pwn and in college


## References 
https://pwn.college/linux-luminarium/piping/


11.
# Challenge Name
process substitution for the input

## My solve
**Flag:** `pwn.college{AkF9jwjT_HocMb0nbBSU9JdtbN6.0lNwMDOxwCM4gjNzEzW}`

- basically i used the command to obtain the path of each files and used the difference to obtain the flag
```bash
diff <(/challenge/print_decoys) <(/challenge/print_decoys_and_flag)
```

## What I learned
- Linux follows the philosophy that "everything is a file". That is, the system strives to provide file-like access to most resources, including the input and output of running programs
- When you write <(command), bash will run the command and hook up its output to a temporary file that it will create and print out the path
## References 
https://pwn.college/linux-luminarium/piping/


12. <IMPPPP>
# Challenge Name
writing to multiple programs

## My solve
**Flag:** `pwn.college{g1nO6B9GdBhLiyCupIiw70Q7Oyf.QXwgDN1wCM4gjNzEzW}`
    
- you need to pipe the output of /challenge/hack and duplicate it to serve as input for both /challenge/the and /challenge/planet
- The tee command will read from standard input and write to both standard output and the file specified as an argument. 
- The process substitution, >(...), creates a temporary named pipe that acts as a file, allowing you to feed the output of tee to a command.
- The | operator sends the standard output of /challenge/hack to the standard input of tee.
- The output of tee is automatically sent to the next command in the pipe, /challenge/the
- The tee command will also write to the process substitution, which directs the data to /challenge/planet

```bash
/challenge/hack | tee >(/challenge/the) | /challenge/planet
```

## What I learned
the >(command) reads the standard input, implements the command and writes it to the standard output
## References 
https://pwn.college/linux-luminarium/piping/
gemini to understand the process clearly


13. <IMPPPP>
# Challenge Name
split-piping stderr and stdout

## My solve

**Flag:** `pwn.college{kLMjpZlNEYxqLKzqWwMbT2hXN_N.QXxQDM2wCM4gjNzEzW}`

- so first we type out the file and then use (>) which essentially redirects output of /hack to another file but here we use (>()) so that the system sends the standard standard output obtain the file directly to the /planet file
- now the error output present in the /planet file is (>) copied into another file and then (>()) is used where the error is directly copied to the /the file
```bash
/challenge/hack > >( /challenge/planet ) 2> >( /challenge/the )
```

## What I learned
- > redirects stdout to a file or another destination.
- 2> redirects stderr to a file or another destination.
- 2>&1 merges stderr into wherever stdout is going, but this mixes both streams.
- >(...) creates a process substitution, allowing direct piping of output to another command.
- > >( /challenge/planet ) sends stdout to /challenge/planet.
- 2> >( /challenge/the ) sends stderr to /challenge/the
## References 
https://pwn.college/linux-luminarium/piping/


14.
# Challenge Name
names pipes

## My solve
**Flag:** `pwn.college{MNDkX5R9HqwMzRsxQltYJleEfco.01MzMDOxwCM4gjNzEzW}`

- so i made a fifo file called flag_fifo and then redirected the output of the given command to the fifo file
- since fifo is interdependent and runs when read and write are simultanous i opened a new termnal and ran the cat command to obtain the file

```bash
mkfifo /tmp/flag_fifo
/challenge/run > /tmp/flag_fifo'
cat /tmp/flag_fifo
```

## What I learned
- FIFOs, which stands for First (byte) In, First (byte) Out.
- mkfifo is the command to perform the task
- You control where FIFOs are created
- They persist until you delete them
- Any process can write to them by path (e.g., echo hi > my_pipe)
- You can see them with ls and examine them like files
- One problem with FIFOs is that they'll "block" any operations on them until both the read side of the pipe and the write side of the pipe are ready.
- No disk storage: FIFOs pass data directly between processes in memory - nothing is saved to disk
- Ephemeral data: Once data is read from a FIFO, it's gone (unlike files where data persists)
- Automatic synchronization: Writers block until the readers are ready, and vice-versa. This is actually useful! It provides automatic synchronization. Consider the example above: with a FIFO, it doesn't matter if cat myfifo or echo pwn > myfifo is executed first; each would just wait for the other. With files, you need to make sure to execute the writer before the reader.
- Complex data flows: FIFOs are useful for facilitating complex data flows, merging and splitting data in flexible ways, and so on. For example, FIFOs support multiple readers and writers.
## References 
https://pwn.college/linux-luminarium/piping/



Module-7
Shell variables

1.
# Challenge Name
printing variables

## My solve
**Flag:** `pwn.college{oALP94wbuOtKPnE30jx-aCljGAT.QX3UTN0wCM4gjNzEzW}`

- i used the echo command as well as the dollar symbol to print the value in the variabel which is the flag
```bash
echo $FLAG
```

## What I learned
- ($) prints the value present in a specfic variable
## References 
https://pwn.college/linux-luminarium/variables/


2.
# Challenge Name
setting variables

## My solve
**Flag:** `pwn.college{wmwfH1nbnC76B2cfS9ncSrAmy8I.QX5UTN0wCM4gjNzEzW}`

- to set up the variable we can simplet type the varibale name along with equal to and the value but we should make sure we dont leave any spaces in between as the shell will run the command and wont take the value

```bash
PWN=COLLEGE
```

## What I learned
we can set up the value of the variable by simply declaring it but make sure there are no spaces while doing so
## References 
https://pwn.college/linux-luminarium/variables/


3.
# Challenge Name
multi word variables

## My solve
**Flag:** `pwn.college{MbxMmjxlObp118a38kn9v-qp9ng.QXwYTN0wCM4gjNzEzW}`

- for multi word variables we enclose the value of the variable in double quotes
```bash
PWN="COLLEGE YEAH"
```

## What I learned
for multi word variables we enclose the value of the variable in double quotes

## References 
https://pwn.college/linux-luminarium/variables/


4.
# Challenge Name
expoting variables

## My solve
**Flag:** `pwn.college{MLBkBB5kad9SmzQaVN-GxJ2PMvL.QXyYTN0wCM4gjNzEzW}`

- since we to export the pwn variable we do so and then store the college variable and then run the program
- sh is a minimal shell implmentation that invokes as a child of the main shell
```bash
export PWN=COLLEGE
COLLEGE=PWN
/challenge/run
```

## What I learned
- not all set variables can be used outside since security is important
- so export is a command to export the variables

- ''' hacker@dojo:~$ VAR=1337
hacker@dojo:~$ echo "VAR is: $VAR"
VAR is: 1337
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: '''
the $ prompt is the prompt of sh, a minimal shell implementation that is invoked as a child of the main shell process. And it does not receive the VAR variable!
- only when we export we get the value of variable
## References 
https://pwn.college/linux-luminarium/variables/


5.
# Challenge Name
printed exported variables

## My solve
**Flag:** `pwn.college{UrDSinrfdEUgwDwNXYsOel2HqPc.QX4UTN0wCM4gjNzEzW}`

- env is a command that prints out all exported variables

```bash
env
```

## What I learned
- env is a command that prints out all exported variables
## References 
https://pwn.college/linux-luminarium/variables/


6.
# Challenge Name
storing command output

## My solve
**Flag:** `pwn.college{oggEdCrYrFua6mz4ENn5bOgU0FV.QX1cDN1wCM4gjNzEzW}`

- we can directly save the output of a command into a variable by enclosing the command into brackets or back ticks as well and starting of with a dollar sign

```bash
PWN=$(/challenge/run) or $'/challenge/run'
echo $PWN
```

## What I learned
- store the output of some command into a variable. the above method is called command substitution
## References 
https://pwn.college/linux-luminarium/variables/


7.
# Challenge Name
reading input

## My solve
**Flag:** `pwn.college{cy5yBYc9DaW_4b_Ym67JymM6QJG.QX4cTN0wCM4gjNzEzW}`

- we read the variable by using read command and then the name of the variable
```bash
read PWN
COLLEGE
```

## What I learned
we can read the variable from the user by using the read command and then list the variable in which the input shall be contained
## References 
https://pwn.college/linux-luminarium/variables/


8.
# Challenge Name
reading files

## My solve
**Flag:** `pwn.college{MPSpLt7k3vReXc-CewqBOusJ9wS.QXwIDO0wCM4gjNzEzW}`

- we can store the value of the variable as shown instead of using cat
```bash
read PWN < /challenge/read
```

## What I learned
- instead of using cat to state variables we can simply doi it by using the (<) character and read command
## References 
https://pwn.college/linux-luminarium/variables/



Module-8
Data manipulation


1.
# Challenge Name
Translating characters


## My solve
**Flag:** `pwn.college{gHR93yupvkvTJvKkwsils3Ms5yr.01MxEzNxwCM4gjNzEzW}`

- since tr is a term for translates and implements the edit or just replaces the characters mentioned, on running the command the system provided a toggled flag so so change the case i used the tr command which essentially stands for translate and pasted the toggled flag followed by the edits i want to make and then typed out the flag with the case changes

```bash
/challenge/run
Your case-swapped flag:
PWN.COLLEGE{Ghr93YUPVKVtjVkKWSILS3mS5YR.01mXeZnXWcm4GJnZeZw}

/challenge/run | tr PWN.COLLEGE{Ghr93YUPVKVtjVkKWSILS3mS5YR.01mXeZnXWcm4GJnZeZw} pwn.college{gHR93yupvkvTJvKkwsils3Ms5yr.01MxEzNxwCM4gjNzEzW}
youR CasE-sWappEd flag:
pwn.college{gHR93yupvkvTJvKkwsils3Ms5yr.01MxEzNxwCM4gjNzEzW}
```

## What I learned
tr is a command that stands for translate and helps edit the character provided in the first argument to the character provided in the next argument and can be used for multiple characters as well
## References 
https://pwn.college/linux-luminarium/data/


2.
# Challenge Name
deleting characters

## My solve
**Flag:** `pwn.college{cIf1OYQOYC6cT_C2Ydg0wEGlKMC.0FNxEzNxwCM4gjNzEzW}`

- since the tr command can also be used to delete characters i ran the program and obtained the flag with garbage charcaters hence used the command to remove the garbad characters mentioned and obtained the flag

```bash
hacker@data~deleting-characters:~$ /challenge/run
Your character-stuffed flag:
p^w%n%.%c^%o%lle^%g^e^{^%c%I^f%1^%O^Y%Q^O%Y^%C^6^c^%T^%_%C2%Y^%d^%g^%0^%w%E^G^l%K^%M%C^%.^%0^FN^%xE^zN^%x^w^%CM%4%g^j%N^%z%E^%z%W}^%%
```

## What I learned
'''tr -d''' command deltes the characters which are mentioned in the argument after the command from the file
## References 


3.
# Challenge Name
deleting new lines

## My solve
**Flag:** `pwn.college{A1k6_czMJeWRNNQC4k9SeNBWIes.0VNxEzNxwCM4gjNzEzW}`

- i ran the command to obtain the flag with a lot of unnecesary lines so to remove the unnecessary line breaks so to remove the line breaks i use the tr -d command to remove all the line breaks and obtain the flag. here we have to put the line break operator is ingle quotes so that the sytem understand to delete every possible line break given in the out put

```bash
/challenge/run | tr -d '\n'
```

## What I learned
enclosing the argument to be deleted in the ```tr -d``` command deletes every possible instance without passing any argument that should be edited. 
## References 
https://pwn.college/linux-luminarium/data/


4.
# Challenge Name
extracting the first lines with head

## My solve
**Flag:** `pwn.college{0EIIlsV1tLk5WprVpa6UJDvrdNh.0lNxEzNxwCM4gjNzEzW}`

- so at first i piped the initial file followed by a command head to obtain the first 7 lines of the file and then piped these 7 lines ones more to the college file as asked by the system. The system obtained the first 7 lines in pwn file and piped them to the college file to obtain the code. This command helps us to find out what the file contains instead of catting the file and print the entire content.

```bash
/challenge/pwn | head -n 7 | /challenge/college
```

## What I learned
- head is a command to obtain the first few lines of a code and by deafult it prints out the first 10 lines.
- we can decide the number of lines to be printed by using ```head -n <number>``` where the system reads the number and prints those many number of lines from the file
## References 
https://pwn.college/linux-luminarium/data/


5.
# Challenge Name
extracting specific selections of text

## My solve
**Flag:** `pw.college{osEKLhqgfAw_I6wNhZpqYNYXwDe.01NxEzNxwCM4gjNzEzW}`

- i entered the command which excutes the program to output the flag and pipe it in then i use the ```cut``` command where i mentione ```-d``` followed by a space which tells the system that the columns are seperated by a space character and the '''-f 2``` tells the system to find the column number 2 and extract or cut and then use another pipe where i used the translate command followed by line break is single quotes to get rid of the line breaks wherever possible and obtain the proper value of flag
```bash
/challenge/run | cut -d ' ' -f 2 | tr -d '\n'
```

## What I learned
- cut is a command to obtain specific columns of a data where it extracts those columns
- we key in -d which is a delimiter and explains how columns are separeted like above we key in the space character to tell it columns are sepereated by space
- the -f argument specifies the column number to be extracted also called the field number
## References 
https://pwn.college/linux-luminarium/data/


6.
# Challenge Name
sorting data

## My solve
**Flag:** `pwn.college{gRc4fHA5AIvAdSj2JUangqLyfHA.0FM0MDOxwCM4gjNzEzW}`

- i used the flag command as mentioned which sorts the text according to the argument provided but by deafult it sorts in the alphabetical order and then obtained the flag from the bottom as mentioned in the challenge

```bash
sort /challenge/flag.txt
```

## What I learned
sort orders lines alphabetically. Arguments can change this:
-r: reverse order (Z to A)
-n: numeric sort (for numbers)
-u: unique lines only (remove duplicates)
-R: random order
## References 
https://pwn.college/linux-luminarium/data/



Module-9
Processes and jobs


1.
# Challenge Name
listing processes

## My solve
**Flag:** `pwn.college{4JZdVnBDbrijCvMIKcoHrqwNZ4a.QX4MDO0wCM4gjNzEzW}`

- here since the two command ps -ef and ps aux provide the info about the computer i ran the commands but none of the files opened up the flag so as mentioned in the note i ran commands ps -efw and ps auxww as the system truncates the path till the terminal window ends and to avoid this we should use those commands to prevent the system from doing so

```bash
ps auxww
```

## What I learned
- ps -ef and ps aux are two commands which basically put out the list of the processes run on the computer with a bunch  of details.
- "Standard" Syntax: in this syntax, you can use -e to list "every" process and -f for a "full format" output, including arguments. These can be combined into a single argument -ef.
- "BSD" Syntax: in this syntax, you can use a to list processes for all users, x to list processes that aren't running in a terminal, and u for a "user-readable" output. These can be combined into a single argument aux.
- they are slightly different but give almost the same output
- the system truncates the paths sometimes because of the terminal window size so to avoid this we should use the ps -efw or ps auxww to avoid this truncation
- The -e flag is shorthand for --everything or --all. It instructs ps to select all processes currently running, regardless of the user or terminal they are associated with.
- The -f flag is shorthand for --full. It tells ps to display a more detailed, "full" format of the process listing.
## References 
https://pwn.college/linux-luminarium/processes/


2.
# Challenge Name
killing processes

## My solve
**Flag:** `pwn.college{IN8nlYA0ZeXckVtsahlGoOWkbr6.QXyQDO0wCM4gjNzEzW}`

- i serached out all the running processes using ps -ef command and then observed the PID ID of dont_run command. so then i implemnted the kill function mentioning the PID id of the process and then ran the process succesfully obtaining the flag

```bash
ps -ef
kill 136
/challenge/run
```

## What I learned
- kill is a command which succesfully terminates a running process in the terminal
- to kill a process u have to mention the pid (process id) of the process as an argument to kill
- A PID (Process ID) is a unique number assigned to each running process by an operating system's kernel. It's like a social security number for a program, used to identify and manage it.
## References 
https://pwn.college/linux-luminarium/processes/


3.
# Challenge Name
interrupting processes

## My solve
**Flag:** `pwn.college{wgNfOY4SGOW7grwsGjcQt-1UIXq.QXzQDO0wCM4gjNzEzW}`

- here i typed out the command to run the program but the challenge required me to interupt it so i typed out contrl c command to interrupt the application and obtain the flag
```bash
/challenge/run
^c (ctrl + c)
```

## What I learned
sometimes you just want to get rid of the process that's clogging up your terminal, terminals have a hotkey for this: Ctrl-C sends an "interrupt" to whatever application is waiting on input from the terminal and this causes the application to cleanly exit
## References 
https://pwn.college/linux-luminarium/processes/


4.
# Challenge Name
killing misbehaving processes

## My solve
**Flag:** `pwn.college{4YRTIRrHqjyu9eJjtxvGIP0pOsg.0FNzMDOxwCM4gjNzEzW}`

- so i typed out ps auxww which is the command to show all the processes and piped it through to search for the required process where i grepped decoy to print out all the processes whose names have decoy.
-  i noted the pid id of the process which was 142 and used the kill command to kill the process or stop the process and then ran the run command which allowed the falg to be sent to the flag_fifo file from which i had to use cat to open the fifo file and print out the flag
- since fifo files only run when both read and write mode run at the same time we should open another terminal and cat the fifo file for it to run and obtain the flag

```bash
ps auxww | grep decoy
kill 142
/challenge/run
cat /challenge/flag_fifo
```

## What I learned
sometimes some processes mmight disturb the running of a certain command and it is necessary to kill them so kill command is very necessary at such times as well as grep to search out the process causing the problem
## References 
https://pwn.college/linux-luminarium/processes/


5.
# Challenge Name
suspending processes

## My solve
**Flag:** `pwn.college{cePfwSr2xulkCK2ZIveW5_RTQPy.QX1QDO0wCM4gjNzEzW}`

- so here we run the run command but the challenge was to interupt the process subtly so by pressing ctrl+z i interupted the process and then ran the process again since that was the goal of the challenge to obatin the flag

```bash
/challenge/run
^z (ctrl+z)
/challenge/run
```

## What I learned
ctrl-C interupts processes but ctrl-Z suspends processes in the background subtly
## References 
https://pwn.college/linux-luminarium/processes/


6.
# Challenge Name
resuming processing

## My solve
**Flag:** `pwn.college{oRw7cYzkfT1mBIcR0d29nuXkYBF.QX2QDO0wCM4gjNzEzW}`

- i ran the run command but the main piont was to learn how to resume a command after interupting it so first i interupted the command using ctrl-z then used the fg command which essentially resumes the process and brings it back onto the terminal

```bash
/challenge/run
^z (ctrl+Z)
fg
```

## What I learned
fg command is command which resumes an interrputed process back on to the terminal
fg stands for foreground
## References 
https://pwn.college/linux-luminarium/processes/


7.
# Challenge Name
backgrounding processes

## My solve
**Flag:** `pwn.college{0g-FsUbj1YJ79O2BwIGQl4pw-k9.QX3QDO0wCM4gjNzEzW}`

- at first i ran the run command but the challenge wanted me to run the same command again to obtain the flag so i suspended the process using ctrl-z and used the bg command which essentially allowed the process to keep running which giving me the shell back to invoke more commands and then i ran the challenge again so that the system recognised two same processed and provided the flag

```bash
/challenge/run
^z
bg
/challenge/run
```

## What I learned
- we can resume processes using bg command which stands for background, htis allows the process to keep running, while giving you your shell back to invoke more commands in the meantime.
- bg (background): Resumes a stopped job or sends a running job to the background so that it continues execution without occupying your command-line interface. You can then continue working in the terminal.
fg (foreground): Brings a background or suspended job back to the foreground, allowing it to interact directly with the terminal.
- The bg Command
The bg command is used to resume a stopped job and keep it running 'behind the scenes.'
Syntax: bg [%job_number]
Effect: The job resumes execution, but its output will still occasionally print to your terminal, and it cannot receive input from the keyboard.
Example: If you run a long command and press Ctrl + Z (it stops), running bg will make it continue in the background.
-The fg Command
The fg command is used to bring a background or suspended job 'back to the interactive command line.'
Syntax: fg [%job_number]
Effect: The job becomes the active process. It can now accept keyboard input, and its output is clearly displayed, pausing your ability to type new commands until the job is completed or suspended again.
Example: If you run a text editor like vim and send it to the background, running fg will bring the text editor window back up for interactive use.
(refer to the description for this particular part in pwn collage since it is given in a little more detail regarding the nomenclature of the ps command explaining which state each process is in) --->>


[{how to view the differences between suspended and backgrounded properties. First, let's suspend a sleep:

hacker@dojo:~$ sleep 1337
^Z
[1]+  Stopped                 sleep 1337
hacker@dojo:~$
The sleep process is now suspended in the background. We can see this with ps by enabling the stat column output with the -o option:

hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 T    sleep 1337
hacker       782 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$ 
See that T? That means that the process is suspended due to our Ctrl-Z. The S in bash's STAT column means that bash is sleeping while waiting for input. The R in ps's column means that it's actively running, and the + means that it's in the foreground!

Watch what happens when we resume sleep in the background:

hacker@dojo:~$ bg
[1]+ sleep 1337 &
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 S    sleep 1337
hacker      1224 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$
The sleep now has an S. It's sleeping while, well, sleeping, but it's not suspended! It's also in the background and thus doesn't have the +.
}]

## References 
https://pwn.college/linux-luminarium/processes/


8.
# Challenge Name
foreground processing

## My solve
**Flag:** `pwn.college{IkKZgeo4avam3JyXWVdPKwSWPpG.QX4QDO0wCM4gjNzEzW}`

- i typed out the command to run the program and then suspended it using ctrl+z followed by bg to the run the process in the background which essentially resumes it providing the shell back. Then i typed out the fg command to bring this command from happening in the background to the foreground as told by the challenge and then obtained the flag

```bash
/challenge/run
^z
bg
fg
```

## What I learned
we can foreground a process running in the background by simply usng the fg command which brings it to the foregorund from the background or from a suspended state
## References 
https://pwn.college/linux-luminarium/processes/


9.
# Challenge Name
starting background processes

## My solve
**Flag:** `pwn.college{IMqPzELzxFzGd9te0Y7x1U8YQ3Z.QX5QDO0wCM4gjNzEzW}`

- the challenge was do directly run the command in the background so i used the (&) sign after the command

```bash
/challenge/run &
```

## What I learned
the (&) starts the process directly in the background and should by argumented after the command 
## References 
https://pwn.college/linux-luminarium/processes/


10.
# Challenge Name
process exit codes

## My solve
**Flag:** `pwn.college{Icl3hgUgIRT8uShU85bJ6oQaf6N.QX5YDO1wCM4gjNzEzW}`

- i ran the get-code command to obtain the code but the command exited with an error so then i typed out the command $? which gave me the code that has to be argumented to submit code to obtain the flag

```bash
/challenge/get-code
echo $?
/challenge/submit-code 253
```

## What I learned
- Every shell command, including every program and every builtin, exits with an exit code when it finishes running and terminates. This can be used by the shell, or the user of the shell to check if the process succeeded in its functionality
- You can access the exit code of the most recently-terminated command using the special ? variable prepended by $ to read the value as well as echo for terminal to print it out
- commands that succeed typically return 0 and commands that fail typically return a non-zero value, most commonly 1 but sometimes an error code that identifies a specific failure mode
## References 
https://pwn.college/linux-luminarium/processes/




Module-10
Untangling users


1.
# Challenge Name
becoming root with su

## My solve
**Flag:** `pwn.college{0WyneUvgXPqx6HbLnhu-ZutGTIE.QX1UDN1wCM4gjNzEzW}`

- to become root i have to run the su command so i did so and then typed out the given password to get control of the root. once i got control of the root i used the cat command so that the terminal prints out the flag

```bash
su
hack-the-planet
cat /flag
```

## What I learned
- There are MANY users on a typical Linux system! The full list of users on a Linux system is specified in the /etc/passwd file
- One important user is root: the system administrator. The system administrator has obvious security implications: a hacker user that can somehow, through various functionalities of Linux, become the root user would be able to wreak havoc on the system. A very frequent goal of hackers breaking into systems is to escalate to root, and thus root must be defended at all cost
- It's not just hackers that need to become root. Oftentimes, you, as the owner of your computer, need to use root access to administer it. Becoming root is a fairly common action that Linux users take, and there are two utilities that exist for this purpose: su and sudo.
- we will cover the older one, su (the substitute user command). This is not typically used to elevate to root access anymore, but it is an elegant utility from a more civilized time
- su is setuid binary
- hacker@dojo:~$ ls -l /usr/bin/su
-rwsr-xr-x 1 root root 232416 Dec 1 11:45 /usr/bin/su
- Because it has the SUID bit set, su runs as root. Running as root, it can start a root shell but before allowing the user to elevate privileges to root, it checks to make sure that the user knows the root password
- this checking of root password made it old fashioned
- Modern systems very rarely have root passwords, and different mechanisms are used to grant administrative access.
## References 
https://pwn.college/linux-luminarium/users/


2.
# Challenge Name
other users with su

## My solve
**Flag:** `pwn.college{MWMd6OLmA_Szu5MxvA1DMy-4rE2.QX2UDN1wCM4gjNzEzW}`

- since su lets me access the root terminal i can argument it with a username so i argumented it with zardus and typed out the password to get control of the root

```bash
su zardus
dont-hack-me
```

## What I learned
- With no arguments, su will start a root shell. However, you can also give a username as an argument to switch to that user instead of root.
- ```hacker@dojo:~$ su some-user
Password:
some-user@dojo:~$```

## References 
https://pwn.college/linux-luminarium/users/


3.
# Challenge Name
cracking passwords

## My solve
**Flag:** `pwn.college{8wjeiJCXSsBzK8YqHFoZalKY4W8.QX3UDN1wCM4gjNzEzW}`

- to solve the challenge as mentioned at first i use the john command famous for john the ripper(read what i learned) and add the shadow-leak as an argument where the it cracks the password hash contained in the file. Soon a prompt pops up saying session completed and after they we type out the su command to crack the rood folllowed by the username of the user and then type ot the crack password to gain control of the root. then we run the program run to obtain the flag

```bash
john /challenge/shadow-leak
su zardus
aardvark
/challenge/run
```

## What I learned
- When you enter a password for su, it compares it against the stored password for that user. These passwords used to be stored in /etc/passwd, but because /etc/passwd is a globally-readable file, this is not good for passwords, these were moved to /etc/shadow
- When you input a password into su, it one-way-encrypts (hashes) it and compares the result against the stored value. If the result matches, su grants you access to the user
- If you have the hashed value of the password, you can crack it. Even though /etc/shadow is, by default, only readable by root, leaks can happen! For example, backups are often stored, unencrypted and insufficiently protected, on file servers, and this has led to countless data disclosures.
- If a hacker gets their hands on a leaked /etc/shadow, they can start cracking passwords and wreaking havoc. The cracking can be done via the famous John the Ripper
- ```hacker@dojo:~$ john ./my-leaked-shadow-file
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Will run 32 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password1337      (zardus)
1g 0:00:00:22 3/3 0.04528g/s 10509p/s 10509c/s 10509C/s lykys..lank
Use the "--show" option to display all of the cracked passwords reliably
Session completed```

- john is a command which is an open source utility which helpd decrypt the encrypted password or hack and can be used using the john commmand argumented with the file
## References 
https://pwn.college/linux-luminarium/users/


4.
# Challenge Name
using sudo

## My solve
**Flag:** `pwn.college{keSz6gkX0nwFTS7evaj_npNIH6_.QX4UDN1wCM4gjNzEzW}`

- normall to read the flag we need root permissions but here we can directly read the flag and we are given acces to sudo which provides us the root priveleges and hence i cat the flag file to obtain the flag
```bash
sudo cat /flag
```

## What I learned
- sudo: Stands for "substitute user do" or "super-user do." It allows a permitted user to execute a command as the superuser (root) or another user
- Linux system had a root password that administrators would use to su to root (after logging into their account with their normal account password). But root passwords are a pain to maintain, they (or their hashes!) can leak, and they don't lend themselves well to larger environments, the world has moved from administration via su to administration via sudo 
- the world has moved from administration via su to administration via sudo which checks policies to determine whether the user is authorized to run commands as root. These policies are defined in /etc/sudoers

## References 
https://pwn.college/linux-luminarium/users/



Module 11
Perceving_permissions

1.
# Challenge Name
changing file ownership

## My solve
**Flag:** `pwn.college{wMIdNIS-WbrVU5vr5I7IxtCzjoO.QXxEjN0wCM4gjNzEzW}`

- Used the chown command to assign ownership of the /flag file to the hacker user. The challenge explicitly grants you the ability to use chown as the hacker user, which is usually a root-only command.
- now since i got the root permission i simply cat the flag

Bash
```bash
chown hacker /flag
cat /flag
```

## What I learned
- The challenge goal is to read the contents of the /flag file. Normally, the /flag file is owned by the root user, which prevents a regular user like hacker from reading it. The key to solving the level is the chown command, which is used to change the owner of a file. In this specific challenge, the hacker user is given special temporary permission to use chown
- chown stands for change owner
## References 
https://pwn.college/linux-luminarium/permissions/


2.
# Challenge Name
groups and files

## My solve
**Flag:** `pwn.college{MQfDTuePzVZMCG9lSaS9pWovTTM.QXxcjM1wCM4gjNzEzW}`

- The challenge states that the flag is readable by whatever group owns it, but it's currently owned by the root group. so we are granted special permission to use chgrp as the hacker user so i used the chgrp command to chage the group to hacker and then accordingly used cat command to obtain the flag but at the first try it printed out a pratice flag but on restaring the shell it provided the proper flag

```bash
chgrp hacker /flag
cat /flag
```

## What I learned
- Sharing is caring, and sharing is built into Linux's design. Files have both an owning user and group. A group can have multiple users in it, and a user can be a member of multiple groups. We can check what groups you are part of with the "id" command
- The /flag file is currently owned by the root user and the root group. The hacker user cannot read it because they are neither the owner nor a member of the owning group. but i am granted permission to use chgrp command which changed the ownership of the file to be obtained
## References 
https://pwn.college/linux-luminarium/permissions/


3.
# Challenge Name
fun with group names

## My solve
**Flag:** `pwn.college{wu6NivfMKqaZu4hTe5YqGd00zRS.QXycjM1wCM4gjNzEzW}`

- the challenge didnt mention which grp had the control of the flag file so i used the id command to see which all groups i was a part of and used trial and error to check which  group had the access to open the flag so i used the chgrp command to change my group to the first group which was shown in the ```id``` and luckily it had the access to flag to hence i used the cat command and obtained the file but yet again i had to restart the privelege since the system popped a practice flag the first time i ran the command

```bash
id
chgrp grp30837 /flag
cat /flag
```

## What I learned
- There is a convention in Linux that every user has their own group, but this does not have to be the case. For example, many computer labs will put all of their users into a single, shared users group.
- the ```id``` command helps you look at which all groups the user(here me) is a part of
## References 
https://pwn.college/linux-luminarium/permissions/


4.
# Challenge Name
changing permissions

## My solve
**Flag:** `pwn.college{4oUUEICVHVx0Tz5BYPFUGeeETbv.QXzcjM1wCM4gjNzEzW}`

- chmod is a commond we can change mode and permissions for many things, so i used chmod to add read permissions to others on the flag file and cat the flag file to obtain flag
- The /flag file is owned by the root group, preventing the hacker user from reading it and the file's permissions allow group members to read the file. Since, we are  empowered to use the chgrp command, which is normally reserved for root. we changed the file's group ownership from root to hacker so we the hacker group, can finally read the flag.

```bash
chmod o+r /flag
cat /flag
```

## What I learned
- the first character there is the file type. The next nine characters are the actual access permissions of the file or directory, split into 3 characters denoting permissions for the owning user (now you understand this!), 3 characters denoting the permissions for the owning group (now you understand this as well!), and 3 characters denoting the permissions that all other access (e.g., by other users and other groups) has to the file.

- For college_file above, the (rw-r--r--) permissions entry decodes to:
r: the user that owns the file (user hacker) can read it
w: the user that owns the file (user hacker) can write to it
-: the user that owns the file (user hacker) cannot execute it
r: users in the group that owns the file (group hacker) can read it
-: users in the group that owns the file (group hacker) cannot write to it
-: users in the group that owns the file (group hacker) cannot execute it
r: all other users can read it
-: all other users cannot write to it
-: all other users cannot execute it

- Like ownership, file permissions can also be changed. This is done with the chmod (change mode) command. The basic usage for chmod is:
chmod [OPTIONS] MODE FILE
- examples:
u+r, as above, adds read access to the user's permissions
g+wx adds write and execute access to the group's permissions
o-w removes write access for other users
a-rwx removes all permissions for the user, group, and 

## References 
https://pwn.college/linux-luminarium/permissions/


5.
# Challenge Name
excutable files

## My solve
**Flag:** `pwn.college{YjMP1MyGtsDEozo9akx019iHLx6.QXyEjN0wCM4gjNzEzW}`

- at first i used the chmod option and added the excute option to other users for the /challenge/run program and ls -l to the list of processes running but unfortunately the owner only had persmisson to read the file so u used chmod to give owner permmission to excute file and then ran the command to succesfulle obtain the flag

```bash
hacker@permissions~executable-files:~$ chmod o+x /challenge/run
hacker@permissions~executable-files:~$ ls -l /challenge/run
-r--r--r-x 1 hacker hacker 32 Jan 14  2025 /challenge/run
hacker@permissions~executable-files:~$ chmod u+x /challenge/run
hacker@permissions~executable-files:~$ /challenge/run
Successful execution! Here is your flag:
```

## What I learned
- from the learning from the previous operations i learnt how to use chmod effectively and changed the mode for owner and others as well as used the ```ls -l``` command to understand the permissions for the flag file with respect to the owner, group and others
## References 
https://pwn.college/linux-luminarium/permissions/


6.
# Challenge Name
permission tweaking pratice

## My solve
**Flag:** `pwn.college{c-DWj0PkDHG9JdSjY2yGXHiQRbQ.QXwEjN0wCM4gjNzEzW}`

- here is start of by running the run command to start the challenge where i had to use the + and - signs to user or group or other and tweak permissions 8 times in order to get the ownership of the file and then i used the chmod command to allow reading persmission for the flag and used the cat command to read the flag

```bash
/challenge/run
<<<8 different command based on the tasts given for 8 rounds>>
chmod u+r /flag
cat /flag
```

## What I learned
- since we know the rading of the file using + and - we can tweak permissions for the user or group or other individually using chmod command to obtain a flag in the challeneg or generally to gain control of a file or directory
## References 
https://pwn.college/linux-luminarium/permissions/


7.
# Challenge Name
permissions setting practice

## My solve
**Flag:** `pwn.college{41GHsbqabv31-F-SyQ9aRNZZdlw.QXzETO0wCM4gjNzEzW}`

- - here is start of by running the run command to start the challenge where i had to use the + and - signs as well as = to set the permissions to user or group or other and tweak permissions 8 times in order to get the ownership of the file and then i used the chmod command to allow reading persmission for the flag and used the cat command to read the flag

```bash
/challenge/run
<<<8 different command based on the tasts given for 8 rounds>>
chmod u+r /flag
cat /flag
```

## What I learned
- since we know the rading of the file using + and - we can tweak permissions for the user or group or other individually using chmod command to obtain a flag in the challeneg or generally to gain control of a file or directory
- here we can use = to set the command directly as well as a , to seperate more than one commands in the same line
- (=-) stands for removing all the permissions for a user or group or others

## References 
https://pwn.college/linux-luminarium/permissions/


8.
# Challenge Name
the SUID bit

## My solve
**Flag:** `pwn.college{Y52BneQlsHiHUk-vo2d2QMDjylG.QXzEjN0wCM4gjNzEzW}`

- Since the /challenge/getroot program is owned by root, setting the SUID bit is the mechanism to get the program to run as root. Since u+s is the standard way to set the SUID bit on the user (u) permissions and nnce the SUID bit is set, executing the program will launch it with root privileges. The challenge confirmed this program is designed to then give you a root shell so then since we got the root permission we go ahead and cat the flag file to obatin the flag.

```bash
choms u+s /challenge/getroot
/challenge/getroot
cat /flag
```

## What I learned
- there are many cases in which non-root users need elevated access to do certain system tasks. The system admin can't be there to give them the password every time a user wanted to do a task that only root/sudoers can do. Instead, the "Set User ID" (SUID) permissions bit allows the user to run a program as the owner of that program's file.
- The s part in place of the executable bit means that the program is executable with SUID. It means that, regardless of what user runs the program, the program will execute as the owner use
- As the owner of a file, you can set a file's SUID bit by using chmod:
chmod u+s [program]

## References 
https://pwn.college/linux-luminarium/permissions/




Module-12
Chaining commands


1.
# Challenge Name
chaining with semicolons

## My solve
**Flag:** `pwn.college{87pKVpxFC-NhJOotbDkgtWqkpxY.QX1UDO0wCM4gjNzEzW}`

-  i sed a semicolon as it effectively helps me run two commands in one command
```bash
/challenge/pwn; /challenge/college
```

## What I learned
semicolon works as a break and then runs the first command followed by the second command and prevents us from clicking enter and typing a command all over again
## References 
https://pwn.college/linux-luminarium/chaining/


2.
# Challenge Name
building on success

## My solve
**Flag:** `pwn.college{srHw6sbbJggVe-Et8tqR3wz4bM2.0lM0MDOxwCM4gjNzEzW}`

- i rain the first command followed by the && operator so that it checks if the first command ran succesfully and runs the second command
```bash
/challenge/first-sucsess && /challenge/second
```

## What I learned
&& operator checks if the first command succeeds and the runs the second command
## References 
https://pwn.college/linux-luminarium/chaining/


3.
# Challenge Name
handling failure

## My solve
**Flag:** ` pwn.college{QVyYdi14HFwbUZV_CLB5Zl-99Ek.01M0MDOxwCM4gjNzEzW}`

- i ran the first command followed by the or operator which essecntially runs the second command only when the first command fails so here the first command was bound to fail an it did running the second command and printing out the flag

```bash
/challenge/first-failure || /challenge/second
```

## What I learned
- the || operator allows you to run a second command only if the first command fails (exits with a non-zero code). This is called the "OR" operator because either the first command succeeds OR the second command will run.
- hacker@dojo:~$ command1 || command2
## References 
https://pwn.college/linux-luminarium/chaining/


4.
# Challenge Name
your first shell script

## My solve
**Flag:** `pwn.college{YiQoUesNYMMBh_PIR60L6eOHa-K.QXxcDO0wCM4gjNzEzW}`

- since we had to run two commands through a file at first we open a text editor (here vs code) and i typed in two commands which i wanted to run in the terminal and saved the file with a name and sh extension which stands for shell.
- then i move to the terminal and type of bash followed by the name of the file so the terminal runs the commands in the shell file and prints the flag

```bash
<in a text editor
/challenge/pwn
/challenge/college>

bash x.sh
```

## What I learned
- As you combine more and more commands to achieve complex effects, the length of the combined prompt quickly gets really annoying to deal with. When this happens, you can put these commands in a file, called a shell script, and run them by executing the file
- We can create a shell script called pwn.sh and then we can execute by passing it as an argument to a new instance of our shell (bash)
## References 
https://pwn.college/linux-luminarium/chaining/


5.
# Challenge Name
redirecting script output

## My solve
**Flag:** `pwn.college{YZASDEMJ_2zB3QR87LyLAaxhtG7.QX4ETO0wCM4gjNzEzW}`

- the file of x.sh was already saved on desktop and consists of two commands required by the challenge to run. Next i piped the file using bash commands which essentially runs these commands into /solve file as said by the challenge to obtain the flag

```bash
bash x.sh | /challenge/solve
```

## What I learned
- if we wanted to send the output of several programs to one command we can redirect the input and output using the pipe command
- All of the various redirection methods work: > for stdout, 2> for stderr, < for stdin, >> and 2>> for append-mode redirection, >& for redirecting to other file descriptors, and | for piping to another command.
## References 
https://pwn.college/linux-luminarium/chaining/


6.
# Challenge Name
executable shell scripts

## My solve
**Flag:** `pwn.college{8OoWXqTH3uZSYCDR2zCcbPDQVqh.QX0cj    M1wCM4gjNzEzW}`

- to run the command without bash at first i saved a file x.sh and typed out a command in the file required by the challenged and used the chmod function to add the excute permission to the user so that we can directly read the flag and then typed out the file location in the terminal to obtain the flag without bash since we provided excuting permission to the user

```bash
<in text editor
/challenge/solve>
ls -l
chmod u+x x.sh
/home/hacker/x.sh
```

## What I learned
- we can avoid the need to manually invoke bash, if our shell script file is executable
- we can create the file and change the permission using chmod command so that file cann be excutavle by typing its location instead of bash command
## References 
https://pwn.college/linux-luminarium/chaining/


7.
# Challenge Name
understanding shebangs

## My solve
**Flag:** `pwn.college{YyiK8ZcY5RhdCJsg0HXfGAYV18_.0VOzMDOxwCM4gjNzEzW}`

- as the challenge has explained i created a file called solve with the shell extension and typed the first line as a shebang as it tells linux to use /bin/bash interpreter to excute rest of the commands followed by using the echo command to prinnt out hack the planet text as mentioned. Then i moved to ther terminal and used the chmod command to provide excuting acces to the user for the solve file and ran the /challenge/run command for the system to verify if the opertaion actually works

```bash
<text editor
#!/bin/bash
echo "hack the planet">
chmod u+x /home/hacker/solve.sh
/challenge/run
```

## What I learned
- our shellscripts can only be launched from the shell. Things worked great in the previous level because i was invoking my script from the bash shell, but they won't work if the script was being invoked by, say, a program written in Python (or any other language).
- When a program is invoked in Linux, the Linux kernel first inspects the file to determine how it should be run. This does NOT use the extension rather, Linux looks at the first few bytes of the file for this information.
- There are a bunch of different types of programs, but if the program file starts with the characters #! (often termed a "shebang"), Linux treats the file as an interpreted program, and the contents of the rest of the line as the path to the interpreter
- ```#!/bin/bash
echo "Hello Hackers!"```
When ./script.sh was executed, Linux opened the file, read the first line, extracted /bin/bash as the interpreter, and executed /bin/bash ./script.sh to launch the script
- Note, the shebang line must be the VERY FIRST line of the file - no blank lines or spaces before it
- Common shebangs you might see:
#!/bin/bash for bash scripts
#!/usr/bin/python3 for Python scripts
#!/bin/sh for POSIX shell scripts

## References 
https://pwn.college/linux-luminarium/chaining/


8.
# Challenge Name
scrpiting with arguments

## My solve
**Flag:** `pwn.college{QiU5nbYwOTS2ZNzzFHGkW47wDsP.0VNzMDOxwCM4gjNzEzW}`

- i move to the text editor and then typed out the shebang at first for linux to look at it as an interpreter program followed by the command where i used echo to tell the system to print the second argument which can be mapped to $2 first follwed by first argument mapped to $1 and print them on to the terminal
- i ran the shellscript using bash command and then run command for the system to check and print the flag

```bash
<text editor
#!/bin/bash
echo "$2 $1">
bash home/hacker/solve.sh hello world
/challenge/run
```

## What I learned
- The script can access these arguments using special variables:
$1 contains the first argument ("hello")
$2 contains the second argument ("world")
...and so on
- example:
```
<text editor
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2">
hacker@dojo:~$ bash myscript.sh hello world
First argument: hello
Second argument: world 
```
## References 
https://pwn.college/linux-luminarium/chaining/


9.
# Challenge Name
scripting with conditionals

## My solve
**Flag:** `pwn.college{8t0Zwpp3zaGo1FCEl9P1A33L5r9.0lNzMDOxwCM4gjNzEzW}`

- at first i write a code in the text editor starting of with a shebang followed by the if statement to print college if pwn argument is given after excuting the statement. Then i run the shellscript using bash and run the challenge/run command for the system to check and provide the flag

```bash
<text editor
#!/bin/bash
if [ "$1" == "pwn" ]
then
    echo "college"
fi
>
bash /home/hacker/solve.sh pwn
/challenge/run
```

## What I learned
- we can include if statement in bash commands where the syntax is different than c and instead of else there is an fi statement
- example: 
```if [ "$1" == "ping" ]
then
    echo "pong"
fi
```
here the terminal prints pong if the entered argument is ping or return nothing if argument is something else
## References 
https://pwn.college/linux-luminarium/chaining/


10.
# Challenge Name
scripting with default cases    

## My solve
**Flag:** `pwn.college{ADmq-eA2qnxSrgWGWDm0Mb3q57y.01NzMDOxwCM4gjNzEzW}`

- i moved to the text editor to create a solve file and typed in the first line as a shebang followed by if statement which prints college if pwn is argumented and noep if something else in printed followed by fi coomand which entes the conditonal statement. Then i run the file using the bash command, the path of the file followed by pwn command and confirmed college got printed and then followed the run command for the system to chekc and provide the falg

```bash
<text editor
#!/bin/bash
if [ "$1" == "pwn" ]
then
    echo "college"
else
    echo nope
fi>
bash /home/hacker/solve.sh pwn
/challenge/run
```

## What I learned
- The else clause executes when the if condition is false
- example: 
```if [ "$1" == "hello" ]
then
    echo "Hi there!"
else
    echo "I don't understand"
fi
```
- Note that the else doesn't have a condition --- it catches everything that didn't match previously. It also doesn't have a then statement. Finally, the fi goes after the else block to denote the end of the whole complex statement
## References 
https://pwn.college/linux-luminarium/chaining/


11.
# Challenge Name
scripting with multiple conditions

## My solve
**Flag:** `pwn.college{Y7fgSTNLt5TKX5SN-Bg5p6-fdAN.0FOzMDOxwCM4gjNzEzW}`

- since the challenge requires multiple conditions to be used i use the elif command for specific conditions in the text editor and wrote a shellscript followed by run command which checked my script for all possible conditions and printed the flag

```bash
<text editor
#!/bin/bash
if [ "$1" == "hack" ]
then
    echo "the planet"
elif [ "$1" == "pwn" ]
then
    echo "college"
elif [ "$1" == "learn" ]
then
    echo "linux"
else
    echo "unknown"
fi>
/challenge/run
```

## What I learned
- You can use elif also note that you do need a then after the elif, just like the if. As before the else at the end catches everything that didn't match.
- NOTE: As you're creating your script, make sure to follow the spacing closely in the examples. Unlike many other languages, bash requires the [ and the ] to be separated from other characters by spaces, otherwise it cannot parse the condition.
## References 
https://pwn.college/linux-luminarium/chaining/


12.
# Challenge Name
reading shell scripts

## My solve
**Flag:** `pwn.college{sRQZQX4c-9dfpbB3z6TnJ_XhTfS.0lMwgDOxwCM4gjNzEzW}`

- so i used cat to open the program /challenge/run where the guess or argument should be hack the PLANET for the system to give th flag so then i ran the command and the system asked for a password and i typed out the guess value for which flag will be printed and obtained the flag

```bash
cat /challenge/run
/challenge/run
hack the PLANET
```

## What I learned
-  shellscripts are very handy for doing simple "system-level" tasks and some require us to put a secret password to run the command present in the shellscript.
## References 
https://pwn.college/linux-luminarium/chaining/




Module-13
Terminal Multiplexing


1.
# Challenge Name
launching screen

## My solve
**Flag:** `pwn.college{c3U5RIHZZnyDGBefa8XUYdLJEYP.0VN4IDOxwCM4gjNzEzW}`

- the only command in the challenge was to start the virtual terminals so i typed out the screen command to open a virtual terminal and after a while the system printed the flag

```bash
screen
```
## What I learned
- screen is a program that creates virtual terminals inside your terminal. It's somewhat like having multiple browser tabs, but for your command line!
Starting screen is super simple:
hacker@dojo:~$ screen
- typing exit or press Ctrl-D to leave the screen session. Then screen will terminate and return us to our original shell.
## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/


2.
# Challenge Name
detaching and attaching

## My solve
**Flag:** `pwn.college{wreAVcNvALMCS_HC1GHTqnqgRuf.0lN4IDOxwCM4gjNzEzW}`

- at first i launch the screen command to open a virtual terminal and detach it on purpose useing control A and d key which stands for detach and leaves the session running the background. Then run the /challenge/run command to send the flag to the detached session and then we use the screen command followed by the -r argument for the terminal to reattach the screen to obtain the flag

```bash
screen
^A (ctrl+A)
d key
/challenge/run
screen -r
```

## What I learned
- you're working on something important over a remote connection, and your connection drops,  with a normal terminal, everything's gone but with screen, your work keeps running, and you can reattach later.
- You can also detach on purpose, which we'll do in this challenge. You detach by pressing Ctrl-A, followed by d, this leaves your session running in the background while you return to your normal terminal. To reattach, you can use the -r argument to screen.

hacker@dojo:~$ screen
## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/


3.
# Challenge Name
finding sessions

## My solve
**Flag:** `pwn.college{UcY4irec720ataP0lqBkwjlQomU.01N4IDOxwCM4gjNzEzW}`

- at first i used the screen -ls command which printed all the virtual terminals running at the momment and using hit and trial one by one i used the screen -r command argumented with the name of the terminal i want to reattach so that the system prints the right flag.
```bash
screen -ls
screen -r session_f5ad7d31003c4ecf
```

## What I learned
- If you become an avid screen user, you will inevitably end up with multiple sessions running and to look at them we can use the ```screen -ls``` command.
- The identifiers of the sessions are the PID of each respective screen process, a dot, and the name of the screen session. To attach to a specific one, you use its name or its PID by giving it as an argument to screen -r.
- hacker@dojo:~$ screen -ls
There are screens on:
        23847.mysession   (Detached)
        23851.goodwork    (Detached)
        23855.morework    (Detached)
3 Sockets in /run/screen/S-hacker.
- ex: hacker@dojo:~$ screen -r goodwork (where goodwork is the screen terminal connected to be attached)

## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/


4.
# Challenge Name
switching windows

## My solve
**Flag:** `pwn.college{E6GVUfYo6VIs2dP5DXdt1CZWnA7.0FO4IDOxwCM4gjNzEzW}`

-  at first we reattach the screen using screen -r command where it prints the different windows running and then we use the same command argumented with the challenge_session where the terminal takes us to window 1. There i use the ctrl+A followed by 0 command to switch the window to window 0 since we were in window 1 and once i switched to window 0 the system printed the flag.

```bash
screen -r
screen -r challenge_session
ctrl+A 0
```

## What I learned
- Inside a single screen session, you can have multiple windows, like your browser has multiple tabs. This can be super handy for organizing different tasks!
These windows are handled with different keyboard shortcuts, all starting with Ctrl-A:
Ctrl-A c - Create a new window
Ctrl-A n - Next window
Ctrl-A p - Previous window
Ctrl-A d - detach window
Ctrl-A 0 through Ctrl-A 9 - Jump directly to window 0-9
Ctrl-A " - bring up a selection menu of all of the windows
- these shorcut keys help perform different tasks in different virtual terminals created in a terminal
## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/


5.
# Challenge Name
detaching and attaching (tmux)

## My solve
**Flag:** `pwn.college{0kZbJjES9sw--0W6PdoLwZORFRM.0VO4IDOxwCM4gjNzEzW}`

- at first i created a terminal using tmux command and once i am in as mentioned i exited the terminal using ctrl+b and d key followed by run command which attached the flag to the tmux terminal. Then using the tmux -a command i attached the terminal back where i found the key printed.

```bash
tmux
ctrl+b d key
/challenge/run
tmux -a
```

## What I learned
- tmux (terminal multiplexer) is screen's younger, more modern cousin. It does all the same things but with some different key bindings. Instead of Ctrl-A, tmux uses Ctrl-B as its command prefix, So to detach from tmux, you press Ctrl-B followed by d.
- The commands also differ:
tmux ls - List sessions
tmux attach or tmux a - Reattach to session
## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/


6.
# Challenge Name
switchinng windows (tmux)

## My solve
**Flag:** `pwn.college{wP-193xZ6SCsT3eHSW35b3vhRmr.0FM5IDOxwCM4gjNzEzW}`

- i start by typing in the tmux command argumented with a standing fro attach to start or attach the terminal window where window 1 gets attached where a popup says that switching to window 0 will provide the flag so then i click ctrl+B and then argument it with 0 which essentially tells the terminal to change to the 0th window where the flag is printed.

```bash
tmux a
ctrl+B 0
```

## What I learned
- just like screen, tmux has windows. The key combos are different, but the concept is the same:
Ctrl-B c - Create a new window
Ctrl-B n - Next window
Ctrl-B p - Previous window
Ctrl-B 0 through Ctrl-B 9 - Jump to window 0-9
Ctrl-B w - See a nice window picker
- Tmux shows your windows at the bottom in a status bar that looks like:
[0] 0:bash* 1:bash
The * shows your current window, and each entry also shows the process that the window was created to run.
## References 
https://pwn.college/linux-luminarium/terminal-multiplexing/




Module-14
Pondering PATH


1.
# Challenge Name
the path variable

## My solve
**Flag:** `pwn.college{QcSXVtSESf8jPNiC4zVmPO50I9M.QX2cDM1wCM4gjNzEzW}`

- the challenge wanted me to disrupt /run file so i typed out the special variable path which stores commands so here it stores rm command, so i set path to nothing so that rm command can no more be used by the /run file and hence on running it the system cant find the rm command and fails to delete the fllag hence proivding the flag.

```bash
PATH=""
/challenge/run
```

## What I learned
- here is a special shell variable, called PATH, that stores a bunch of directory paths in which the shell will search for programs corresponding to commands but Without a PATH, bash cannot find the ls command.
- ex: ```hacker@dojo:~$ PATH=""
hacker@dojo:~$ ls
bash: ls: No such file or directory```

## References 
https://pwn.college/linux-luminarium/path/


2.
# Challenge Name
setting path

## My solve
**Flag:** `pwn.college{QttyW_8isF8Ifu6g4u-RMGCcSEK.QX1cjM1wCM4gjNzEzW}`

- to launch the the /run file by name at first i changed the path variable to a specific directory where /challenge/run file is present. Once i set the correct path i simply ran the file to obtain the flag just by the bare name

```bash
PATH=/challenge/more_commands/
/challenge/run
```

## What I learned
- If you maintain useful scripts that you want to be able to launch by bare name, we can do it by adding directories to or replacing directories in this list, you can expose these programs to be launched using their bare name
- For example:
hacker@dojo:~$ PATH=/home/hacker/scripts
hacker@dojo:~$ goodscript
YEAH! This is the best script!
## References 
https://pwn.college/linux-luminarium/path/


3.
# Challenge Name
finding commands

## My solve
**Flag:** `pwn.college{YRlPW7rId-Q8SeTrg_pRhGmetQv.01NzEzNxwCM4gjNzEzW}`

- since the flag is located in the same path of win i type out which win which prints the path of the win command. Next i use the cat command and used the same path followed by flag to tell the system to open that file and hence it openes that file printing out the flag

```bash
which win
cat /challenge/paths/13103/flag
```

## What I learned
- which command lists the path of the command
- When you type the name of a command, something inside one of the many directories listed in your $PATH variable is what actually gets executed.
- Mirroring what the shell does when searching for commands, which looks at each directory in $PATH in order and prints the first file it finds whose name matches the argument you passed.
- ex: hacker@dojo:~$ which cat
/bin/cat
hacker@dojo:~$ /bin/cat /flag
YEAH
hacker@dojo:~$
## References 
https://pwn.college/linux-luminarium/path/


4.
# Challenge Name
adding commands

## My solve
**Flag:** `pwn.college{EY3NgWLupzWO_vAQCQv6ndmaAzq.QX2cjM1wCM4gjNzEzW}`

- We created a executable shellscript named win where we typed out the shebang at the top for the function as mentioned before and type out the path of cat followed by the/flag file which essentially conatins command to read the flag file. Then we made it excutable by using chmod command and argumenting the path.
- Then what we do is we export the path and typing the path we want to set it to the path environment variable and tell it to perform the task.By setting export PATH=/tmp/pwn:$PATH, we make the search order look at our malicious directory first.
- Then we type challenge/run which runs the shellscript first and then any other command.

```bash
which cat
<text editor
#!/bin/bash
/run/dojo/bin/cat /flag >
chmod +x /home/hacker/win.sh
export PATH=/home/hacker:$PATH
/challenge/run
```

## What I learned
- The objective was to read the highly restricted flag file located at /flag but The /challenge/run script runs with root privileges and tries to execute the command simply as win. Because it doesn't use the full path, it relies on the shell's $PATH variable.
- The location of cat command file is something we obtained as a path.
- The command export PATH=/tmp/pwn:$PATH is a powerful shell instruction that temporarily changes the search order for every command executed by your shell
- The $PATH variable is a colon-separated list of directories where the shell looks for executable programs.
- : - It tells the shell where one directory path ends and the next one begins.
- $PATH	The variable expansion of the current `$PATH* value. This takes all the standard, default system directories (like /usr/bin, /bin, etc.) and appends them to the end of the new list.
- For every command I or any program I launch run, first check the /home/hacker directory, and only then start searching the rest of the standard system directories.
- By setting export PATH=/tmp/pwn:$PATH, we make the search order look at our malicious directory first.
- Root's shell checks the $PATH: It finds our /home/hacker/win.sh before finding any win command and our script runs with the privileges of the parent process—root—allowing it to use the special cat binary to read the protected /flag file.

## References
https://pwn.college/linux-luminarium/path/


5.
# Challenge Name
hijacking commands

## My solve
**Flag:** `pwn.college{QScatSog_bjLALLkrQUJgWvlLxr.QX3cjM1wCM4gjNzEzW}`

- i renamed the file to rm and then as before i typed out the shebang and command to cat the file. Then i used chmod to provide executing access and then altered the path to the /home/hacker where rm is present. Then i ran the /run program so it gets tricked and runs the rm program in /home/hacker which tells it to print the flag.

```bash
<text editor
#!/bin/bash
/run/dojo/bin/cat /flag >
chmod +x /home/hacker/rm
export PATH="/home/hacker:$PATH"
/challenge/run
```

## What I learned
- $PATH	The variable expansion of the current `$PATH* value. This takes all the standard, default system directories (like /usr/bin, /bin, etc.) and appends them to the end of the new list.
- we can trick the system to first open a file in another directory before anything else where we type certain commands in that so it excutes those first before anything else.
- this is one of the ways of expliaiting small vulnerabilities in the system to crack in.
## References 
https://pwn.college/linux-luminarium/path/

















