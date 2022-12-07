#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;
bool checkAnswer(const string &nameOfTest, bool received, bool expected);
// Implement printString here
void printString(const string& s) {
	for (auto c : s) {
		cout << c << '.';
	}
	cout << endl;
}
// Implement testString here
bool testString(const string& s) {
	// Since the ascii code of the smallest character > 0, use 0 as a starting value
	int prev = 0;
	for (auto c : s) {
		if (prev >= c) {
			return false;
		}
		// update prev with the current character
		prev = c;
	}
	return true;
}
// EDIT CODE BELOW *ONLY* FOR TESTING (ANY CODE BELOW WILL BE OVER-WRITTEN DURING GRADING WITH DIFFERENT TESTS)
int main() {
  cout << "Test if the characters in a string are in sorted order" << endl;
  {
    string s = "begin";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), true);
  }
  {
    string s = "bear";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), false);
  }
  {
    string s = "delta";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), false);
  }
  {
    string s = "x";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), true);
  }
  {
    string s = "deity";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), true);
  }
  {
    string s = "dolores";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), false);
  }
  {
    string s = "to";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), false);
  }
  {
    string s = "daft";
    cout << "Contents of array : ";
    printString(s);
    checkAnswer(s, testString(s), false);
  }
  return 0;
}
bool checkAnswer(const string &nameOfTest, bool received, bool expected) {
    if (received == expected) {
        cout << std::boolalpha << "PASSED " << nameOfTest << ": expected and received " << received << endl;
        return true;
    }
    cout << std::boolalpha << "FAILED " << nameOfTest << ": expected " << expected << " but received " << received << endl;
    return false;
}