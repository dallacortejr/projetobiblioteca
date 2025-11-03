from pathlib import Path
from library_manager.core import add_document, remove_document

def test_add_and_remove(tmp_path):
    src = tmp_path / 't.docx'
    src.write_text('hello')
    dest_dir = tmp_path / 'store'
    added = add_document(str(src), str(dest_dir))
    assert Path(added).exists()
    assert remove_document(str(added))
    assert not Path(added).exists()
