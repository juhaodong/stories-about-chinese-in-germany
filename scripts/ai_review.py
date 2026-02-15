import os
import sys

def ai_review():
    story_file = "🇩🇪创业往事-我开软件公司的七年/完整故事.md"
    review_file = "🇩🇪创业往事-我开软件公司的七年/修改意见.md"
    
    if not os.path.exists(story_file):
        print(f"找不到文件: {story_file}")
        return

    with open(story_file, 'r', encoding='utf-8') as f:
        story_content = f.read()

    # 这里提供一个脚本框架。由于在本地环境中运行需要 API Key，
    # 脚本会检查环境变量。如果没有 API Key，它将提醒用户。
    api_key = os.getenv("OPENAI_API_KEY")
    
    print("正在生成 AI 修改意见...")
    
    if not api_key:
        review_content = "# AI 修改意见\n\n> [!CAUTION]\n> 未检测到 `OPENAI_API_KEY` 环境变量。请在环境中设置它以启用自动 AI 评审。\n\n## 预设评审要点 (需配置 API)\n1. 剧情连贯性\n2. 错别字检查\n3. 情感表达建议\n"
        print("警告: 未设置 OPENAI_API_KEY。生成了占位文档。")
    else:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "你是一位资深的文学编辑，请阅读以下创业回忆录，并提供专业的修改意见，包括结构、叙事节奏、错别字及情感表达。"},
                    {"role": "user", "content": story_content}
                ]
            )
            review_content = f"# AI 修改意见 (由 GPT-4o 生成)\n\n{response.choices[0].message.content}"
        except Exception as e:
            review_content = f"# AI 修改意见\n\n获取 AI 意见时发生错误: {str(e)}"
            print(f"错误: {e}")

    with open(review_file, 'w', encoding='utf-8') as f:
        f.write(review_content)
    
    # 自动添加到 git 暂存区
    os.system(f"git add '{review_file}'")
    print(f"修改意见已更新至: {review_file}")

if __name__ == "__main__":
    ai_review()
