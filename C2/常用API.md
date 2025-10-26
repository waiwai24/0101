# 常用 API

## 1.LoadLibraryA

LoadLibraryA：将指定的模块加载到调用进程的地址空间中

```c
HMODULE LoadLibraryA(
  [in] LPCSTR lpLibFileName
);
```



## 2.VirtualAlloc

VirtualAlloc：在调用进程的虚拟地址空间中预留、提交或更改页面区域的状态。分配的内存会自动初始化为零

- flAllocationType:
  - MEM_COMMIT：从保留的内存中分配实际内存，但实际物理内存只有在实际访问虚拟地址时才会分配
  - MEM_RESERVE：不分配实际的物理存储，仅保留进程的虚拟地址空间范围
  - MEM_RESET：清除内存
- flProtect：
  - PAGE_EXECUTE：允许执行代码
  - PAGE_EXECUTE_READ：允许执行代码并读取数据
  - PAGE_EXECUTE_READWRITE：允许执行代码、读取和写入数据
  - PAGE_EXECUTE_WRITECOPY：允许执行代码、写入数据并复制
  - PAGE_NOACCESS：禁止访问
  - PAGE_READONLY：允许读取

```c
LPVOID VirtualAlloc(
  [in, optional] LPVOID lpAddress,          // 要分配的区域的起始地址
  [in]           SIZE_T dwSize,             // 要分配的区域的大小，以字节为单位
  [in]           DWORD  flAllocationType,   // 内存分配类型
  [in]           DWORD  flProtect           // 要分配的页区域的内存保护
);
```



## 3.VirtualProtect

VirtualProtect：更改调用进程的虚拟地址空间中某一区域已提交页面的保护级别

```c
BOOL VirtualProtect(
  [in]  LPVOID lpAddress,       // 要更改其访问保护的内存区域的基地址
  [in]  SIZE_T dwSize,          // 要更改其访问保护属性的区域大小（以字节为单位）
  [in]  DWORD  flNewProtect,    // 新的内存保护选项
  [out] PDWORD lpflOldProtect   // 指向接收 `lpAddress` 之前访问保护值的 `DWORD` 变量
);
```



## 4.CreateThread

CreateThread：在调用进程的虚拟空间中创建线程

```c
HANDLE CreateThread(
  [in, optional]  LPSECURITY_ATTRIBUTES   lpThreadAttributes,    // 设置为 NULL - 可选
  [in]            SIZE_T                  dwStackSize,           // 设置为 0 - 默认
  [in]            LPTHREAD_START_ROUTINE  lpStartAddress,        // 指向线程要执行的函数
  [in, optional]  __drv_aliasesMem LPVOID lpParameter,           // 指向要传递给执行函数的变量（设置为 NULL - 可选）
  [in]            DWORD                   dwCreationFlags,       // 设置为 0 - 默认
  [out, optional] LPDWORD                 lpThreadId             // 指向接收线程 ID 的“DWORD”变量（设置为 NULL - 可选）   
);
```



## 5.VirtualFree

VirtualFree：在调用进程的虚拟地址空间内释放、解分配或同时释放和解分配一个页面区域

dwFreeType：

- MEM_DECOMMIT：释放物理内存，而不释放与之链接的虚拟地址空间。因此，仍可以使用虚拟地址空间在将来分配内存，但与之链接的页面不再受物理内存支持
- MEM_RELEASE：同时释放与已分配虚拟内存关联的虚拟地址空间和物理内存。如果使用此标志，则 dwSize 参数必须为 0

```c
BOOL VirtualFree(
  [in] LPVOID lpAddress,  // 要释放的页面区域的基本地址
  [in] SIZE_T dwSize,     // 要释放的内存区域的大小
  [in] DWORD  dwFreeType  // 释放操作类型
);
```



## 6.LocalAlloc

LocalAlloc：从堆中分配指定的字节数，如果函数成功，则返回值是新分配的内存对象的句柄；失败，则返回值为 NULL

```c
DECLSPEC_ALLOCATOR HLOCAL LocalAlloc(
  [in] UINT   uFlags,  // 通常为 LPTR
  [in] SIZE_T uBytes   // 分配字节数
);
```



## 7.LocalFree

