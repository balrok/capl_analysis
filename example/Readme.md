# Example

A short example program so that you can see if it works correctly

## Conversion

```
../run.py Controller.can can_msg.cin > example.cpp
```

You can also compare it to example.gold.cpp `diff -a example.cpp example.gold.cpp`.

## Analysis

### cppcheck

```
cppcheck example.gold.cpp

Checking example.gold.cpp ...
[example.gold.cpp:69]: (error) Array 'test_array[10]' accessed at index 13, which is out of bounds.
[example.gold.cpp:70]: (error) Array 'test_array[10]' accessed at index 13, which is out of bounds.
[example.gold.cpp:76]: (error) Uninitialized struct member: msgthis.id
[example.gold.cpp:88]: (error) Uninitialized variable: msg
```

The last two lines are problems to handle `message *` things. And are problems of the conversion not the code.

You can also use `cppcheck --enable=all --inconclusive -f example.gold.cpp`


### g++
From gcc

`g++ -Wall -Wextra -ferror-limit=99999 -c example.gold.cpp`

### scan-build
From clang: http://clang-analyzer.llvm.org/scan-build.html

`scan-build g++ -c example.gold.cpp`
