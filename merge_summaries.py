import os
from datetime import datetime
import sys
import glob
import shutil
import re
import subprocess

# 输入文件列表
input_files = [
    "第一部分_总结.md",
    "第二部分_总结.md", 
    "第三部分_总结.md",
    "第四部分_总结.md"
]

# 输出文件
output_file = "完整总结_{}.pdf".format(datetime.now().strftime("%Y%m%d"))

# 清理临时文件
def cleanup_temp_files():
    print("\n清理临时文件...")
    # LaTeX临时文件
    temp_extensions = [
        '.aux', '.log', '.out', '.toc', '.lof', '.lot', '.fls', '.fdb_latexmk', 
        '.synctex.gz', '.blg', '.bbl', '.nav', '.snm', '.vrb', '.xdv', '.html',
        '.tex' # 清理所有tex文件
    ]
    
    # 查找和删除临时文件
    removed_count = 0
    for ext in temp_extensions:
        for file in glob.glob(f'*{ext}'):
            try:
                os.remove(file)
                removed_count += 1
            except Exception as e:
                print(f"无法删除文件 {file}: {e}")
                pass
    
    # 删除生成的模板
    template_files = ['template.tex', 'simple_output.tex', 'header.tex', 'footer.tex', 'test.tex']
    for file in template_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                removed_count += 1
            except:
                pass
    
    print(f"已清理 {removed_count} 个临时文件")

# 检查文件是否存在
missing_files = [f for f in input_files if not os.path.exists(f)]
if missing_files:
    print("以下文件缺失:")
    for f in missing_files:
        print(f" - {f}")
    exit(1)

# 合并Markdown文件
print("合并Markdown文件...")
with open("combined_summary.md", "w", encoding="utf-8") as out_f:
    out_f.write("# 论文完整总结\n\n")
    for file in input_files:
        with open(file, "r", encoding="utf-8") as in_f:
            content = in_f.read()
            out_f.write(f"## {file.replace('_总结.md', '')}\n\n")
            out_f.write(content)
            out_f.write("\n\n")

print("合并文件完成，正在生成PDF...")

# 使用最简单的方法：直接通过pandoc生成PDF，尽量减少复杂设置
print("\n尝试生成PDF（方法1 - 最简单方式）...")
cmd = f'pandoc combined_summary.md -o "{output_file}" --pdf-engine=xelatex -V mainfont="Microsoft YaHei" -V documentclass=article -V geometry:margin=2.5cm --verbose'
print(f"执行命令: {cmd}")
ret = os.system(cmd)

if ret == 0 and os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
    print(f"\n成功生成PDF: {output_file}")
    # 清理临时文件
    cleanup_temp_files()
    sys.exit(0)

# 如果第一种方法失败，尝试第二种方法：使用中文字体文件路径
print("\n尝试生成PDF（方法2 - 指定字体文件）...")
cmd = f'pandoc combined_summary.md -o "{output_file}" --pdf-engine=xelatex -V CJKmainfont="C:/Windows/Fonts/msyh.ttc" -V documentclass=article'
print(f"执行命令: {cmd}")
ret = os.system(cmd)

if ret == 0 and os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
    print(f"\n成功生成PDF: {output_file}")
    # 清理临时文件
    cleanup_temp_files()
    sys.exit(0)

# 如果前两种方法都失败，尝试第三种方法：使用简化的LaTeX模板
print("\n尝试生成PDF（方法3 - 简化模板）...")

latex_header = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[UTF8]{ctex}
\usepackage{geometry}
\geometry{a4paper,left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}
\usepackage{hyperref}
\begin{document}
"""

with open("header.tex", "w", encoding="utf-8") as f:
    f.write(latex_header)

with open("footer.tex", "w", encoding="utf-8") as f:
    f.write(r"\end{document}")

cmd = f'pandoc combined_summary.md -o "{output_file}" --pdf-engine=xelatex -H header.tex -A footer.tex --verbose'
print(f"执行命令: {cmd}")
ret = os.system(cmd)

if ret == 0 and os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
    print(f"\n成功生成PDF: {output_file}")
    # 清理临时文件
    cleanup_temp_files()
    sys.exit(0)

# 如果以上方法都失败，尝试更直接的方法：转换为Word后手动处理
print("\n无法直接生成PDF，尝试生成Word文档...")
word_file = "combined_summary.docx"
cmd = f'pandoc combined_summary.md -o "{word_file}"'
print(f"执行命令: {cmd}")
ret = os.system(cmd)

if ret == 0 and os.path.exists(word_file):
    print(f"\n成功生成Word文档: {word_file}")
    print("请用Word打开后另存为PDF")
    
    # 尝试自动打开Word文档
    try:
        os.startfile(os.path.abspath(word_file))
    except:
        print("无法自动打开Word文档，请手动打开")

# 最终清理
cleanup_temp_files()

print("\n处理完成。如果无法生成PDF，请检查系统配置：")
print("1. 确保已安装完整的TeX发行版（如MiKTeX或TeX Live）")
print("2. 确保已安装pandoc")
print("3. 确认微软雅黑字体(msyh.ttc)可用")
print("4. 如有Office，可尝试手动将Word文档转为PDF")
