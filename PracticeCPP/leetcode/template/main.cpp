// TODO: FOLLOW https://stackoverflow.com/questions/62910867/how-to-run-tests-and-debug-google-test-project-in-vs-code

#include "main.h"
#include <iostream>
using namespace std;

// Returns true if and only if n is a prime number.
bool IsPrime(int n) {
    if (n == 0 || n == 1) {
        return false;
    }

    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// int main() {
//     int n = 7;
//     if (IsPrime(n)) {
//         cout << n << " is a prime number" << endl;
//     } else {
//         cout << n << " is not a prime number" << endl;
//     }
// }
