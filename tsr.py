from PIL import Image
from pytesseract import image_to_string
import json
from os import walk

def ocr_date(jpg):
    data = image_to_string(Image.open('data/'+jpg))
    result = {}
    before = ''
    befjum = 0
    lines = data.split('\n')
    for idx, line in enumerate(lines):
        line = line.replace('_',' ').replace('  ',' ')
        dta = line.split()

        if len(dta) > 1:
            if dta[len(dta)-1].strip().lower().replace('.','').strip() in ['lab', 'spesimen', 'orang', 'buah', 'biji']:
                try:
                    jml = int(dta[len(dta)-2].replace(',','').replace('.',''))
                except:
                    jml  = None
            else:
                try:
                    jml = int(dta[len(dta)-1].replace(',','').replace('.',''))
                except:
                    jml  = None
            if jml:
                if dta[len(dta)-1].strip().lower().replace('.','').strip() in ['lab', 'spesimen', 'orang', 'buah', 'biji']:
                    key = line.replace(' '+str(dta[len(dta)-2])+' '+str(dta[len(dta)-1]),'')
                else:
                    key = line.replace(' '+str(dta[len(dta)-1]),'')
                if dta[len(dta)-1].strip().lower().replace('.','').strip() in ['lab', 'spesimen', 'orang', 'buah', 'biji']:
                    if idx > 0:
                        if 'RT-PCR' in lines[idx-1]:
                            if not 'Jumlah' in lines[idx-1]:
                                key = 'TCM'
                    if 'RT-PCR' in key:
                        if not 'Jumlah' in key:
                            key = 'RT-PCR'
                    if key in result:
                        key = key+'-'+str(idx)
                    if '.' in key:
                        key = key.replace(key.split('.')[0]+'. ','')
                    if 'RT-PCR' in lines[idx+1]:
                        if not 'Jumlah' in lines[idx+1]:
                            before = key
                    if key == 'RT-PCR':
                        befjum = result[before]
                        result[before] = {}
                        result[before]['total'] = befjum
                        result[before]['total'] = befjum
                        result[before][key] = jml
                    elif key == 'TCM':
                        result[before][key] = jml
                    else:
                        result[key] = jml
                else:
                    if not key in result:
                        result[key] = jml
    return result


f = []
for (dirpath, dirnames, filenames) in walk('./data'):
    f.extend(filenames)
    break
hasil = {}
for i in f:
    rslt = ocr_date(i)
    hasil[i.replace('.jpg','')] = rslt

result = hasil.items()
sorted_result = sorted(result)
#hasil = ocr_date('2020-05-09.jpg')

with open('result.json','w') as fle:
    fle.write(json.dumps(sorted_result,indent=4))

print(json.dumps(sorted_result,indent=4))