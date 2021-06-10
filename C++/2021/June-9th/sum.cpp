#include <iostream>

using namespace std;

int main()
{
    cout << "+------------------------------------+" << endl;
    cout << "|        Add Integers Example        |" << endl;
    cout << "+------------------------------------+" << endl;

    int num;
    int sum = 0;

    while (true)
    {
        cout << "Please enter an integer or EOF: ";
        cin >> num;
        if (cin.eof())
        {
            break;
        }

        if (cin.fail())
        {
            cout << "Invalid Input" << endl;
            cin.clear();
            cin.ignore(INT16_MAX,'\n');
            continue;
        }

        sum += num;
    }

    cin.clear();

    cout << "The sum is " << sum << endl;
    return 0;

}