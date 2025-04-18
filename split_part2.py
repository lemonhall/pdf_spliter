from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_chapters(input_path, output_prefix, chapter_ranges):
    """按章节拆分PDF文件
    
    Args:
        input_path: 输入PDF文件路径
        output_prefix: 输出文件前缀
        chapter_ranges: 章节页码范围列表，格式为[(起始页,结束页),...]
    """
    reader = PdfReader(input_path)
    
    # 定义第二部分章节名称
    chapter_names = [
        "自进化的优化空间和维度(Optimization_Spaces)",
        "大型语言模型作为优化器(LLMs_as_Optimizers)",
        "在线和离线智能体自我改进(Self-Improvement)",
        "科学发现与智能进化(Scientific_Discovery)"
    ]
    
    for i, ((start, end), name) in enumerate(zip(chapter_ranges, chapter_names), 1):
        writer = PdfWriter()
        for page in range(start-1, end):  # PyPDF2页码从0开始
            writer.add_page(reader.pages[page])
        
        # 生成输出文件名，包含部分编号和章节名称
        output_name = f"{output_prefix}_Part2_{i}_{name}.pdf"
        with open(output_name, "wb") as f:
            writer.write(f)
        print(f"已生成: {output_name}")

# 第二部分的章节页码范围
part2_chapter_ranges = [
    (103, 110),   # 第9章: 自进化的优化空间和维度
    (111, 115),   # 第10章: 大型语言模型作为优化器
    (116, 119),   # 第11章: 在线和离线智能体自我改进
    (120, 129)    # 第12章: 科学发现与智能进化
]

# 使用示例
split_pdf_by_chapters(
    input_path="2504.01990v1.pdf",
    output_prefix="2504.01990v1",
    chapter_ranges=part2_chapter_ranges
)
