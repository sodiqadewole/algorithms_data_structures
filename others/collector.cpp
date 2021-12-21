#include <iostream>
#include <string>
using namespace std;

class Collector {
    int * list;
    int size;
    int capacity;

    public:
    // Default constructor
    Collector(){
        // We define the default values for the data members
        list = nullptr;
        size = 0;
        capacity = 0;
    }


    // Parameterized constructor
    Collector(int cap){
        // Arguments are used as values
        capacity = cap;
        size = 0;
        list = new int[capacity];
    }

    bool append(int v){
        if (size < capacity){
            list [size++ ] = v;
            return true;
        }
        return false;
    }

    // Print function
    void dump(){
        for(int i=0; i<size; i++){
            cout << list[i] << " ";
        }
        cout << endl;
    }

    // Destructor
    ~Collector(){
        cout << "Deleting the object " << endl;
        if (capacity > 0)
            delete[] list;
    }
};

int main(){
    // Create instance of the constructor
    Collector *c;
    c = new Collector(10);
    for (int i = 0; i < 15; i++){
        cout << c->append(i) << endl;
    }
    delete c;
    cout << "Exiting program" << endl;
}