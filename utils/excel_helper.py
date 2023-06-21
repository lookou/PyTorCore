import xlwt
from datetime import datetime
from llog import llogger
import conf

logger = llogger()

def WriteExcel(excel_data):
  now = datetime.now().strftime("%Y%m%d%H%M")
  excel_name = r"{0}excel{1}.xls".format(conf.panid_save_addr, now)
  book = xlwt.Workbook()
  title = ["uid", "user_id"]
  for sheet_name,data in excel_data.items():
    logger.debug(sheet_name + ": " + str(len(data)))
    sheet = book.add_sheet(sheet_name)
    # 写表头
    i = 0
    for header in title:
      sheet.write(0, i, header)
      i += 1
    # 写数据
    length = len(data)
    for row in range(0, length):
      #一个sheet最多写60000条数据
      if row > 0 and row % 60000 == 0:
        logger.debug(sheet_name + "sheet已满")
        sheet = book.add_sheet(sheet_name + str(row//60000))
        # 写表头
        i = 0
        for header in title:
          sheet.write(0, i, header)
          i += 1

      for col in range(0, len(data[row])):
        sheet.write(row%60000 + 1, col, data[row][col])
  
  book.save(excel_name)
  return excel_name
