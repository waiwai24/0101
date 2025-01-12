# IDA

## 1.反汇编视图 IDA View-A

* 是主要的数据视图，有两种不同的形式：
  * 图形视图（默认）
  * 列表视图（使用`space`键切换） 
* 图形视图：将一个函数分解成了许多基本块
  * 绿色箭头：分支yes
  * 红色箭头：分支no
  * 蓝色箭头：执行下一个基本块，顺序执行
  * `ctrl+鼠标滚轮`：调整图形大小
* 列表视图：
  * 左边的窗口箭头：
    * 实线：非条件跳转
    * 虚线：条件跳转
    * 粗线（实/虚）：逆向流程（循环）
* 可创建其他的反汇编窗口帮助分析



## 2.桌面使用技巧

* View->Open Subviews 恢复无意关闭的数据窗口
* Window->Reset Desktop 将桌面恢复原始布局
* Windows->Save Desktop 保存桌面布局
* Windows->Load Desktop 打开之前保存的一个桌面布局



## 3.假名字

- sub_ 指令和子函数起点
- locret_ 返回指令 
- loc_ 指令
- off_ 数据，包含偏移量
- seg_ 数据，包含段地址值
- asc_ 数据，ASCII字符串
- byte_ 数据，字节（或字节数组）
- word_ 数据，16位数据（或字数组）
- dword_ 数据，32位数据（或双字数组）
- qword_ 数据，64位数据（或4字数组）
- flt_ 浮点数据，32位（或浮点数组）
- dbl_ 浮点数，64位（或双精度数组）
- tbyte_ 浮点数，80位（或扩展精度浮点数）
- stru_ 结构体(或结构体数组)
- algn_ 对齐指示
- unk_ 未处理字节

- LOWORD()得到一个32bit数的低16bit 
- HIWORD()得到一个32bit数的高16bit
- LOBYTE()得到一个16bit数最低（最右边）那个字节
- HIBYTE()得到一个16bit数最高（最左边）那个字节



## 4.交叉引用

两种基本的交叉引用xref：

* 代码交叉引用
* 数据交叉引用

![image-20240822194232980](.img/IDA.assets/image-20240822194232980.png)

* CODE XREF：代码交叉引用
* main+CB：交叉引用的源地址
* ↓p：引用位置的相对方向

### 4.1 代码交叉引用

代码交叉引用用于一条指令将控制权转交给另一条指令，在IDA里也称之为流（flow），同时又分为三种基本的流：

* 普通流：是一种最简单的流，表示从一条指令到另一条指令的顺序流，这是默认的执行流，没有特殊的显示标志
* 跳转流：每个无条件分支指令和条件分支指令，后缀`j` (jump)
* 调用流：call指令,由函数调用导致的交叉引用用后缀`p` (procedure)

### 4.2 数据交叉引用

数据交叉引用用于跟踪二进制文件访问数据的方式

* 读取交叉引用：访问的是某个内存位置的内容，后缀`r`
* 写入交叉引用：指出了修改变量内容的位置，后缀`w`
* 偏移量交叉引用：引用某个位置的地址，后缀`o`



## 5.快捷键

* `space`：在IDA View窗口切换视图
* `shift+F2`：脚本
* `Shift+E`：提取数据
* `F5`：汇编代码转成C代码
* `/`，`;`：添加注释
* `Ctrl+W`：保存数据库
* `Ctrl+Shift+W`：唤起IDB快照窗口
* `Ctrl+Shift+T`：唤出IDB快照弹窗

search:

* `shift+F12`：打开string窗口
* `ALT+T`：子字符串搜索，`CTRL+T`可匹配下一个
* `ALT+B`：二进制搜索（十六进制应每两位一个空格），`CTRL+B`可匹配下一个

jump：

* `G`：跳转到指定虚拟地址
* `Esc`：在IDA View窗口相当于后退，其他窗口相当于关闭窗口
* `CTRL+L`：名字选择器
* `CTRL+P`：函数选择器
* `CTRL+S`：段选择器
* `x`：查看某个变量或函数的交叉引用
* `Alt+M`：标记
* `CTRL+M`：跳转到标记

edit:

* `C`：将数据转化为指令

* `D`：将指令转化为数据

* `N`：更改某个变量或函数的名称g

* `R`：将选中的数字转换为相应的 ASCII 字符




## 6.idapython

