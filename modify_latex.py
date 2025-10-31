import re

def modify_latex(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    documentclass_inserted = False

    for line in lines:
        modified_lines.append(line)

        if not documentclass_inserted and re.match(r'\\documentclass\[.*\]\{.*\}', line):  # 匹配 documentclass 行
            modified_lines.append('\\usepackage{url}\\usepackage{hyperref}\\usepackage{ragged2e}\\RaggedRight\n')  # 添加 usepackage 命令
            documentclass_inserted = True

    with open(filename, 'w') as f:
        f.writelines(modified_lines)

if __name__ == "__main__":
    modify_latex("custom.tex")
