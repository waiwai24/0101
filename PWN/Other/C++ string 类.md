# C++ string 类

## 1.头文件

```c++
#include <iostream>
#include <string>
```

在 C++ 中，字符串是由字符组成的序列。`<string>` 头文件提供了 `std::string` 类，它是对 C 风格字符串的封装，提供了更安全、更易用的字符串操作功能

string与char*的区别：

- **`char*`** 是一个指针
- **`string`**本质上是一个类，类的内部封装了**`char*`**，即**`string`**是一个**`char*`**型的容器
- **`string`**管理**`char*`**所分配的内存，不用担心复制越界和取值越界等



## 2.基本语法

- 声明字符串变量：

  ```
  std::string str;
  ```

- 初始化字符串：

  ```
  std::string str = "Hello, World!";
  ```

- 使用 `+` 连接字符串



## 3.常用成员函数

`std::string` 类提供了许多成员函数来操作字符串，以下是一些常用的成员函数：

  | 函数名                | 描述                                           | 示例代码                                       |
  | --------------------- | ---------------------------------------------- | ---------------------------------------------- |
  | `size()`              | 返回字符串的长度（字符数）。                   | `std::cout << str.size();`                     |
  | `length()`            | 与 `size()` 相同，返回字符串的长度。           | `std::cout << str.length();`                   |
  | `empty()`             | 判断字符串是否为空。                           | `std::cout << (str.empty() ? "Yes" : "No");`   |
  | `operator[]`          | 访问字符串中指定位置的字符。                   | `std::cout << str[0];`                         |
  | `at()`                | 访问字符串中指定位置的字符（带边界检查）。     | `std::cout << str.at(0);`                      |
  | `substr()`            | 返回从指定位置开始的子字符串。                 | `std::string sub = str.substr(0, 5);`          |
  | `find()`              | 查找子字符串在字符串中的位置。                 | `std::cout << str.find("sub") << std::endl;`   |
  | `rfind()`             | 从字符串末尾开始查找子字符串的位置。           | `std::cout << str.rfind("sub") << std::endl;`  |
  | `replace()`           | 替换字符串中的部分内容。                       | `str.replace(pos, length, "new_substring");`   |
  | `append()`            | 在字符串末尾添加内容。                         | `str.append(" more");`                         |
  | `insert()`            | 在指定位置插入内容。                           | `str.insert(pos, "inserted");`                 |
  | `erase()`             | 删除指定位置的字符或子字符串。                 | `str.erase(pos, length);`                      |
  | `clear()`             | 清空字符串。                                   | `str.clear();`                                 |
  | `c_str()`             | 返回 C 风格的字符串（以 null 结尾）。          | `const char* cstr = str.c_str();`              |
  | `data()`              | 返回指向字符数据的指针（C++11 及之后的版本）。 | `const char* data = str.data();`               |
  | `compare()`           | 比较两个字符串。                               | `int result = str.compare("other");`           |
  | `find_first_of()`     | 查找第一个匹配任意字符的位置。                 | `size_t pos = str.find_first_of("aeiou");`     |
  | `find_last_of()`      | 查找最后一个匹配任意字符的位置。               | `size_t pos = str.find_last_of("aeiou");`      |
  | `find_first_not_of()` | 查找第一个不匹配任意字符的位置。               | `size_t pos = str.find_first_not_of("aeiou");` |
  | `find_last_not_of()`  | 查找最后一个不匹配任意字符的位置。             | `size_t pos = str.find_last_not_of("aeiou");`  |