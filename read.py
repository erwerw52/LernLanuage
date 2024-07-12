import random
import ezodf

def ods_to_dict(filename, sheet_no=0, header=0):

  odf = ezodf.opendoc(filename)
  sheet = odf.sheets[sheet_no]

  columns = list(sheet.columns())

  sheets = []
  for she in odf.sheets:
    sheets.append(she.name)

  keys = [cell.value for cell in columns[0] if cell.value is not None][header + 1:]
  values = [cell.value for cell in columns[1] if cell.value is not None][header + 1:]

  ods_contact = dict(zip(keys, values))
  ods_contact['sheets_no'] = sheets
  
  return ods_contact

def readRandomDict(day):
  filename = 'vocabulary.ods'
  result_dict = ods_to_dict(filename, day)
  
  x = random.randrange(0, 59)
  keys = list(result_dict.keys())
  values = list(result_dict.values())
  
  tf = {}
  try:
    tf = {keys[x] : values[x]}
  except IndexError:
    tf = {'錯誤' : '超出範圍'}
  tf['current'] = str(x + 1)#目前位置
  tf['size'] = str(len(keys))#總列數
  tf['sheets_no'] = result_dict['sheets_no']#總sheet名稱
  return tf