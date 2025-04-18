# PDF 论文分割工具

本项目是为方便阅读 arXiv 论文 **"Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems"** (编号: 2504.01990v1) 而开发的专用工具。

## 论文概述
这篇论文探讨了基础智能体的前沿进展与挑战，分为四个主要部分：
1. 第一部分：智能体的核心组件
2. 第二部分：智能体的自我进化
3. 第三部分：协作与进化的智能系统
4. 第四部分：构建安全有益的AI智能体

## 功能说明
- 将长篇论文PDF按章节拆分为多个小文件
- 自动命名输出文件，包含章节编号和标题
- 保留原论文的目录结构和页码信息

## 使用方法
1. 确保安装Python 3.x和PyPDF2库：
   ```powershell
   pip install PyPDF2
   ```

2. 运行分割脚本：
   ```powershell
   python split_part1.py  # 处理第一部分
   python split_part2.py  # 处理第二部分
   python split_part3.py  # 处理第三部分
   python split_part4.py  # 处理第四部分
   ```

3. 输出文件将保存在当前目录和对应的子目录中

## 文件结构
- `split_part1.py` - 处理第一部分(智能体的核心组件)
- `split_part2.py` - 处理第二部分(智能体的自我进化)
- `split_part3.py` - 处理第三部分(协作与进化的智能系统)
- `split_part4.py` - 处理第四部分(构建安全有益的AI智能体)
- `rename.py` - 辅助重命名工具
- `第一部分/` - 第一部分章节输出目录
- `第二部分/` - 第二部分章节输出目录
- `第三部分/` - 第三部分章节输出目录
- `第四部分/` - 第四部分章节输出目录

## 依赖项
- Python 3.x
- PyPDF2 库

## 注意事项
- 请确保原论文文件 `2504.01990v1.pdf` 存在于项目目录中
- 分割后的文件命名格式为：`2504.01990v1_PartX_Y_章节名称.pdf`
