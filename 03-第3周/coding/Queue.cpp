#include <iostream>

class Queue {
    int* arr;
    int front;
    int rear;
    int capacity;
    int size;
public:
    Queue(int n): front(0), rear(0), capacity(n), size(0) {
        arr = new int[capacity];
    }
    ~Queue(){
        delete[] arr;
    };
    void push(int x){
        if (full()) {
            std::cout << "Queue is full!" << std::endl;
            return;
        }
        arr[rear] = x;
        rear = (rear + 1) % capacity;
        size++;
    }
    void pop(){
        if (empty()) {
            std::cout << "Queue is empty!" << std::endl;
            return;
        }
        front = (front + 1) % capacity;
        size--;
    }
    int frontelement(){
        return arr[front];
    }
    bool empty(){
        return size == 0;
    }
    bool full(){
        return size == capacity;
    }
};

int main() {
    Queue q(5);
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);
    q.push(6); // Queue is full!

    std::cout << "Front element: " << q.frontelement() << std::endl; // Front element: 1

    q.pop();
    std::cout << "Front element after pop: " << q.frontelement() << std::endl; // Front element after pop: 2

    return 0;
}