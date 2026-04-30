#include <iostream>
#include <cstdlib>

class List{
    private:
        int* arr;
        int capacity;
        int current;
    public:
        List(int s){
            capacity = s;
            arr = new int[capacity];
            current = 0;
        }
        ~List(){
            delete[] arr;
        }
        void add(int value){
            if(current < capacity){
                arr[current] = value;
                current++;
            }else{
                capacity *= 2;
                arr = (int*)realloc(arr, capacity * sizeof(int));
                arr[current] = value;
                current++;
            }
        }
        void insert(int index, int value){
            if(index > current+1 || index < 0){
                std::cout << "Index out of bounds" << std::endl;
                return;
            }else{
                if(index == current){
                    add(value);
                    return;
                }
                if(current == capacity){
                    capacity *= 2;
                    arr = (int*)realloc(arr, capacity * sizeof(int));
                }
                for(int i = current; i > index; i--){
                    arr[i] = arr[i-1];
                }
                arr[index] = value;
                current++;
            }
        }
        void deleteAt(int index){
            if(index >= current || index < 0){
                std::cout << "Index out of bounds" << std::endl;
                return;
            }else{
                for(int i = index; i < current-1; i++){
                    arr[i] = arr[i+1];
                }
                current--;
            }
        }
        int size(){
            return current;
        }
        int get(int index){
            if(index >= current || index < 0){
                std::cout << "Index out of bounds" << std::endl;
                return -1;
            }else{
                return arr[index];
            }
        }
        void print(){
            for(int i = 0; i < current; i++){
                std::cout << arr[i] << " ";
            }
            std::cout << std::endl;
        }
};

int main(){
    List mylist(2);
    mylist.add(1);
    mylist.add(2);
    mylist.insert(0, 3);
    mylist.print();
    mylist.deleteAt(1);
    mylist.print();
}