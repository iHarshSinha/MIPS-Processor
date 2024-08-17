#include<stdio.h>
int main(){
    int n=7;
    int ans=1;
    if(n==0){
        printf("%d\n",1);
    }
    else if(n==1){
        printf("%d\n",1);
    }
    else{
        while(n>1){
            ans=ans*n;
            n--;
        }
        printf("%d\n",ans);
    }
    
    return 0;
}