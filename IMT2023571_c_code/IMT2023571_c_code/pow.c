#include<stdio.h>
int main(){
    int x=2;
    int y=0;
    int ans=1;
    if(y==0){
        printf("%d\n",1);
    }
    else{
    while(y){
        ans=ans*x;
        y--;
    }
    printf("%d\n",ans);
    }
    return 0;
}