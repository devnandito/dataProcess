# coding=utf-8

import pandas as pd, sqlite3, os, sys
from datetime import datetime, timedelta

if __name__ == '__main__':

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        options = input('Enter options [start/quit]:')
        options = options.lower()
        if options == 'quit': 
            break
        elif options == 'start':
            xlsxname = input('Enter file name to excel:')
            sqlfile = input('Enter query file sql:')
            colstart1 = input('Enter column initial title 1:')
            colend1 = input('Enter column end title 1:')
            colstart2 = input('Enter column initial title 2:')
            colend2 = input('Enter column end title 2:')
            title1 = input('Enter title 1:')
            title2 = input('Enter title 2:')
            size_cell = input('Enter size cell:')

            file_log = os.path.join(BASE_DIR, 'set/vlog.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list1 = []
            for x in f1:
                list1.append(x)
            count = int(list1[0])
            fname = list1[1]
            f.close()

            filesql = os.path.join(BASE_DIR, 'set/'+sqlfile)
            fsql = open(filesql, "r")
            query1 = ''
            for x in fsql:
                query1 = query1 + x

            conn = sqlite3.connect('/mnt/c/sqlite/db/pyt2.db')

            cur = conn.cursor()

            df = pd.read_sql_query(query1, conn)

            xfile = os.path.join(BASE_DIR, 'set/results/')
            xlsx = '.xlsx'
            # xname = xfile+list1[1].rstrip('\n')+list1[0].rstrip('\n')+xlsx
            xname = xfile+xlsxname+xlsx
            writer = pd.ExcelWriter(xname, engine='xlsxwriter')

            df.to_excel(writer, sheet_name='Sheet1', startrow=2, index=False, header=False)
            # df.to_excel(writer, sheet_name='Sheet1', startrow=1, index=False, header=False, columns=['PK', 'FK', 'TITLE'], startcol=0)
            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            cell_format = workbook.add_format()
            c1 = colstart1+':'+colend1
            c2 = colstart2+':'+colend2
            size_cell = int(size_cell)
            worksheet.set_column(c1, size_cell, cell_format)
            worksheet.set_column(c2, size_cell, cell_format)
            # cell_format.set_border()

            cell_format_title1 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'green',
                'size': 12
            })

            cell_format_title2 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'yellow',
                'size': 12
            })

            t1 = '{}1:{}1'.format(colstart1,colend1)
            t2 = '{}1:{}1'.format(colstart2,colend2)
            worksheet.merge_range(t1, title1, cell_format_title1)
            worksheet.merge_range(t2, title2, cell_format_title2)

            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#D7E4BC',
                'border': 1,
                'size': 12
            })

            for col_num, value in enumerate(df.columns.values):
                worksheet.write(1, col_num, value, header_format)
                # worksheet.write(0, col_num + 1, value, header_format)

            writer.save()

            conn.close()

            now = datetime.now()
            ohour = now.hour
            ominute = now.minute
            osecond = now.second
            end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
            timerun = end - start
            message = '''
                    Time start: {} \n
                    Runtime: {} \n
                    Time finish: {}
                    '''.format(start, timerun, end)
            print(message)

            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(list1[1]))
            f.close()

            ext1 = '.txt'
            logFile = '%s%s%s'%(list1[1].rstrip('\n'),list1[0].rstrip('\n'),ext1)
            filename1 = os.path.join(BASE_DIR, 'set/logs/'+logFile)
            f = open(filename1, 'w')
            f.write(str(message))
            f.close