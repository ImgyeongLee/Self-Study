#pragma once
#include <iostream>
#include <string>

using namespace std;

struct Record
{
    string FirstName;
    string LastName;
    string StudentID;
    string Score;    
};

namespace samples
{
    Record ReadRecord(istream& stream, bool bPrompt);
    
    void WriteFileRecord(fstream& outputStream, const Record& record);

    void DisplayRecords(fstream& fileStream);

    void ManageRecordsExample();
}