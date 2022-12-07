//
// EDIT THIS FILE ONLY FOR YOUR OWN TESTING
// WRITE YOUR CODE IN CharLinkedList.cpp
//

#include <iostream>
#include <string>
#include "CharLinkedList.h"

using std::string;
using std::cout;
using std::endl;
bool checkAnswer(const string &nameOfTest, bool received, bool expected);

int main() {
  cout << "Test if the characters in a linked list are in sorted order" << endl;
  {
    CharLinkedList mylist;
    mylist.addFront('n');
    mylist.addFront('i');
    mylist.addFront('g');
    mylist.addFront('e');
    mylist.addFront('b');
  	string s = "List: b -> e -> g -> i -> n";
  	checkAnswer(s, mylist.checkList(), true);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('r');
    mylist.addFront('a');
    mylist.addFront('e');
    mylist.addFront('b');
  	string s = "List: b -> e -> a -> r";
  	checkAnswer(s, mylist.checkList(), false);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('a');
    mylist.addFront('t');
    mylist.addFront('l');
    mylist.addFront('e');
    mylist.addFront('d');
  	string s = "List: d -> e -> l -> t -> a";
  	checkAnswer(s, mylist.checkList(), false);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('x');
  	string s = "List: x";
  	checkAnswer(s, mylist.checkList(), true);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('y');
    mylist.addFront('t');
    mylist.addFront('i');
    mylist.addFront('e');
    mylist.addFront('d');
  	string s = "List: d -> e -> i -> t -> y";
  	checkAnswer(s, mylist.checkList(), true);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('s');
    mylist.addFront('e');
    mylist.addFront('r');
    mylist.addFront('o');
    mylist.addFront('l');
    mylist.addFront('o');
    mylist.addFront('d');
  	string s = "List: d -> o -> l -> o -> r -> e -> s";
  	checkAnswer(s, mylist.checkList(), false);
  }
  {
    CharLinkedList mylist;
    mylist.addFront('t');
    mylist.addFront('f');
    mylist.addFront('a');
    mylist.addFront('d');
  	string s = "List: d -> a -> f -> t";
  	checkAnswer(s, mylist.checkList(), false);
  }
}

bool checkAnswer(const string &nameOfTest, bool received, bool expected) {
    if (received == expected) {
        cout << std::boolalpha << "PASSED " << nameOfTest << ": expected and received " << received << endl;
        return true;
    }
    cout << std::boolalpha << "FAILED " << nameOfTest << ": expected " << expected << " but received " << received << endl;
    return false;
}
