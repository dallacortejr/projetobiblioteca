import os
from pathlib import Path
from typing import List, Dict
from datetime import datetime
from dateutil import parser as dateparser
import PyPDF2
import docx
from ebooklib import epub

SUPPORTED = ['.pdf', '.epub', '.mobi', '.azw', '.docx']

def find_documents(root: str) -> List[Path]:
    p = Path(root)
    return [f for f in p.rglob('*') if f.suffix.lower() in SUPPORTED]

def extract_year(path: Path) -> int | None:
    try:
        if path.suffix.lower() == '.pdf':
            with open(path, 'rb') as fh:
                reader = PyPDF2.PdfReader(fh)
                meta = reader.metadata
                date = meta.get('/CreationDate') or meta.get('/ModDate')
                if date and date.startswith('D:'):
                    return int(date[2:6])
        elif path.suffix.lower() == '.docx':
            doc = docx.Document(path)
            props = doc.core_properties
            if props.created:
                return props.created.year
        elif path.suffix.lower() == '.epub':
            book = epub.read_epub(str(path))
            if book.get_metadata('DC', 'date'):
                ds = book.get_metadata('DC', 'date')[0][0]
                return dateparser.parse(ds).year
    except:
        return None
    return None

def list_by_type_and_year(root: str) -> Dict[str, Dict[str, List[str]]]:
    files = find_documents(root)
    out: Dict[str, Dict[str, List[str]]] = {}
    for f in files:
        t = f.suffix.lower().lstrip('.')
        year = extract_year(f) or 'unknown'
        out.setdefault(t, {}).setdefault(str(year), []).append(str(f))
    return out

def add_document(src_path: str, dest_dir: str) -> Path:
    src = Path(src_path)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if src.resolve() == dest.resolve():
        return dest
    with open(src, 'rb') as r, open(dest, 'wb') as w:
        w.write(r.read())
    return dest

def rename_document(path: str, new_name: str) -> Path:
    p = Path(path)
    dest = p.with_name(new_name)
    p.rename(dest)
    return dest

def remove_document(path: str) -> bool:
    p = Path(path)
    if p.exists():
        p.unlink()
        return True
    return False
