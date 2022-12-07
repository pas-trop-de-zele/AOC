#pragma once

class SNode {
public:
  char elem;
  SNode *next;
};

class CharLinkedList {
private:
  SNode *head;
  bool checkRecurse (SNode *ptr); // for Problem 3; Implement in CharLinkedList.cpp

public:
  CharLinkedList(): head(nullptr) {}
  void addFront(char x);

  bool checkList(); // for Problem 2; Implement in CharLinkedList.cpp

  // recursion helper function called from main for PROBLEM 3
  bool checkRecurseHelper ();
};
