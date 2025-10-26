# UV

Rust 编写的极快 Python 包和项目管理工具，所以一些命令也是类似于 cargo 的

python 管理：

- uv python install: 安装 Python 版本
- uv python list: 查看可用 Python 版本
- uv python find: 查找已安装的 Python 版本
- uv python pin: 将当前项目固定使用特定 Python 版本
- uv python uninstall: 卸载 Python 版本

项目管理：

- uv init: 创建新 Python 项目
- uv add: 为项目添加依赖
- uv remove: 从项目移除依赖
- uv sync: 同步项目依赖到环境
- uv lock: 为项目依赖创建锁文件
- uv run: 在项目环境中运行命令
- uv tree: 查看项目依赖树.

实用工具：

- uv cache clean: 清除缓存条目
- uv cache prune: 清除过期的缓存条目
- uv cache dir: 显示 uv 缓存目录路径
- uv tool dir: 显示 uv 工具目录路径
- uv python dir: 显示 uv 安装的 Python 版本路径
- uv self update: 将 uv 更新至最新版本