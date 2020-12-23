import pandas as pd, json, csv, re, os, sys
from datetime import datetime, timedelta

if __name__ == '__main__':
    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    while True:
        initial = input('Enter options start/quit:')
        initial = initial.lower()
        if initial == 'quit':
            break
        elif initial == 'start':
            file_log = os.path.join(BASE_DIR, 'set/vquerylog.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list_log = []
            for x in f1:
                list_log.append(x)
            count = int(list_log[0])
            fname = list_log[1]
            f.close()

            file_excel = input('Enter file excel:')
            table_name = input('Enter table name:')
            output_file = input('Enter output file:')
            
            data_frame1 = pd.read_excel(file_excel, usecols='B:D', skiprows=range(0,8))
            data_frame1 = data_frame1.dropna(subset=['CEDULA', 'NOMBRE', 'APELLIDO'])
            data_frame1 = data_frame1.to_dict(orient='records')

            ofile = os.path.join(BASE_DIR, 'set/results/'+output_file)
            with open(ofile, 'w+') as outfile:
                for row in data_frame1:
                    tmp_ci = str(row['CEDULA'])
                    ci = tmp_ci.split('.')
                    query_insert = 'INSERT INTO {} (document, name, lastname) VALUES ("{}", "{}", "{}"); \n'.format(table_name, ci[0], row['NOMBRE'], row['APELLIDO'])
                    outfile.write(query_insert)
            
            now = datetime.now()
            ohour = now.hour
            ominute = now.minute
            osecond = now.second
            end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
            timerun = end - start
            message = '''
                    Time start: {} \n
                    Runtime: {} \n
                    Time finish: {} \n
                    File: {}
                    '''.format(start, timerun, end, output_file)
            print(message)
            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(list_log[1]))
            f.close()
        else:
            continue
