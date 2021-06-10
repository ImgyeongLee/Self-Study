#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
    cout << "+----------------------------------+" << endl;
    cout << "|        Print Menu Example        |" << endl;
    cout << "+----------------------------------+" << endl;

    const float coffeePrice = 1.25f;
    const float lattePrice = 4.75f;
    const float breakfastComboPrice = 12.104f;

    // size_t - This is a kind of variable type which is similar to unsigned int
    const size_t nameColumnLength = 20;
    const size_t priceColumnLength = 10;

    // set the circumstance of the cout
    cout << left << fixed << showpoint << setprecision(2);

    cout << setfill('-') << setw(nameColumnLength + priceColumnLength) << "" << endl << setfill(' '); // initialize the blank places
    cout << setw(nameColumnLength) << "Name" << setw(priceColumnLength) << "Price" << endl;
    cout << setfill('-') << setw(nameColumnLength + priceColumnLength) << "" << endl << setfill(' ');

    cout << setw(nameColumnLength) << "Coffee" << "$" << coffeePrice << endl;
    cout << setw(nameColumnLength) << "Latte" << "$" << lattePrice << endl;
    cout << setw(nameColumnLength) << "Breakfast Combo" << "$" << breakfastComboPrice << endl;

    return 0;
}