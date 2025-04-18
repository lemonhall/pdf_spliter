import os
import logging
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path: str) -> str:
    """从PDF文件中提取文本内容"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        logger.error(f"读取PDF文件 {pdf_path} 时出错: {e}")
        return ""

def summarize_with_model(text: str, api_key: str, model_name: str, api_base: str | None = None) -> str:
    """使用大模型API总结文本内容"""
    if not api_key:
        logger.error("未提供API密钥")
        return "错误：未提供API密钥"
    if not model_name:
        logger.error("未提供模型名称")
        return "错误：未提供模型名称"

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=api_base
        )

        prompt = "全程用中文总结，这一章节主要讲了些啥？\n\n" + text
        logger.info(f"正在将文本发送到模型 '{model_name}' 进行总结...")
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        
        summary = response.choices[0].message.content
        logger.info("总结已接收")
        return summary

    except Exception as e:
        logger.error(f"API调用出错: {e}")
        return f"总结文本时出错: {e}"

def process_directory(directory: str, output_file: str, api_key: str, model_name: str, api_base: str | None = None):
    """处理目录中的所有PDF文件"""
    if not os.path.exists(directory):
        logger.error(f"目录不存在: {directory}")
        return

    with open(output_file, 'a', encoding='utf-8') as out_f:
        from datetime import datetime
        out_f.write(f"\n\n=== 运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")
        for filename in os.listdir(directory):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(directory, filename)
                logger.info(f"正在处理文件: {pdf_path}")
                
                text = extract_text_from_pdf(pdf_path)
                if not text:
                    out_f.write(f"文件 {filename} 内容提取失败\n\n")
                    continue
                
                summary = summarize_with_model(text, api_key, model_name, api_base)
                out_f.write(f"=== {filename} 总结 ===\n")
                out_f.write(summary + "\n\n")

def main():
    test_api_key = os.getenv("HUOSHAN_API_KEY")  # 火山引擎API密钥
    model_name = "ep-20250328074804-dj5t9"  # 火山引擎模型名称
    api_base = "https://ark.cn-beijing.volces.com/api/v3/"  # 火山引擎API地址


    # 处理所有四个部分
    parts = ["第一部分", "第二部分", "第三部分", "第四部分"]
    for part in parts:
        output_file = f"{part}_总结.md"
        logger.info(f"开始处理 {part}...")
        process_directory(part, output_file, test_api_key, model_name, api_base)
        logger.info(f"{part} 处理完成，结果保存在 {output_file}")

if __name__ == '__main__':
    main()
