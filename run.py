#!/usr/bin/env python3

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
#from antlr4 import *
from CaplLexer import CaplLexer
from CaplParser import CaplParser
# from MyCaplListener import MyCaplListener
from CaplToCListener import CaplToCListener
import tqdm
#from filecache import filecache

import sys


# TODO how to cache the tree
def getTree(file):
    input = FileStream(file, encoding="iso-8859-15")
    lexer = CaplLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CaplParser(stream)
    tree = parser.compilationUnit()
    return tree

def getFileContent(file):
    with open(file, encoding="iso-8859-15") as f:
        return f.read().split("\n")

def main(argv):
    # cl = MyCaplListener()
    cl = CaplToCListener()

    with tqdm.tqdm(total=len(argv)-1) as pbar:
        for file in argv[1:]:
            pbar.set_description(file)
            pbar.update(1)
            cl.file_content = getFileContent(file)
            tree = getTree(file)
            walker = ParseTreeWalker()
            walker.walk(cl, tree)


    # includes - manually
    print("#include <string>")

    # typedefs - manually
    print("// typedefs")
    print("")
    print("typedef unsigned int word;")
    print("typedef unsigned int dword;")
    print("typedef unsigned int byte;")
    print("typedef unsigned int msTimer;")
    #print("typedef unsigned int message;")
    print("struct message {int id; int msgChannel;int byte_0;int byte_1;int byte_2;int byte_3;int byte_4;int byte_5; int byte_6;int byte_7;int byte_8;int byte_9;int word_0;int word_1;int word_2;int word_3;int word_4;int word_5; int word_6;int word_7;int word_8;int word_9; int dlc;};")
    
    # capl functions
    print("")
    print("")
    print("// capl functions")
    print("")
    print_global_functions()
    # global vars
    print("")
    print("")
    print("// global variables")
    print("")
    for v in cl.global_vars:
        print("static ", end="")
        v.print_raw()

    print("")
    print("")
    print("// global functions which require my custom types")
    print("")
    print_global_functions_specifc()
    # funcdefs
    print("")
    print("")
    print("// function definitions")
    print("")
    for f in cl.all_functions:
        f.print_header()
    # functions
    print("")
    print("")
    print("// functions")
    print("")
    for f in cl.all_functions:
        f.print_raw()
        print("")



    # print("Global vars:")
    # for v in cl.global_vars:
    #     if not v.used:
    #         v.print()
    # print("Functions:")
    # for f in cl.all_functions:
    #     for v in f.vars:
    #         if not v.used:
    #             v.print()

def print_global_functions():
    print("void write(std::string a){}")
    print("void write(std::string a, std::string a1){}")
    print("void write(std::string a, std::string a1, float a2){}")
    print("void write(std::string a, float a0, std::string a1, float a2){}")
    print("void write(std::string a, void * a1){}")
    print("void write(std::string a, void * a1, void * a2){}")
    print("void write(std::string a, void * a1, void * a2, void * a3){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5, void * a6){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5, void * a6, void * a7){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5, void * a6, void * a7, void * a8){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5, void * a6, void * a7, void * a8, void * a9){}")
    print("void write(std::string a, void * a1, void * a2, void * a3, void * a4, void * a5, void * a6, void * a7, void * a8, void * a9, void * a10){}")
    print("void write(std::string a, float a1){}")
    print("void write(std::string a, float a1, float a2){}")
    print("void write(std::string a, float a1, float a2, float a3){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5, float a6){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5, float a6, float a7){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5, float a6, float a7, float a8){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5, float a6, float a7, float a8, float a9){}")
    print("void write(std::string a, float a1, float a2, float a3, float a4, float a5, float a6, float a7, float a8, float a9, float a10){}")
    print("void write(std::string a, std::string a1, std::string a2, std::string a3, std::string a4, std::string a5, std::string a6, std::string a7, std::string a8, std::string a9, std::string a10){}")
    print("void write(std::string a, std::string a1, float a11, std::string a2, float a21, std::string a3, float a31, std::string a4, float a41, std::string a5, float a51, std::string a6, float a61, std::string a7, float a71, std::string a8, float a81, std::string a9, float a91){}")
    print("int sysGetVariableInt(std::string a, std::string a1){ return 0; }")
    print("long sysGetVariableLong(std::string a, std::string a1){ return 0; }")
    print("long sysGetVariableLongLong(std::string a, std::string a1){ return 0; }")
    print("void sysSetVariableInt(std::string a, std::string a1, int a2){ }")
    print("void sysSetVariableLong(std::string a, std::string a1, long a2){ }")
    print("void sysSetVariableLongLong(std::string a, std::string a1, long a2){ }")
    print("void sysSetVariableString(std::string a, std::string a1, char a2[]){ }")
    print("int random(long a) {return 0;}")
    #print("void snprintf(std::string a, int a2, std::string b) {}")
    print("int elcount(int a) { return 0;}")
    print("int elcount(void * a) { return 0;}")
    print("int _max(int a, int a1) { return 0;}")
    print("int _min(int a, int a1) { return 0;}")
    print("float cos(float a) { return 0;}")
    print("float sin(float a) { return 0;}")
    print("float arctan(float a) { return 0;}")
    print("float sqrt(float a) { return 0;}")
    print("int abs(int a) { return 0;}")
    print("float _round(float a) { return 0;}")
    print("float _floor(float a) { return 0;}")
    print("void cancelTimer(msTimer a) { }")
    print("void setTimer(msTimer a, long a1) { }")
    print("void fileClose(int a) { }")
    print("dword openFileWrite(char buf[], int a){return 0;}")
    print("void filePutString (char buf[], int a, dword fh){}")
    print("void output(message * a) { }")
    print("float pi = 3.14;")

def print_global_functions_specifc():
    print("void memcpy(struct position a, struct position b) {}")
    print("void memcpy(struct P36MoveType a, struct P36MoveType b) {}")

    #     for i in ['sysGetVariableInt', 'sysGetVariableLong', 'sysSetVariableInt', 'sysSetVariableLong', 'random'
    #               ,'memcpy', 'snprintf', 'write', 'elcount', '_max', 'cos', 'abs', 'sin', '_round', '_floor', '_min'
    #               , 'cancelTimer', 'fileClose']:
if __name__ == '__main__':
    main(sys.argv)
