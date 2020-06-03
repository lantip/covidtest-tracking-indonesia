Covid Test Scraper
===
Script ini bertujuan mengumpulkan laporan Gugus Tugas Covid terkait perkembangan jumlah laboratorium dan jumlah test di Indonesia sejak 1 April 2020. Data diambil dari twit Bapak Agus (@aw3126) dan dari BNPB (@bnpb_indonesia). 
Proses ocr menggunakan modul pytesseract.

Requirements
---
- Python 3
- twint
- pytesseract

Installation
---
- `git clone https://github.com/lantip/covidtest-tracking-indonesia.git`
- `cd covidtest-tracking-indonesia`
- Jalankan `pip install -r requirements.txt`

Usage
---
```
# untuk mengumpulkan twit, gunakan:
$ python main.py

File image akan disimpan dalam folder "data". Hasil akan tersimpan dalam file twit.json

# untuk proses extract text menjadi file json:
$ python tsr.py

Hasil akan disimpan dalam file result.json
```
