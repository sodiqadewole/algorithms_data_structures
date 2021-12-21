#include <iostream>
using namespace std;

class Country{
    string name;
    int population;
    public:
    Country(string name, int population){
        this->name = name;
        this->population = population;
    }
    string getName(){
        return name;
    }
};

class Person{
    string name;
    Country* Cobj; // A pointer to a country object
    public:
    Person(string name, Country* Cobj){
        this->name = name;
        this->Cobj = Cobj;
    }
    string printDetails(){
        cout << "Name: " << name << endl;
        cout << "Country: " << Cobj->getName() << endl;
    }
};

int main(){
    Country* Cobj = new Country("Utopia", 1);
    {
        Person user("Benjamin Udesh", Cobj);
        user.printDetails();
    }
    // The user object's lifetime is over
    cout << Cobj->getName() << endl; // The country object still exists!

}