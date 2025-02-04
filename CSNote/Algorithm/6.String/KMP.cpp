#include <iostream>
#include <cstring>
using namespace std;

void GetNext(int* next, char* str)
{
    // 初始化
    int j = -1;
    next[0] = -1;
    for(int i = 1 ;i < strlen(str) ; i++)//注意i从1开始
    {
        while(j >= 0 && str[i] != str[j + 1])//前后缀不相同时
        {
            j = next[j];//向前回退
        }
        if (str[i] == str[j + 1])//前后缀相同时
        {
            j++;
            next[i] = j;//将前缀的长度赋给next[i]
        }
    }
}

int KMP(char* text, char* pattern)
{
    //定义两个下标j 指向P模式串起始位置，i指向T文本串起始位置
    int i,j,* next=(int*) malloc(sizeof(int)*strlen(pattern));
    GetNext(next,pattern);
    i = j = 0;
    while(i < strlen(text) && j < strlen(pattern))
    {
        if(text[i] == pattern[j])
        {
            i++;
            j++;
        }
        else if(next[j] >= 0)
        {
            j = next[j];
        }
        else
        {
            j=0;
            i++;
        }
    }
    if(j >= strlen(pattern))
    {
        return i-strlen(pattern);
    }
    else
    {
        return -1;
    }
}

int main()
{
    char text[] = "aabaabaafa";
    char pattern[] = "abaafa";
    cout << KMP(text,pattern) << endl;
    return 0;
}
