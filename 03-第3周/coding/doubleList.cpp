#include <iostream>

class DoubleListNode{
    public:
        int val;
        DoubleListNode* prev;
        DoubleListNode* next;
        DoubleListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
        void printNode(){
            DoubleListNode* temp = this;
            while(temp != nullptr){
                std::cout << temp->val << " ";
                temp = temp->next;
            }
        }
};

DoubleListNode* insertList(DoubleListNode* head, int x, int index){
    DoubleListNode* newNode = new DoubleListNode(x);
    if(index == 0){
        head->prev = newNode;
        newNode->next = head;
        head = newNode;
        return head;
    }
    DoubleListNode* temp = head;
    for(int i = 0; i < index - 1; i++){
        if(temp == nullptr){
            std::cout << "index out of range" << std::endl;
            return head;
        }
        temp = temp->next;
    }
    if(temp->next){
        newNode->next = temp->next;
        temp->next->prev = newNode;
    }
    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

DoubleListNode* popList(DoubleListNode* head, int index){
    if(head == nullptr) return head;
    if(index == 0){
        DoubleListNode* temp = head;
        head = head->next;
        if(head) head->prev = nullptr;
        delete temp;
        return head;
    }
    DoubleListNode* temp = head;
    for(int i = 0; i < index; i++){
        if(temp == nullptr){
            std::cout << "index out of range" << std::endl;
            return head;
        }
        temp = temp->next;
    }
    if(temp == nullptr) return head;
    if(temp->prev) temp->prev->next = temp->next;
    if(temp->next) temp->next->prev = temp->prev;
    delete temp;
    return head;
}

int main(){
    DoubleListNode* doubleList = new DoubleListNode(0);
    doubleList = insertList(doubleList,1,0);
    doubleList = insertList(doubleList,2,1);
    doubleList = insertList(doubleList,3,2);
    doubleList->printNode();
    std::cout << std::endl;
    doubleList = popList(doubleList,1);
    doubleList = popList(doubleList,0);
    doubleList->printNode();
    return 0;
}
