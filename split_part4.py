from PyPDF2 import PdfReader, PdfWriter

def split_pdf_part4(input_path, output_prefix, chapter_ranges):
    """拆分PDF文件的第四部分（构建安全有益的AI智能体）

    Args:
        input_path: 输入PDF文件路径
        output_prefix: 输出文件前缀
        chapter_ranges: 章节页码范围列表，格式为[(起始页,结束页),...]
    """
    reader = PdfReader(input_path)

    # 第四部分章节名称（中英文对照）
    chapter_names = [
        "智能体内在安全_AI大脑的威胁(Intrinsic_Safety_Brain_Threats)",
        "智能体内在安全_非大脑模块的威胁(Intrinsic_Safety_NonBrain_Threats)",
        "智能体外在安全_交互风险(Extrinsic_Safety_Interaction_Risks)",
        "超级对齐与安全扩展法则(Superalignment_Safety_Scaling)",
        "结论与未来展望(Concluding_Remarks)"
    ]

    for i, ((start, end), name) in enumerate(zip(chapter_ranges, chapter_names), 1):
        writer = PdfWriter()
        for page in range(start-1, end):  # PyPDF2页码从0开始
            writer.add_page(reader.pages[page])
    
        # 生成输出文件名（保持和第三部分相同的命名风格）
        output_name = f"{output_prefix}_Part4_{i}_{name}.pdf"
        with open(output_name, "wb") as f:
            writer.write(f)
        print(f"已生成: {output_name}")

# 第四部分的章节页码范围
part4_chapter_ranges = [
    (163, 175),   # 第18章
    (176, 179),   # 第19章
    (180, 183),   # 第20章
    (184, 188),   # 第21章
    (189, 190)    # 第22章
]

# 使用示例
split_pdf_part4(
    input_path="2504.01990v1.pdf",
    output_prefix="2504.01990v1",
    chapter_ranges=part4_chapter_ranges
)
