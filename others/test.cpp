#include <iostream>
#include string
using namespace std;

class Vehicle{
    protected:
    string Make;
    string Color;
    int Year;
    string Model;

    public:
    Vehicle(){
        string Make = "";
        string Color = "";
        int Year = 0;
        string Model = "";
    }

    Vehicle(string mk, string col, int yr, string mod){
        Make = mk;
        Color = col;
        Year = yr;
        Model = mod;
    }

    void print_details(){
        cout << "Manufacturer: " << Make << endl;
        cout << "Color: " << Color << endl;
        cout << "Year: " << Year << endl;
        cout << "Model: " << Model << endl;
    }
};

class Cars: public Vehicle{
    string trunk_size;

    public:
    Cars(){
        trunk_size = "";
    }

    Cars(string mk, string col, int yr, string mod, string ts)
        :Vehicle(mk, col, yr, mod){
            trunk_size = ts;
    }

    ~Car(){
        cout << endl << "Car class Destructor!";
    }

    void car_details(){
        print_details();
        cout << "Trunk size: " << trunk_size << endl;
    }
};

class Ships: public Vehicle{
    int Number_of_Anchors;

    public:
    Ships(){
        Number_of_Anchors = 0;
    }

    Ships(string mk, string col, int yr, string mod, int num_anch)
        :Vehicle(mk, col, yr, mod){
            Number_of_Anchors = num_anch;
    }

    ~Ship(){
        cout << endl << "Ship class Destructor!";
    }

    void ship_details(){
        print_details();
        cout << "Number of Anchors: " << Number_of_Anchors << endl;
    }
};

/*
Multi-level inheritance
#include <iostream>
using namespace std;

class A {
  public:
    void init() {
      cout << "Class A initialized!" << endl;
    }
    void update() {
      cout << "Class A updated!" << endl;
    }
};

class B : public A {
  public:
    void update() {
      cout << "Class B updated!" << endl;
    }
};

class C : public B { };

int main() {
  // your code goes here
  C c;
  c.init();
  c.update();
  return 0;
}
*/

int main(){
    Cars car("Chevrolet", "Black", 2010, "Camaro", "9.1 cubic feet");
    car.car_details();
    cout << endl;

    Ships ship("Harland and Wolff, Belfast", "Black and White", 1912, "RMS Titanic", 3);
    ship.ship_details();
}