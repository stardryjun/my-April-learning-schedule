#include <iostream>

class Stack{
    int capacity=5;
    int* arr = new int[capacity];
    int top = -1;
    public:
        Stack(int x){
            arr[0] = x;
            top = 0;
        }
        void push(int x){
            if(top == capacity - 1){
                capacity *= 2;
                arr = (int*)realloc(arr, capacity * sizeof(int));
            }
            arr[++top] = x;
            return;
        }
        void pop(){
            if(top>=0){
                top --;
                return;
            }else{
                std::cout << "stack is empty" << std::endl;
            }
        }
        void print(){
            for(int i = 0; i <= top; i++){
                std::cout << arr[i] << " ";
            }
            std::cout << std::endl;
        }
};

int main(){
    Stack s(1);
    s.push(2);
    s.push(3);
    s.print();
    s.pop();
    s.pop();
    s.pop();
    s.pop();
    s.print();
    return 0;
}