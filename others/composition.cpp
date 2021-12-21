#include <iostream>
using namespace std;

class Engine{
    int capacity;
    public:
    Engine(){
        capacity=0;
    }
    Engine(int capacity){
        this->capacity=capacity;
    }
    void Engine_details(){
        cout << "Engine size: " << capacity << endl;
    }
};

class Tyres{
    int num_tyres;
    public:
    Tyres(){
        num_tyres=0;
    }
    Tyres(int num_tyres){
        this->num_tyres=num_tyres;
    }
    void Tyre_details(){
        cout << "Number of tyres: " << num_tyres << endl;
    }
};

class Doors{
    int num_doors;
    public:
    Doors(){
        num_doors=0;
    }
    Doors(int num_doors){
        this->num_doors=num_doors;
    }
    void Door_details(){
        cout << "Number of doors: " << num_doors << endl;
    }
};

class Car{
    Engine Eobj;
    Tyres Tobj;
    Doors Dobj;
    string color;
    public:
    Car(Engine eng, Tyres tyre, Doors door, string color)
        : Eobj(eng), Tobj(tyre), Dobj(door){
            this->color = color;
        }
    void Car_details(){
        Eobj.Engine_details();
        Tobj.Tyre_details();
        Dobj.Door_details();
        cout << "Car color: " << color << endl;
    }
};

int main(){
    Engine Eobj(3700);
    Tyres Tobj(4);
    Doors Dobj(4);
    cout << "--Car details--" << endl;
    Car Cobj(Eobj, Tobj, Dobj, "Black");
    Cobj.Car_details();
}