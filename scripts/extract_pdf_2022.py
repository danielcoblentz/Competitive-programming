from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path(r"c:\Users\dan\Desktop\Competitive-programming\2022 problems\ccsce2022-contest.pdf")
reader = PdfReader(str(pdf_path))
text = []
for p in reader.pages:
    text.append(p.extract_text() or '')

out = Path(r"c:\Users\dan\Desktop\Competitive-programming\2022 problems\ccsce2022-contest.txt")
out.write_text('\n\n'.join(text), encoding='utf-8')
print('Wrote', out)
