import os
import re

def merge_chapters():
    # 设定正文目录和输出文件
    base_dir = "🇩🇪创业往事-我开软件公司的七年/正文"
    output_file = "🇩🇪创业往事-我开软件公司的七年/完整故事.md"
    
    # 获取所有 .md 文件并按文件名排序
    files = sorted([f for f in os.listdir(base_dir) if f.endswith('.md')])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# 创业往事 - 我开软件公司的七年\n\n")
        
        for filename in files:
            filepath = os.path.join(base_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                if not lines:
                    continue
                
                # 获取第一行作为标题（如果符合 x/标题 格式）
                first_line = lines[0].strip()
                content = lines[1:]
                
                # 处理标题
                if '/' in first_line:
                    title = first_line.split('/', 1)[1]
                else:
                    title = first_line
                
                outfile.write(f"## {title}\n\n")
                outfile.writelines(content)
                outfile.write("\n\n---\n\n") # 添加分隔符
    
    print(f"已成功将 {len(files)} 个章节合并到 {output_file}")
    # 自动将生成的文件添加到 git 暂存区
    os.system(f"git add '{output_file}'")

if __name__ == "__main__":
    merge_chapters()
