# C++ allocator 类

## 1.介绍

```c++
#include <memory>
```

allocator是STL的重要组成，隐藏在所有容器（包括vector）身后，默默完成内存配置与释放，对象构造和析构的工作

![image-20250217112058010](.img/C++ allocator 类.assets/image-20250217112058010.png)

allocator 类主要与内存分配和对象的构造有关，它分配的内存是：

* **原始的**：未初始化的，也意味着分配的内存只是简单地分配了一块“原始”的内存空间，而没有对内存中的内容进行任何初始化操作
* **未构造的**：分配配的内存并未调用任何对象的构造函数。虽然分配的内存可以容纳对象，但此时内存块本身并没有被初始化为对象的状态。它只是一个未使用的“存储块”。若要在分配的内存中创建对象，必须通过显式地调用对象的构造函数来完成

分配和释放未构造的原始内存两种方法：

- allocator 类，提供可感知类型的内存分配
- 标准库中的 opeator new 和 operator delete

原始内存中构造和撤销对象的方法：

- allocator类定义了名为construct和destroy的成员
- placement new表达式，接受指向未构造内存的指针
- 直接调用对象的析构函数来撤销对象
- 算法uninitialized_fill 和 uninitialized_copy，在目的地构造对象

简单示例：

```c++
#include <iostream>
#include <memory> // allocator 和 placement new 头文件

int main() {
    // 创建一个 allocator 对象，用于分配 int 类型的内存
    std::allocator<int> alloc;
    // 分配一个 int 类型的内存块，此时内存是原始的、未构造的
    int* ptr = alloc.allocate(1);
    // 使用 placement new 在分配的内存中构造一个对象
    new (ptr) int(10);
    // 访问已构造的值
    std::cout << "Value: " << *ptr << std::endl;
    // 调用析构函数
    ptr->~int();
    // 释放分配的内存
    alloc.deallocate(ptr, 1);

    return 0;
}
```



## 2.支持的操作

| allocator<T> a       | 定义了一个名为 a 的 allocator 对象，它可以为类型为 T 的对象分配内存 |
| -------------------- | ------------------------------------------------------------ |
| a.allocate(n)        | 分配一段原始的、未构造的内存，保存 n 个类型为 T 的对象       |
| a.deallocate(p, n)   | 释放从 T* 指针 p 中地址开始的内存，这块内存保存了 n 个类型为 T 的对象；p 必须是一个先前由 allocate 返回的指针，且 n 必须是 p 创建时所要求的大小。在调用 deallocate 之前，用户必须对每个在这块内存中创建的对象调用 destroy |
| a.construct(p, args) | p 必须是一个类型为 T* 的指针，指向一块原始内存；arg 被传递给类型为 T 的构造函数，用来在 p 指向的内存中构造一个对象 |
| a.destroy(p)         | p 为 T* 类型的指针，此算法对 p 指向的对象执行析构函数        |

| uninitialized_copy(b, e, b2)   | 从迭代器 b 和 e 指出的输入范围中拷贝元素到迭代器 b2 指定的未构造的原始内存中。b2 指向的内存必须足够大，能容纳输入序列中元素的拷贝 |
| ------------------------------ | ------------------------------------------------------------ |
| uninitialized_copy_n(b, n, b2) | 从迭代器 b 指向的元素开始，拷贝 n 个元素到 b2 开始的内存中   |
| uninitialized_fill(b, e, t)    | 在迭代器 b 和 e 指定的原始内存范围中创建对象，对象的值均为 t 的拷贝 |
| uninitialized_fill_n(b, n, t)  | 从迭代器 b 指向的内存地址开始创建 n 个对象。b 必须指向足够大的未构造的原始内存，能够容纳给定数量的对象 |
