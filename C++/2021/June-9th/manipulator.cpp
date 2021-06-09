#include <iostream>
#include <string>
#include <iomanip> // to use some manipulators

using namespace std;

// Manipulator (조정자)

int main()
{
    // 1) showpos/noshowpos - show the positive integer sign or do not

    int num1 = 10;

    cout << showpos << num1 << endl; // +10
    cout << noshowpos << num1 << endl; // 10

    cout << "------------------------------" << endl;

    // 2) dec/hex/oct - decimal, hexadecimal, octal
    int num2 = 18;
    cout << dec << num2 << endl; // decimal - 18
    cout << hex << num2 << endl; // hexadecimal - 16
    cout << oct << num2 << endl; // octal - 22

    cout << "------------------------------" << endl;

    // 3) uppercase/nouppercase - show the alphabet as uppercase or do not (only for the number, no string, no bool)
    
    int num3 = 13;
    string str = "hello";

    cout << uppercase << str << endl; // hello
    cout << nouppercase << str << endl; // hello
    cout << uppercase << hex << num3 << endl; // D
    cout << nouppercase << hex << num3 << endl; // d

    cout << "------------------------------" << endl;

    // 4) showbase/noshowbase - show the some signs (e.g 0x) or do not

    cout << showbase << num3 << endl; // 0xd
    cout << noshowbase << num3 << endl; // d

    cout << "------------------------------" << endl;

    // 5) left/internal/right - alligning

    cout << left << showpos << dec << num3 << endl; // +13
    cout << internal << setw(5) << showpos << num3 << endl; // +   13
    cout << right << setw(5) << showpos << num3 << endl; //   +13
    // Once we use dec/hex/oct manipulator, cout will print out the number with the same format

    cout << "------------------------------" << endl;

    // 6) fixed/scientific - the way to print a number

    float num4 = 123.4568;

    cout << fixed << noshowpos << num4 << endl; // 123.456802
    cout << scientific << num4 << endl; // 1.234568e+002

    cout << "------------------------------" << endl;

    // 7) boolalpha/noboolalpha - the way to show bool variables

    bool is_bool = true;

    cout << fixed << boolalpha << is_bool << endl; // true
    cout << noboolalpha << is_bool << endl; // 1

    cout << "------------------------------" << endl;

    // 8) Some manipulators in iomanip header

    string str2 = "Deepbread";

    cout << setw(15) << str2 << endl; // set the blank spaces
    cout << setfill('*') << setw(15) << str2 << endl; // fill the blank spaces
    cout << setprecision(10) << num4 << endl; // 123.4568023682

    return 0;
}
