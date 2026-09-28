import json
from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_doctypes_are_valid_json():
    docs = list((ROOT / 'academic_management').rglob('*.json'))
    assert len(docs) >= 15
    for path in docs:
        data=json.loads(path.read_text(encoding='utf-8'))
        assert data['doctype'] == 'DocType'
        assert 'name' in data

def test_required_modules_exist():
    for path in ['academic_management/hooks.py','academic_management/api/dashboard.py','docs/system-design.md']:
        assert (ROOT / path).exists()
