import re

def modify_latex(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    documentclass_inserted = False
    begin_document_inserted = False

    for line in lines:
        modified_lines.append(line)

        if not documentclass_inserted and re.match(r'\\documentclass\[.*\]\{article\}', line):
            modified_lines.append('\\usepackage{url}\\usepackage{hyperref}\n')
            documentclass_inserted = True

        if not begin_document_inserted and re.match(r'\\begin\{document\}', line):
            modified_lines.append('\\usepackage{ragged2e}\\RaggedRight\n')
            begin_document_inserted = True

    with open(filename, 'w') as f:
        f.writelines(modified_lines)

if __name__ == "__main__":
    modify_latex("custom.tex")
