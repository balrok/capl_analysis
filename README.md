# capl_analysis
Static analysis for capl code by translation to C.

## How it works
Capl looks very similar to C/CPP code. When not so many capl-specific constructs are in your code base it is quite simple to convert a
capl-file to C.
Having code in C allows to use all kind of static analysis tools.

This project is based on the C-grammar from antlr. A few CAPL-specifc constructs are added to it (`includes{}`, `variables{}` sections and the `on ..{}` blocks). When parsing a CAPL file these constructs are converted.
Some simplifications are done and you probably need to add some more methods, so no compiler warnings will happen.

## Installation
You need antlr4 and python3 installed.

```
# Install the python requirements
pip install --user -r requirements.txt
# Build the antlr-tools from the Capl grammar.
antlr4 -Dlanguage=Python3 Capl.g4
```

## How to use

### Convert to .cpp
```
./run.py file1.can file2.can > out.cpp
```

Converting to cpp requires to specify all .can files as the includes are not automatically resolved. The order is not important - it will
automatically generate function declarations. You can
also create a file like this:
```
file1.can
file2.can
..
```
And call: `./run.py `cat filelist` > out.cpp`

### Static analysis on .cpp

```
g++ -Wall -Wextra -ferror-limit=99999 -O3 -fstack-protector-all -fmudflap -lmudflap -c out.cpp
```

#### Other tools

* http://clang-analyzer.llvm.org/scan-build.html
* http://cppcheck.sourceforge.net/

### Fixing Bugs in the conversion

As initially said this conversion is not complete. If a CAPL-constant or CAPL-method is missing, you can add this in `run.py` in the
`print_global_functions` method.

#### Not working / Bugs

The conversion CAN-specific things likel `msg.` and `this.` is implemented by string replacement and not very robust. 

The special arrays which can contain strings as keys are not implemented

Unspecified multidemensional arrays. E.g. as parameter to a function following is valid: `void func(int arr[][])`. My solution is to do
string replacement on it `replace("[][], "[][10]")` - which might yield falsse-positives for array out of bound.

Basically it is the best to stick closest to CPP like code and it works fine.

## Difference of Capl.g4 to C.g4

To track the differences I added the original C-grammar to the source code. Just do a `diff -Nau Capl.g4 C.g4`.

# Contributing

Please message me and I'll add you to this repository if you want to help improving this code.
