#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    cout << "+------------------------------+" << endl;
    cout << "|    Reverse String Example    |" << endl;
    cout << "+------------------------------+" << endl;
    
    const int LINE_SIZE = 512;
    char line[LINE_SIZE];

    cout << "Please enter a string to reverse" << endl << "or EOF to quit: ";
    
    cin.getline(line, LINE_SIZE);
    if (cin.fail())
    {
        cin.clear();
        return 0;
    }

    char* p = line;
    char* q = line + strlen(line) - 1;
    while (p < q)
    {
        char temp = *p;
        *p = *q;
        *q = temp;

        p++;
        q--;
    }

    cout << "Reversed string: " << line << endl;

    return 0;
}