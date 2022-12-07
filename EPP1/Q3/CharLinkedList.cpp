// ADD ANSWER TO THIS FILE

#include "CharLinkedList.h"
bool CharLinkedList::checkList() {
	SNode* cur = head;
	int prev = 0;
	while(cur) {
		if (prev >= cur->elem) {
			return false;
		}
		prev = cur->elem;
		cur = cur->next;
	}
	return true;
}

bool CharLinkedList::checkRecurse (SNode *ptr) {
	if (!ptr || !ptr->next) {
		return true;
	}
	bool result = checkRecurse(ptr->next);
	bool cur = ptr->elem < ptr->next->elem;
	return cur && result;

}

void CharLinkedList::addFront(char x) {
  SNode *tmp = head;
  head = new SNode;
  head->next = tmp;
  head->elem = x;
}

// recursion helper function called from main for PROBLEM 3
bool CharLinkedList::checkRecurseHelper () {
  return checkRecurse(head);
}
