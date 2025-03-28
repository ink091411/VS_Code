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
    LNode *p=L;                 //ָ��pָ��ǰɨ�赽�Ľ�㣬��ֵָ��ͷ��㡣
    int j=0;                    //��ǰpָ��ڼ�����㣬��ֵΪ0����ͷ�ڵ㣩��
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