# coding=utf-8

import pandas as pd, json, csv, os, sys, sqlite3
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
            file_input1 = input('Enter file 1:')
            file_input2 = input('Enter file 2:')
            file_output = input('Enter file output:')
            data_frame1 = pd.read_json(file_input1)
            data_frame2 = pd.read_json(file_input2)
            # data_frame1 = pd.read_json('results/sqlToJson.json')
            # data_frame2 = pd.read_json('results/joinEmail.json')
            data_list1 = data_frame1.to_dict(orient='records')
            data_list2 = data_frame2.to_dict(orient='records')

            data_json = list()

            for row1 in data_list1:
                for row2 in data_list2:
                    if row1['ci'] == row2['ci']:
                        print(row1, '/', row2)
                        data_json.append({
                            'row1': row1,
                            'row2': row2,
                        })
            print(len(data_json))
            ofile = os.path.join(BASE_DIR, 'set/results/'+file_output)
            with open(ofile, 'w+') as outfile:
                json.dump(data_json, outfile, indent=4)
        else:
            continue