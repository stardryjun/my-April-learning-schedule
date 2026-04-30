#include <iostream>
#include <vector>

// int main(){
//     std::vector<int> v{1,2,3,4,5,6,7};
//     int size = v.size();
//     int step = 3;
//     int index = 0;
//     while(size > 1){
//         index = (index + step - 1)%size;
//         v.erase(v.begin() + index);
//         size--;
//         for(int i : v){
//             std::cout << i << " ";
//         }
//         std::cout << std::endl;
//     }
//     std::cout << v[0] << std::endl;
// }

int main(){
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    int step = 3;
    int index = 0;
    while(size > 1){
        index = (index + step - 1)%size;
        for(int i = index; i < size - 1; i++){
            arr[i] = arr[i + 1];
        }
        size--;
        for(int i = 0; i < size; i++){
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << arr[0] << std::endl;
}