LocalFree：释放指定的本地内存对象并使其句柄失效

```c
HLOCAL LocalFree(
  [in] _Frees_ptr_opt_ HLOCAL hMem
);
```



## 8.CreateToolhelp32Snapshot

CreateToolhelp32Snapshot：拍摄指定进程以及这些进程使用的堆、模块和线程的快照

- dwFlags：
  - TH32CS_SNAPALL：包括系统中的所有进程和线程，以及th32ProcessID中指定的进程的堆和模块
  - TH32CS_SNAPPROCESS：快照中包含系统中的所有进程

```c
HANDLE CreateToolhelp32Snapshot(
  [in] DWORD dwFlags,
  [in] DWORD th32ProcessID
);
```



## 9.Process32First

Process32First：获取系统中遇到的第一个进程的信息

如果进程列表的第一个条目已复制到缓冲区，则返回 TRUE，否则返回 FALSE。如果没有进程存在或快照不包含进程信息，GetLastError 函数将返回 ERROR_NO_MORE_FILES 错误值

```c
BOOL Process32First(
  [in]      HANDLE           hSnapshot, // 调用 CreateToolhelp32Snapshot 函数返回的快照句柄
  [in, out] LPPROCESSENTRY32 lppe       // 指向 PROCESSENTRY32 结构的指针
);
```

tagPROCESSENTRY32 结构体：

```c
typedef struct tagPROCESSENTRY32 {
  DWORD     dwSize;                     // 该结构体的大小，以字节为单位。在调用 Process32First 函数之前，将此成员设置为 sizeof(PROCESSENTRY32) ；不初始化 dwSize，Process32First 会失败
  DWORD     cntUsage;
  DWORD     th32ProcessID;              // 进程 ID
  ULONG_PTR th32DefaultHeapID;
  DWORD     th32ModuleID;
  DWORD     cntThreads;
  DWORD     th32ParentProcessID;        // 父进程的进程 ID
  LONG      pcPriClassBase;
  DWORD     dwFlags;
  CHAR      szExeFile[MAX_PATH];        // 进程的可执行文件的名称
} PROCESSENTRY32;
```

Process32Next：获取系统快照中记录的下一个进程的信息

```c
BOOL Process32Next(
  [in]  HANDLE           hSnapshot,
  [out] LPPROCESSENTRY32 lppe
);
```



## 10.OpenProcess

OpenProcess：打开一个现有的本地进程对象

```c
HANDLE OpenProcess(
  [in] DWORD dwDesiredAccess,  // 对进程对象的访问权限
  [in] BOOL  bInheritHandle,   //  TRUE，则由该进程创建的进程将继承该句柄。否则，这些进程不会继承该句柄
  [in] DWORD dwProcessId       // 本地进程的标识符
);
```



## 11.VirtualAllocEx

VirtualAllocEx：在指定进程的虚拟地址空间中预留、提交或更改内存区域的状态

```c
LPVOID VirtualAllocEx(
  [in]           HANDLE hProcess,           // 进程的句柄
  [in, optional] LPVOID lpAddress,          // 要分配页面区域起始地址指针
  [in]           SIZE_T dwSize,             // 分配区域字节数
  [in]           DWORD  flAllocationType,   // 内存分配类型
  [in]           DWORD  flProtect           // 内存保护
);
```



## 12.WriteProcessMemory

WriteProcessMemory：将数据写入指定进程的内存区域，函数失败，返回值为0

```c
BOOL WriteProcessMemory(
  [in]  HANDLE  hProcess,                  // 要修改进程内存的句柄
  [in]  LPVOID  lpBaseAddress,             // 指向指定进程要写入数据的基地址指针
  [in]  LPCVOID lpBuffer,                  // 指向包含要写入数据的指针
  [in]  SIZE_T  nSize,                     // 写入字节数
  [out] SIZE_T  *lpNumberOfBytesWritten    // 可选，指向一个变量指针，接收写入指定进程的实际字节数
);
```



## 13.CreateRemoteThread

CreateRemoteThread：创建一个在另一个进程的虚拟地址空间中运行的线程。函数成功，返回值是新线程的句柄，否则返回值是 NULL

