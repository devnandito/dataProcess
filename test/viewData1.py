# coding=utf-8

import pandas as pd, json, csv, os, sys, sqlite3, importlib
from datetime import datetime, timedelta

def ext(data):
    ext = data.split('.')
    ext = ext[1]
    return ext

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    while True:
        options = input('Enter options [start/quit]:')
        options = options.lower()
        if options == 'quit':
            break
        elif options == 'start':
            file_log = os.path.join(BASE_DIR, 'dataProcess/vars/viewData1.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list_log = []
            for x in f1:
                list_log.append(x)
            count = int(list_log[0])
            log_name = list_log[1]
            f.close()

            file_input = input('Enter file:')
            res = ext(file_input)
            
            if res == 'json':
                data_frame = pd.read_json(file_input)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:', len(data_list))
                print('Headers:', cols)
            elif res == 'xlsx':
                # data_frame = pd.read_excel(file_input, header=None)
                data_frame = pd.read_excel(file_input)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:', len(data_list))
                print('Headers:', cols)
            elif res == 'csv' or res == 'txt':
                header_options = input('''
                Enter options
                1. Read headers
                2. No read headers
                3. Save json
                Options:''')
                file_name = input('Enter file name:')
                if header_options == '1':
                    data_frame = pd.read_csv(file_input)
                    cols = data_frame.columns.ravel()
                    data_list = data_frame.to_dict(orient='records')
                    print('Total records:', len(data_list))
                    print(data_frame)
                elif header_options == '2':
                    data_frame = pd.read_csv(file_input, header=None)
                    cols = data_frame.columns.ravel()
                    data_list = data_frame.to_dict(orient='records')
                    print(data_frame)
                elif header_options == '3':
                    handle = open(file_input)
                    data_list = list()
                    for line in handle:
                        stuff = line.split(':')
                        print(stuff)
                        if stuff[1] == 'noencontrada\n' or stuff[1] == 'noencontrada':
                            print(line)
                        elif len(stuff) > 1:
                            data_list.append({
                                'ci': stuff[0],
                                'name': stuff[1] + ' ' + stuff[2],
                                'birthday': stuff[3],
                            })
                        else:
                            print(line)
                    print(data_list)
                    with open('results/ci1000.txt', 'w+') as f:
                        writer = csv.writer(f)
                        for row in data_list:
                            writer.writerow((row,))
                    
                    ofile = os.path.join(BASE_DIR, 'dataProcess/results/'+file_name)
                    with open(ofile, 'w+') as outfile:
                        json.dump(data_list, outfile, indent=4, ensure_ascii=False)

                # create_file = input('Write a module:')
                # file_output = input('Enter file output:')
                # module_input = input('Enter module:')
                
                # response = importlib.import_module(module_input)
                # data_json = response.printFor(data_list, cols)
                # for row in data_list:
                #     data_json.append({
                #         'ci': row[cols[0]],
                #         'first_name': row[cols[1]],
                #         'last_name': row[cols[2]],
                #     })
                # ofile = os.path.join(BASE_DIR, 'set/results/'+file_output)
                # with open(ofile, 'w+') as outfile:
                #     json.dump(data_json, outfile, indent=4, ensure_ascii=False)

            elif res == 'sql':
                file_output = input('Enter file output:')
                file_sql = os.path.join(BASE_DIR, 'dataProcess/queries/'+file_input)
                fsql = open(file_sql, "r")
                query = ''
                for x in fsql:
                    query = query + x
                
                conn = sqlite3.connect('/mnt/c/sqlite/db/pyt2.db')
                cur = conn.cursor()

                data_frame = pd.read_sql_query(query, conn, index_col=None)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:', len(data_list))
                print('Headers:', cols)

                data_json = list()
                for row in data_list:
                    data_json.append({
                        'ci': row[cols[0]],
                        'fist_name': row[cols[1]],
                        'last_name': row[cols[2]],
                        'department': row[cols[3]],
                        'district': row[cols[4]],
                        'cellphone': row[cols[5]],
                        'amount': row[cols[6]],
                        'remission': row[cols[7]],
                        'empe': row[cols[8]],
                    })
                
                ofile = os.path.join(BASE_DIR, 'dataProcess/results/'+file_output)
                with open(ofile, 'w+') as outfile:
                    json.dump(data_json, outfile, indent=4)
            else:
                print('Error archivo incorrecto')

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
                    '''.format(start, timerun, end, file_input.lstrip())
            print(message.strip())
            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(log_name))
            f.close()
        else:
            continue