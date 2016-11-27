#include <string>
// typedefs

typedef unsigned int word;
typedef unsigned int dword;
typedef unsigned int byte;
typedef unsigned int msTimer;
struct message {int id; int msgChannel;int byte_0;int byte_1;int byte_2;int byte_3;int byte_4;int byte_5; int byte_6;int byte_7;int byte_8;int byte_9;int word_0;int word_1;int word_2;int word_3;int word_4;int word_5; int word_6;int word_7;int word_8;int word_9; int dlc;};


// capl functions

void write(std::string a, ...){}
int sysGetVariableInt(std::string a, std::string a1){ return 0; }
long sysGetVariableLong(std::string a, std::string a1){ return 0; }
long sysGetVariableLongLong(std::string a, std::string a1){ return 0; }
void sysSetVariableInt(std::string a, std::string a1, int a2){ }
void sysSetVariableLong(std::string a, std::string a1, long a2){ }
void sysSetVariableLongLong(std::string a, std::string a1, long a2){ }
void sysSetVariableString(std::string a, std::string a1, char a2[]){ }
int random(long a) {return 0;}
int elcount(...) { return 0;}
int _max(int a, int a1) { return 0;}
int _min(int a, int a1) { return 0;}
float cos(float a) { return 0;}
float sin(float a) { return 0;}
float arctan(float a) { return 0;}
float sqrt(float a) { return 0;}
int abs(int a) { return 0;}
float _round(float a) { return 0;}
float _floor(float a) { return 0;}
void cancelTimer(msTimer a) { }
void setTimer(msTimer a, long a1) { }
void fileClose(int a) { }
dword openFileWrite(char buf[], int a){return 0;}
void filePutString (char buf[], int a, dword fh){}
void output(message * a) { }
float pi = 3.14;
void memcpy(...) {}


// global variables

static int test;
static int test_notused;
static int test_array[10];


// global functions which require my custom types



// function definitions

int main();
void handle_message();
void test_notused_method();
void test_method(char a);
void test_capl_msg0();
void test_capl_msg(message * msg);


// functions

int main(){
	test = 13;

	test_array[3] = 1;
	test_array[13] = 1; // testing out of bounds with a constant
	test_array[test] = 1; // testing out of bounds with a variable
	test_method(test); // converting int to char - gives an error?
	test_capl_msg0();
return 0;}

void handle_message(){ message * msgthis;
  if (msgthis->id >= 0x100 && msgthis->id <= 0x100+(10*0x10)+10) { // cmd to server
      write("STATUS - %d", msgthis->id);
  }
}

void test_notused_method(){ } // intentionally not used

void test_method(char a){
}

void test_capl_msg0(){
  message * msg;
  test_capl_msg(msg);
}

void test_capl_msg(message * msg){
  msg->id = 0x0200;  // broadcast id
  msg->dlc = 6;
  msg->byte_0 = 1;
  msg->byte_1 = 2;
  msg->byte_2 = 3;
  msg->byte_3 = 4;
  msg->word_4 = 5;
  output(msg);
}

