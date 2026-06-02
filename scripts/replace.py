import re
from pathlib import Path

ORIGINAL_FILE = Path("CompleteSuicideManual-Zh_CN.md")
MD_FOOTNOTE_PATTERN = re.compile(r"\[\^(\d+)\]")

NEW_FOOTNOTE_NO = 10 # 表示新插入的脚注编号，所有大于等于这个编号的脚注都需要加1

print("Load all footnotes...")
file_content = ORIGINAL_FILE.read_text(encoding="utf-8")
footnotes = sorted(set(int(n) for n in MD_FOOTNOTE_PATTERN.findall(file_content)), reverse=True)
print(f"Found {len(footnotes)} unique footnotes, last footnote no: {footnotes[0]}")

print("Replace footnotes...")
# 从最后一个脚注开始加1，直到 NEW_FOOTNOTE_NO ，避免替换过程中影响到后续的脚注编号
for footnote_no in footnotes:  # 已按降序排列
    if footnote_no >= NEW_FOOTNOTE_NO:
        new_footnote_no = footnote_no + 1
        file_content = file_content.replace(f"[^{footnote_no}]", f"[^{new_footnote_no}]")
        print(f"Replaced footnote [^{footnote_no}] with [^{new_footnote_no}]")
    else:
        break

print("Write back to file...")
ORIGINAL_FILE.write_text(file_content, encoding="utf-8")
print("Done.")