```c
HANDLE CreateRemoteThread(
  [in]  HANDLE                 hProcess,            // 要创建线程的进程的句柄
  [in]  LPSECURITY_ATTRIBUTES  lpThreadAttributes,  // 指向 SECURITY_ATTRIBUTES 的安全描述符指针
  [in]  SIZE_T                 dwStackSize,         // 线程堆栈初始大小
  [in]  LPTHREAD_START_ROUTINE lpStartAddress,      // 指向应用程序定义的函数的指针
  [in]  LPVOID                 lpParameter,         // 要传递给线程函数的变量的指针
  [in]  DWORD                  dwCreationFlags,     // 控制线程创建的标志
  [out] LPDWORD                lpThreadId           // 接收线程标识符的变量指针
);
```



## 14.InternetOpenW

InternetOpenW：初始化应用程序的 WinINet 函数的使用。由于主要用于代理相关事项，因此传递到 WinAPI 的所有参数均为 NULL。值得注意的是，将第二个参数设置为 NULL 等效于使用 INTERNET_OPEN_TYPE_PRECONFIG，它指定应使用系统当前配置来确定 Internet 连接的代理设置。

```c
HINTERNET InternetOpenW(
  [in] LPCWSTR lpszAgent,       // NULL
  [in] DWORD   dwAccessType,    // NULL 或 INTERNET_OPEN_TYPE_PRECONFIG
  [in] LPCWSTR lpszProxy,       // NULL
  [in] LPCWSTR lpszProxyBypass, // NULL
  [in] DWORD   dwFlags          // NULL
);
```



## 15.InternetOpenUrlW

InternetOpenUrlW：打开由完整的 FTP 或 HTTP URL 指定的资源，如果成功建立连接，则返回 URL 的有效句柄；如果连接失败返回 NULL

第五个参数使用 INTERNET_FLAG_HYPERLINK | INTERNET_FLAG_IGNORE_CERT_DATE_INVALID，以提高服务器端发生错误时 HTTP 请求的成功率

```c
HINTERNET InternetOpenUrlW(
  [in] HINTERNET hInternet,       // 由 InternetOpenW 打开的句柄
  [in] LPCWSTR   lpszUrl,         // Payload 的 URL
  [in] LPCWSTR   lpszHeaders,     // NULL
  [in] DWORD     dwHeadersLength, // NULL
  [in] DWORD     dwFlags,         // INTERNET_FLAG_HYPERLINK | INTERNET_FLAG_IGNORE_CERT_DATE_INVALID
  [in] DWORD_PTR dwContext        // NULL
);
```



## 16.InternetReadFile

InternetReadFile：从 InternetOpenUrl、FtpOpenFile 或 HttpOpenRequest 函数打开的句柄读取数据，调用此函数之前，必须分配一个缓冲区来保存有效负载

```c
BOOL InternetReadFile(
  [in]  HINTERNET hFile,                  // 由 InternetOpenUrlW 打开的句柄
  [out] LPVOID    lpBuffer,               // 存储有效负载的缓冲区
  [in]  DWORD     dwNumberOfBytesToRead,  // 要读取的字节数
  [out] LPDWORD   lpdwNumberOfBytesRead   // 指向接收已读取字节数的变量的指针
);
```



## 17.InternetCloseHandle

InternetCloseHandle：关闭单个 Internet 句柄

```c
BOOL InternetCloseHandle(
  [in] HINTERNET hInternet // 由 InternetOpenW 和 InternetOpenUrlW 打开的句柄
);
```



## 18.InternetSetOptionW

InternetSetOptionW：设置 Internet 选项

InternetCloseHandle WinAPI 不会关闭 HTTP/S 连接。进程会尝试重用连接，因此，即使句柄已关闭，连接仍然处于活动状态。使用 INTERNET_OPTION_SETTINGS_CHANGED 标志调用 InternetSetOptionW 将导致系统更新其 Internet 设置的缓存版本，从而导致 WinInet 保存的连接被关闭

```c
BOOL InternetSetOptionW(
  [in] HINTERNET hInternet,     // NULL
  [in] DWORD     dwOption,      // INTERNET_OPTION_SETTINGS_CHANGED
  [in] LPVOID    lpBuffer,      // NULL
  [in] DWORD     dwBufferLength // 0
);
```