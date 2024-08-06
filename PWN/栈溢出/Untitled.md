    保存被调用函数的返回值到 eax 寄存器中 mov eax, xxx
    恢复 esp 同时回收局部变量空间 mov ebp, esp
    将上一个栈帧底部位置恢复到 ebp pop ebp
    弹出当前栈顶元素,从栈中取到返回地址,并跳转到该位置 ret