#include <stdlib.h>
#include <stdio.h>
#define InitSize 10

typedef struct{
    int *data;
    int MaxSize;
    int length;
}SeqList;

void InitList(SeqList &L);
void IncreaseSize(SeqList &L,int len);
bool ListInsert(SeqList &L,int i,int e);
bool ListDelete(SeqList &L,int i,int &e);
int GetElem(SeqList L,int i);
int LocateElem(SeqList L,int e);
void show(SeqList L);

int main(){
    SeqList L;
    InitList(L);
    show(L);

    L.data[0]=1;
    L.data[1]=2;
    L.data[2]=3;
    L.data[3]=4;
    L.data[4]=5;
    L.length=5;
    show(L);

    IncreaseSize(L,5);
    show(L);

    ListInsert(L,6,6);
    show(L);

    int e=0;
    ListDelete(L,6,e);
    printf("被删除的数据值为：%d\n",e);
    show(L);

    printf("%d\n",GetElem(L,3));
    printf("%d\n",LocateElem(L,5));

    return 0;
}

void InitList(SeqList &L){
    L.data=(int *)malloc(InitSize*sizeof(int));
    L.MaxSize=InitSize;
    L.length=0;
}

void IncreaseSize(SeqList &L,int len){
    int *p=L.data;
    L.data=(int *)malloc((L.MaxSize+len)*sizeof(int));
    for(int i=0;i<L.length;i++){
        L.data[i]=p[i];
    }
    L.MaxSize+=len;
    free(p);
}

bool ListInsert(SeqList &L,int i,int e){
    if((i<1||i>L.length+1)||(L.length>=L.MaxSize)){
        return false;
    }
    for(int j=L.length;j>=i;j--){
        L.data[j]=L.data[j-1];
    }
    L.data[i-1]=e;
    L.length++;
    return true;
}

bool ListDelete(SeqList &L,int i,int &e){
    if(i<1||i>L.length){
        return false;
    }
    e=L.data[i-1];
    for(int j=i;j<L.length;j++){
        L.data[j-1]=L.data[j];
    }
    L.length--;
    return true;
}

int GetElem(SeqList L,int i){
    return L.data[i-1];
}

int LocateElem(SeqList L,int e){
    for(int i=0;i<L.length;i++){
        if(L.data[i]==e){
            return i+1;
        }
    }
    return 0;
}

void show(SeqList L){
    printf("该顺序表全长为：%d\n数据长度为：%d\n数据内容如下：\n",L.MaxSize,L.length);
    for(int i=0;i<L.length;i++){
        printf("%d ",L.data[i]);
    }
    printf("\n");
    printf("\n");
}