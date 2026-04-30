#include <iostream>

class ListNode{
    int val;
    ListNode* next;
    public:
        bool isEmpty(){
            return this->next == nullptr;
        }
        ListNode(int x) : val(x), next(nullptr) {}
        void print(){
            ListNode* current = this->next;
            while(current != nullptr){
                std::cout << current->val << " ";
                current = current->next;
            }
            std::cout << std::endl;
        }
        friend ListNode* insertNode(ListNode* head, int index, int value);
        friend ListNode* popNode(ListNode* head, int index);
};
ListNode* insertNode(ListNode* head, int index, int value){
    ListNode* newNode = new ListNode(value);
    if(index == 0){
        newNode->next = head->next;
        head->next = newNode;
        return head;
    }
    ListNode* current = head->next;
    for(int i = 0; i < index - 1; i++){
        if(current == nullptr || current->next == nullptr){
            break;
        }
        current = current->next;
    }
    if(current == nullptr){
        return head;
    }
    newNode->next = current->next;
    current->next = newNode;
    return head;
}
ListNode* popNode(ListNode* head, int index){
    if(head->isEmpty()) return head;
    if(index == 0){
        ListNode* temp = head->next;
        head->next = head->next->next;
        delete temp;
        return head;
    }
    ListNode* current = head->next;
    for(int i = 0; i < index - 1; i++){
        if(current == nullptr || current->next == nullptr){
            return head;
        }
        current = current->next;
    }
    if(current == nullptr || current->next == nullptr){
        return head;
    }
    ListNode* temp = current->next;
    current->next = current->next->next;
    delete temp;
    return head;
}

class Stack{
    ListNode* head = new ListNode(NULL);
    public:
        Stack(int x){
            insertNode(this->head, 0, x);
        }
        void push(int x){
            insertNode(this->head, 0, x);
        }
        void pop(){
            popNode(this->head, 0);
        }
        void print(){
            if(this->head->isEmpty()){
                std::cout << "stack is empty" << std::endl;
                return;
            }
            this->head->print();
        }
};

int main(){
    Stack s(1);
    s.push(2);
    s.push(3);
    s.print();
    s.pop();
    s.pop();
    s.print();
    s.pop();
    s.pop();
    s.print();
    return 0;
}