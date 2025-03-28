#include<stdlib.h>

typedef int ElemType;

typedef struct LNode{
    ElemType data;
    struct LNode *next;
}LNode,*Linklist;

bool InitList(Linklist &L){
    L=(LNode *)malloc(sizeof(LNode));
    if(L=NULL){
        return false;
    }
    L->next=NULL;
    return true;
}

bool ListInsert(Linklist &L,int i,ElemType e){
    if(i<1){
        return false;
    }
    LNode *p=L;                 //指针p指向当前扫描到的结点，初值指向头结点。
    int j=0;                    //当前p指向第几个结点，初值为0（即头节点）。
    while(p!=NULL&&j<i-1){
        p=p->next;
        j++;
    }
    if(p==NULL){
        return false;
    }
    LNode *s=(LNode *)malloc(sizeof(LNode));
    s->data=e;
    s->next=p->next;
    p->next=s;
    return true;

}