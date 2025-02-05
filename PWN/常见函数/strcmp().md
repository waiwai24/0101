# strcmp()

```c
int strcmp(const char *str1, const char *str2)
```

* 头文件：<stdio.h>
* 参数：str1 -- 要进行比较的第一个字符串。str2 -- 要进行比较的第二个字符串。
* 返回值：
  * 如果返回值小于 0，则表示 str1 小于 str2。
  * 如果返回值大于 0，则表示 str1 大于 str2。
  * 如果返回值等于 0，则表示 str1 等于 str2。
* strcmp是根据\x00截断



源码：

```c
int
strcmp (const char *p1, const char *p2)
{
  const unsigned char *s1 = (const unsigned char *) p1;
  const unsigned char *s2 = (const unsigned char *) p2;
  unsigned char c1, c2;

  do
    {
      c1 = (unsigned char) *s1++;
      c2 = (unsigned char) *s2++;
      if (c1 == '\0') return c1 - c2;
    }
  while (c1 == c2);

  return c1 - c2;
}
```

