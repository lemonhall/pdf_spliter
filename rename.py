import os
from pathlib import Path

# 定义原始文件名和对应的注释描述
file_info = {
    "2504.01990v1_part1.pdf": "目录部分",
    "2504.01990v1_part2.pdf": "词汇表",
    "2504.01990v1_part3.pdf": "介绍",
    "2504.01990v1_part4.pdf": "第一部分-智能体的核心组件",
    "2504.01990v1_part5.pdf": "第二部分-智能体的自我进化",
    "2504.01990v1_part6.pdf": "第三部分-协作与进化的智能系统",
    "2504.01990v1_part7.pdf": "第四部分-构建安全有益的AI智能体"
}

def rename_pdf_files(directory):
    """根据注释内容重命名PDF文件"""
    for old_name, description in file_info.items():
        old_path = Path(directory) / old_name
        if old_path.exists():
            # 构建新文件名，保留原始编号和添加描述
            new_name = f"2504.01990v1_{description}.pdf"
            new_path = Path(directory) / new_name
            try:
                old_path.rename(new_path)
                print(f"已重命名: {old_name} -> {new_name}")
            except Exception as e:
                print(f"重命名 {old_name} 失败: {e}")
        else:
            print(f"文件不存在: {old_name}")

# 指定包含PDF文件的目录
pdf_directory = r"E:\development\pdf_spliter"
rename_pdf_files(pdf_directory)
