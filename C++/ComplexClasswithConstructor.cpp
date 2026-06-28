#include <iostream>
using namespace std;

class Complex {
    float real, imag;

public:
    // Default constructor
    Complex() {
        real = 0;
        imag = 0;
    }

    // Parameterized constructor
    Complex(float r, float i) {
        real = r;
        imag = i;
    }

    void showData() {
        cout << real << " + j" << imag;
    }

    Complex sum(Complex c1) {
        Complex c3;
        c3.real = real + c1.real;
        c3.imag = imag + c1.imag;
        return c3;
    }
};

int main () {
    Complex obj1(3,4), obj2(4,5), obj3;
    obj3 = obj1.sum(obj2);

    cout << "\nComplex Number1: "; obj1.showData();
    cout << "\nComplex Number2: "; obj2.showData();
    cout << "\nSum: "; obj3.showData();
    return 0;
}