| function                                                     | Code                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 获取IDA界面地址                                              |                                                              |
| 取当前地址                                                   | idc.here() 或 idc.get_screen_ea()                            |
| 获取最小地址（可以使用的）                                   | ida_ida.inf_get_min_ea()                                     |
| 获取最大地址（可以使用的）                                   | ida_ida.inf_get_max_ea()                                     |
| 获取所选范围的起始地址                                       | idc.read_selection_start()                                   |
| 获取所选范围的结束地址                                       | idc.read_selection_end()                                     |
|                                                              |                                                              |
| **获取地址的数值**                                           |                                                              |
| **以1字节为单位获取地址处的值**                              | idc.get_wide_byte(addr)                                      |
| **以2字节(字)的单位获取**                                    | idc.get_wide_word(addr)                                      |
| **以4字节的单位获取**                                        | idc.get_wide_dword(addr)                                     |
| 以8字节的单位获取                                            | idc.get_qword(addr)                                          |
| 判断是否是字节                                               | ida_bytes.is_byte                                            |
| **得到运行断点之前的寄存器的值**                             | ea=get_reg_value("eax")                                      |
|                                                              |                                                              |
|                                                              |                                                              |
| **修改指令数值**                                             |                                                              |
| **修改addr地址的值为value.每次修改1个字节**                  | ida_bytes.patch_byte(addr,value)                             |
| **每次修改2个字节**                                          | ida_bytes.patch_word(addr,value)                             |
| **每次修改4个字节**                                          | ida_bytes.patch_Dword(addr,value)                            |
| 每次修改8个字节                                              | ida_bytes.patch_Qword(addr,value)                            |
| **修改寄存器的值**                                           | set_reg_value(value, "eip")                                  |
|                                                              |                                                              |
| 汇编指令操作                                                 |                                                              |
| 获取地址处的汇编语句                                         | idc.GetDisasm(addr) 或 idc.generate_disasm_line(addr,flags)  |
| 获取指定地址位置的操作数.参数1是地址.参数2是操作数索引.如 mov ebp,esp中： 操作数1是ebp ，操作数2是esp mov则是汇编指令不是操作数 | idc.print_operand(addr,index)                                |
| 获取汇编操作指令（如mov、add）                               | idc.print_insn_mnem(addr)                                    |
|                                                              |                                                              |
| 段操作                                                       |                                                              |
| 获取段的名字（参数为当前的地址）                             | idc.get_segm_name(addr)                                      |
| 获取段的开始地址                                             | idc.get_segm_start(addr)                                     |
| 获取段的结束地址                                             | idc.get_segm_end(addr)                                       |
| 获取第一个段                                                 | idc.get_first_seg(addr)                                      |
| 获取下一个段                                                 | idc.get_next_seg(addr)                                       |
| 返回一个列表记录所有段的地址                                 | idautil.Segments()                                           |
|                                                              |                                                              |
| 函数操作                                                     |                                                              |
| 获取指定地址之间的所有函数                                   | idautils.Functions(startaddr,endaddr)                        |
| 获取指定地址的函数名                                         | idc.get_func_name(addr)                                      |
| 获取函数的注释                                               | get_func_cmt(addr, repeatable) repeatable:0/1 0是获取常规注释 1是获取重复注释 |
| 设置函数注释                                                 | idc.set_func_cmt(ea, cmt, repeatable)                        |
| 弹出框框要求用户进行选择 参数则是信息                        | idc.choose_func(title)                                       |
| 返回: addr 距离函数的偏移形式                                | idc.get_func_off_str(addr)                                   |
| 寻找函数结尾,如果函数存在则返回结尾地址,否则返回BADADDR      | idc.find_func_end(addr)                                      |
| 设置函数结尾                                                 | ida_funcs.set_func_end(ea, newend) newend:新的结束地址       |
| 设置函数开头                                                 | ida_funcs.set_func_start(addr, newstart)                     |
| 设置地址处的名字                                             | idc.set_name(ea, name, SN_CHECK) Ex函数也使用set_name        |
| 获取首个函数                                                 | idc.get_prev_func(ea)                                        |
| 获取下一个函数                                               | idc.get_next_func(ea)                                        |
|                                                              |                                                              |
| 数据查询                                                     |                                                              |
| 查找二进制找到返回地址没找到返回-1(BADADDR)                  | idc.find_binary(ea, flag, searchstr, radix=16, from_bc695=False) |
| 从ea开始寻找下一个数据地址                                   | ida_search.find_data(ea, sflag)                              |
| 从ea开始寻找下一个代码地址                                   | ida_search.find_code(ea, sflag)                              |
| 光标跳转到ea位置（不是eip！！！）                            | ida_kernwin.jumpto(ea)                                       |
|                                                              |                                                              |
| 数据校验                                                     |                                                              |
| 获取标志                                                     | ida_bytes.get_full_flags(ea)                                 |
| 判断是否为代码                                               | ida_bytes.is_code(f) f即标志                                 |
| 判断是否为数据                                               | ida_bytes.is_data(f)                                         |
|                                                              |                                                              |
| 交叉引用                                                     |                                                              |
| 获取地址处引用位置 A调用B 对B函数地址使用此函数则找到A调用 返回列表.遍历列表则可以找出所有引用位置. 参数1是ea也就是地址,参数2告诉IDA是否跟踪这些代码. | idautils.CodeRefsTo(ea, flow)                                |
| 返回ea的代码引用了何处的代码. 返回一个列表                   | idautils.CodeRefsFrom(ea, flow)                              |
| 返回一个列表告诉ea位置的数据被谁引用了                       | idautils.DataRefsTo(ea)                                      |
| 告诉我们ea引用了谁.                                          | idautils.DataRefsFrom(ea)                                    |
|                                                              |                                                              |
| **动调脚本化**                                               |                                                              |
| **在指定的地址设置断点**                                     | AddBpt(long Address)                                         |
| **获取一个寄存器的名称**                                     | GetRegValue(string Register)                                 |
| **设置寄存器的值**                                           | SetRegValue(long Value, string Register)                     |
| **运行到指定的地址，然后停下**                               | RunTo(long Address)                                          |
| **解决python 脚本和调试器执行流异步执行**（就是说idapython和断点会在汇编执行前执行，这段代码让它在汇编执行后再执行idapython） | idaapi.step_into() GetDebuggerEvent(WFNE_SUSP, -1)           |
| **获取栈内数据**（这样，运行到某个位置，获取esp/rsp的值，为栈顶，通过偏移可以获取相对应的栈内地址，然后使用`Byte()`/ `Dword()`来获取相关数据） | RunTo(xxx) GetDebuggerEvent(WFNE_SUSP, -1) stack = GetRegValue("esp") |