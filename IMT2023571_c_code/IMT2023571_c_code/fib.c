#include<stdio.h>
int main(){
    int n=15;
    int a=0;
    int b=1;
    int i=2;
    int ans=0;
    if(n==0){
        printf("%d\n",a);
    }
    else if(n==1){
        printf("%d\n",b);
    }
    else{
        while(i<n+1){
            ans=a+b;
            a=b;
            b=ans;
            i++;
        }
        printf("%d\n",ans);
    }
    
    return 0;
}