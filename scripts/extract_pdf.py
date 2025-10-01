import sys
from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path(r"c:\Users\dan\Desktop\Competitive-programming\2024 problems\ccsce2024-contest.pdf")
if not pdf_path.exists():
    print('PDF not found', file=sys.stderr)
    sys.exit(1)

reader = PdfReader(str(pdf_path))
text = []
for p in reader.pages:
    text.append(p.extract_text() or '')

out = Path(r"c:\Users\dan\Desktop\Competitive-programming\2024 problems\ccsce2024-contest.txt")
out.write_text('\n\n'.join(text), encoding='utf-8')
print('Wrote', out)
