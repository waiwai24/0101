# github action

## 1.基本概念

用于根据推送、拉取请求或定时任务等事件构建、测试和部署代码, 工作流一般配置在 `.github/workflows` 目录下的 YAML 文件

一些基本概念：

- workflow （工作流程）：持续集成一次运行的过程，就是一个 workflow
- job （任务）：一个 workflow 由一个或多个 jobs 构成，含义是一次持续集成的运行，可以完成多个任务
- step（步骤）：每个 job 由多个 step 构成，一步步完成
- action （动作）：每个 step 可以依次执行一个或多个 action



## 2.workflow 字段

* name：workflow 的名称
* on：触发条件（发生的事件，手动或预定时间）
* job：执行的任务

```yaml
jobs:
  job_name:             # 任务 ID（唯一标识）
    name: 任务名称       # 任务的可读名称（可选）
    runs-on: 运行环境   # 任务运行的环境
    needs: 依赖任务     # 当前任务需要等待哪些任务完成（可选）
    if: 条件判断        # 任务是否执行的条件（可选）
    outputs:            # 任务的输出变量（可选）
      key: value
    strategy:           # 并行或矩阵策略（可选）
      matrix: ...
    steps:              # 任务中的执行步骤
      - name: 步骤名称
        id: 步骤 ID
        uses: 使用 GitHub 组件
        run: 执行 Shell 命令
        with: 组件的参数
        env: 设定环境变量
```

