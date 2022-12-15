#include "CarInventory.h"
#include <iomanip> // std::setprecision
#include <iostream>
#include <string>

using std::cout;
using std::string;

bool testAnswer(const string &nameOfTest, double received, double expected);
template <typename T>
bool testAnswer(const string &nameOfTest, const T &received, const T &expected);

int main() {
    {
        CarInventory cars;
        cout << "Reading data file ...\n";
        cars.readFile("data.txt");
        testAnswer("averageMileage(Corolla)", cars.averageMileage("Corolla"), 35454);
        testAnswer("averageMileage(Camry)", cars.averageMileage("Camry"), 119073);
        testAnswer("averageMileage(RAV4)", cars.averageMileage("Fiat"), -1);
        testAnswer("averageMileage(CRV)", cars.averageMileage("CRV"), 33554);
        testAnswer("averageMileage(Focus)", cars.averageMileage("Focus"), 105201);
    }
}

bool testAnswer(const string &nameOfTest, double received, double expected) {
    if ((received - expected) > -0.01 && (received - expected) < 0.01) {
        cout << "PASSED " << std::setprecision(9) << nameOfTest << ": expected and received " << received << "\n";
        return true;
    }
    cout << "FAILED " << std::setprecision(9) << nameOfTest << ": expected " << expected << " but received " << received << "\n";
    return false;
}

template <typename T>
bool testAnswer(const string &nameOfTest, const T &received, const T &expected) {
    if (received == expected) {
        cout << "PASSED " << nameOfTest << ": expected and received " << received << "\n";
        return true;
    }
    cout << "FAILED " << nameOfTest << ": expected " << expected << " but received " << received << "\n";
    return false;
}
