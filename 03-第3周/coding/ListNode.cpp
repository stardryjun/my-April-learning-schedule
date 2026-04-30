#include <iostream>

class ListNode{
    public:
        int val;
        ListNode* next;
        ListNode(int x) : val(x), next(nullptr) {}
        void print(){
            ListNode* current = this;
            while(current != nullptr){
                std::cout << current->val << " ";
                current = current->next;
            }
            std::cout << std::endl;
        }
};

ListNode* insertNode(ListNode* head, int index, int value){
    if(index == 0){
        ListNode* newNode = new ListNode(value);
        newNode->next = head;
        return newNode;
    }
    ListNode* current = head;
    for(int i = 0; i < index - 1; i++){
        if(current == nullptr || current->next == nullptr){
            break;
        }
        current = current->next;
    }
    ListNode* newNode = new ListNode(value);
    if(current == nullptr){
        return newNode;
    }
    newNode->next = current->next;
    current->next = newNode;
    return head;
}

ListNode* popNode(ListNode* head, int index){
    if(head == nullptr) return head;
    if(index == 0){
        ListNode* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    ListNode* current = head;
    for(int i = 0; i < index - 1; i++){
        if(current->next == nullptr){
            return head;
        }
        current = current->next;
    }
    if(current->next == nullptr){
        return head;
    }
    ListNode* temp = current->next;
    current->next = current->next->next;
    delete temp;
    return head;
}

int main(){
    ListNode* head = new ListNode(0);
    head = insertNode(head, 0, 10); // Insert 10 at index 0
    head = insertNode(head, 1, 20); // Insert 20 at index 1
    head = insertNode(head, 2, 30); // Insert 30 at index 2
    head->print(); // Print the linked list
    head = popNode(head, 1); // Remove the node at index 1 (which has value 20)
    head->print(); // Print the linked list

    // free remaining nodes
    while(head){
        ListNode* tmp = head;
        head = head->next;
        delete tmp;
    }
    return 0;
}
