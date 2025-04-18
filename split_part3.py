from PyPDF2 import PdfReader, PdfWriter

def split_part3(input_path, output_prefix, part3_ranges):
    """拆分PDF的第三部分（协作与进化的智能系统）
    
    Args:
        input_path: 输入PDF路径
        output_prefix: 输出文件前缀
        part3_ranges: 第三部分页码范围，格式为[(起始页,结束页),...]
    """
    reader = PdfReader(input_path)
    
    # 第三部分章节名称
    chapter_names = [
        "多智能体系统设计(Design_of_Multi-Agent_Systems)",
        "通信拓扑(Communication_Topology)",
        "协作范式与机制(Collaboration_Paradigms)",
        "集体智能与适应(Collective_Intelligence)",
        "多智能体系统评估(Evaluating_Multi-Agent_Systems)"
    ]
    
    for i, ((start, end), name) in enumerate(zip(part3_ranges, chapter_names), 13):  # 从第13章开始编号
        writer = PdfWriter()
        for page in range(start-1, end):  # PyPDF2页码从0开始
            writer.add_page(reader.pages[page])
        
        output_name = f"{output_prefix}_Part3_{i}_{name}.pdf"
        with open(output_name, "wb") as f:
            writer.write(f)
        print(f"已生成: {output_name}")

# 第三部分页码范围（130-159页）
part3_ranges = [
    (133, 140),  # 第13章: 多智能体系统设计
    (141, 145),  # 第14章: 通信拓扑
    (146, 151),  # 第15章: 协作范式
    (152, 154),  # 第16章: 集体智能
    (155, 159)   # 第17章: 系统评估
]

# 使用示例
split_part3(
    input_path="2504.01990v1.pdf",
    output_prefix="2504.01990v1",
    part3_ranges=part3_ranges
)
