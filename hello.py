# split_pdf.py
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_prefix, split_ranges):
    """按页码范围切割PDF
    split_ranges: 例如 [(1,3), (4,6)] 表示1-3页为part1，4-6页为part2
    """
    reader = PdfReader(input_path)
    for i, (start, end) in enumerate(split_ranges, 1):
        writer = PdfWriter()
        for page in range(start-1, end):  # PyPDF2页码从0开始
            writer.add_page(reader.pages[page])
        with open(f"{output_prefix}_part{i}.pdf", "wb") as f:
            writer.write(f)

# 更新后的切割范围，包含7个部分
split_ranges = [
    (1, 8),    # 目录部分
    (9, 11),   # 词汇表
    (12, 22),  # 介绍
    (24, 97),  # 第一部分：智能体的核心组件
    (100, 129), # 第二部分：智能体的自我进化
    (130, 159), # 第三部分：协作与进化的智能系统
    (160, 189)  # 第四部分：构建安全有益的AI智能体
]
split_pdf("2504.01990v1.pdf", "2504.01990v1", split_ranges)
