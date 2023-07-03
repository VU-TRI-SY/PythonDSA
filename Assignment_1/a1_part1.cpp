#include <bits/stdc++.h>
using namespace std;
struct SetList{
    //contians a double linked list
    Node* head;
    Node* tail;
};

struct Node{
    int val;
    Node* next;
    Node* prev;
    SetList* setRef;

    Node(int data, SetList* setR){
        //created Node will be added to the passed SetList
        val = data;
        next = nullptr;
        prev = nullptr;
        setRef = setR;
    }
};