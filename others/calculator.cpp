class Calculator{
    float num1;
    float num2;

    public:
    Calculator(){
        num1 = 0;
        num2 = 0;
    }
    // Calculator(float n1, float n2){
    //     num1 = n1;
    //     num2 = n2;
    // }

    float add(float n1, float n2){
        num1 = n1;
        num2 = n2;
        return num1 + num2;
    }

    float subtract(float n1, float n2){
        num1 = n1;
        num2 = n2;
        return num2 - num1;
    }

    float multiply(float n1, float n2){
        num1 = n1;
        num2 = n2;
        return num2 * num1;
    }

    float divide(float n1, float n2){
        num1 = n1;
        num2 = n2;
        return num2 / num1;
    }
};

int main(){
    Calculator calc;
    calc.add(10.0, 15.0);
    calc.subtract(15.0, 10.0);
    calc.multiply(12.0, 4.0);
    calc.divide(12.0, 4.0);
}