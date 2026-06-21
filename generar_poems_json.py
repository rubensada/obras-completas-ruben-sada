"""
Convierte OBRAS_COMPLETAS_LIMPIO.txt -> poems.json para el sitio de búsqueda.

Uso:
    python3 generar_poems_json.py

Requisitos del .txt:
- Cada poema empieza con una línea "§ TÍTULO DEL POEMA"
- El archivo está codificado en UTF-8 (el que generamos ya lo está)
- (Opcional) una línea "@FECHA: ..." en cualquier parte del poema indica
  la fecha en que se escribió. Se guarda aparte y no se mezcla con el
  texto del poema ni con la búsqueda.

Ejecutalo cada vez que agregues poemas nuevos al .txt, y subí el
poems.json actualizado a GitHub (junto con el .txt si querés tenerlo
versionado también).
"""
import json
import re
import sys
from pathlib import Path

TXT_PATH = Path("OBRAS_COMPLETAS_LIMPIO.txt")
JSON_PATH = Path("poems.json")

FECHA_RE = re.compile(r"^@FECHA:\s*(.*)$", re.IGNORECASE)


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9áéíóúñü ]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s


def main():
    if not TXT_PATH.exists():
        sys.exit(f"No encuentro {TXT_PATH}. Poné este script en la misma carpeta que el .txt.")

    text = TXT_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")
    marks = [i for i, l in enumerate(lines) if l.strip().startswith("§")]

    if not marks:
        sys.exit("No encontré ningún título marcado con §. Revisá el archivo.")

    poems = []
    poems_with_date = 0
    for idx, start in enumerate(marks):
        end = marks[idx + 1] if idx + 1 < len(marks) else len(lines)
        title = lines[start].lstrip("§").strip()
        body = lines[start + 1:end]

        date = None
        clean_body = []
        for line in body:
            m = FECHA_RE.match(line.strip())
            if m:
                date = m.group(1).strip()
            else:
                clean_body.append(line)
        body = clean_body

        while body and body[0].strip() == "":
            body.pop(0)
        while body and body[-1].strip() == "":
            body.pop()

        if date:
            poems_with_date += 1

        poems.append({
            "id": idx + 1,
            "title": title,
            "slug": f"{slugify(title)}-{idx + 1}",
            "text": "\n".join(body),
            "date": date,
        })

    JSON_PATH.write_text(json.dumps(poems, ensure_ascii=False), encoding="utf-8")
    size_kb = JSON_PATH.stat().st_size / 1024
    print(f"Listo: {len(poems)} poemas -> {JSON_PATH} ({size_kb:.0f} KB)")
    print(f"Poemas con fecha cargada: {poems_with_date} de {len(poems)}")


if __name__ == "__main__":
    main()
