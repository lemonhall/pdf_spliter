from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_chapters(input_path, output_prefix, chapter_ranges):
    """按章节拆分PDF文件
    
    Args:
        input_path: 输入PDF文件路径
        output_prefix: 输出文件前缀
        chapter_ranges: 章节页码范围列表，格式为[(起始页,结束页),...]
    """
    reader = PdfReader(input_path)
    
    # 定义章节名称
    chapter_names = [
        "认知(Cognition)",
        "记忆(Memory)",
        "世界模型(World_Model)",
        "奖励(Reward)",
        "情感建模(Emotion_Modeling)",
        "感知(Perception)",
        "行动系统(Action_Systems)"
    ]
    
    for i, ((start, end), name) in enumerate(zip(chapter_ranges, chapter_names), 1):
        writer = PdfWriter()
        for page in range(start-1, end):  # PyPDF2页码从0开始
            writer.add_page(reader.pages[page])
        
        # 生成输出文件名，包含章节编号和名称
        output_name = f"{output_prefix}_Part1_{i}_{name}.pdf"
        with open(output_name, "wb") as f:
            writer.write(f)
        print(f"已生成: {output_name}")

# 第一部分的章节页码范围
part1_chapter_ranges = [
    (25, 38),   # 第2章: 认知
    (39, 53),   # 第3章: 记忆
    (54, 62),   # 第4章: 世界模型
    (63, 70),   # 第5章: 奖励
    (71, 76),   # 第6章: 情感建模
    (77, 85),   # 第7章: 感知
    (86, 97)    # 第8章: 行动系统
]

# 使用示例
split_pdf_by_chapters(
    input_path="2504.01990v1.pdf",
    output_prefix="2504.01990v1",
    chapter_ranges=part1_chapter_ranges
)
