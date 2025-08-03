```c
int main (void) { body } 		
int main (int argc, char *argv[]) { body } //在程序启动的时候，就携带参数给他
```

argc和argv是通过命令行窗口传给程序的

* argc：非负值，表示程序运行的环境传递给程序的参数个数
* argv：argc个参数，其中第0个参数是程序的全名，以后的参数是命令行后面跟的用户输入的参数，argv[argc]为NULL



```c++
#include<iostream>
using namespace std;
int  main(int  argc,  char*  argv[]) 
  { 
  int  i; 
  for  (i  =  0;  i<argc;  i++) cout<<argv[i]<<endl; 
  return  0; 
  } 
```

```cmd
$input：
./a.out 123 56
$output：
./a.out
123
56
```

