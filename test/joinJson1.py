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
            file_log = os.path.join(BASE_DIR, 'set/vjoinjsonlog.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list_log = []
            for x in f1:
                list_log.append(x)
            count = int(list_log[0])
            fname = list_log[1]
            f.close()

            file_json = input('Enter file json:')
            output_json = input('Enter output file:')
            tmp_json = file_json.split('/')
            data1 = tmp_json[0]+'/'+tmp_json[1]
            data2 = tmp_json[0]+'/'+tmp_json[2]
            data3 = tmp_json[0]+'/'+tmp_json[3]
            data4 = tmp_json[0]+'/'+tmp_json[4]
            data5 = tmp_json[0]+'/'+tmp_json[5]
            data6 = tmp_json[0]+'/'+tmp_json[6]
            data7 = tmp_json[0]+'/'+tmp_json[7]
            data8 = tmp_json[0]+'/'+tmp_json[8]
            data9 = tmp_json[0]+'/'+tmp_json[9]
            data10 = tmp_json[0]+'/'+tmp_json[10]
            data11 = tmp_json[0]+'/'+tmp_json[11]
            data12 = tmp_json[0]+'/'+tmp_json[12]
            data13 = tmp_json[0]+'/'+tmp_json[13]
            data14 = tmp_json[0]+'/'+tmp_json[14]
            data15 = tmp_json[0]+'/'+tmp_json[15]
            data16 = tmp_json[0]+'/'+tmp_json[16]
            data17 = tmp_json[0]+'/'+tmp_json[17]
            data18 = tmp_json[0]+'/'+tmp_json[18]
            data_frame1 = pd.read_json(data1).to_dict(orient='records')
            data_frame2 = pd.read_json(data2).to_dict(orient='records')
            data_frame3 = pd.read_json(data3).to_dict(orient='records')
            data_frame4 = pd.read_json(data4).to_dict(orient='records')
            data_frame5 = pd.read_json(data5).to_dict(orient='records')
            data_frame6 = pd.read_json(data6).to_dict(orient='records')
            data_frame7 = pd.read_json(data7).to_dict(orient='records')
            data_frame8 = pd.read_json(data8).to_dict(orient='records')
            data_frame9 = pd.read_json(data9).to_dict(orient='records')
            data_frame10 = pd.read_json(data10).to_dict(orient='records')
            data_frame11 = pd.read_json(data11).to_dict(orient='records')
            data_frame12 = pd.read_json(data12).to_dict(orient='records')
            data_frame13 = pd.read_json(data13).to_dict(orient='records')
            data_frame14 = pd.read_json(data14).to_dict(orient='records')
            data_frame15 = pd.read_json(data15).to_dict(orient='records')
            data_frame16 = pd.read_json(data16).to_dict(orient='records')
            data_frame17 = pd.read_json(data17).to_dict(orient='records')
            data_frame18 = pd.read_json(data18).to_dict(orient='records')
            data_join = list()

            for row in data_frame1:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            
            for row in data_frame2:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            
            for row in data_frame3:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame4:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame5:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame6:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame7:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame8:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame9:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame10:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame11:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame12:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame13:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame14:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame15:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame16:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame17:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            for row in data_frame18:
                data_join.append({
                    'ci': row['ci'],
                    'ruc': row['ruc'],
                    'name': row['name'],
                    'activity': row['activity'],
                    'status': row['status'],
                    'salary': row['salary'],
                    'source': row['source'],
                    'count': row['count']
                })
            ofile = os.path.join(BASE_DIR, 'set/results/'+output_json)
            with open(ofile, 'w+') as outfile:
                json.dump(data_join, outfile, indent=4)
            
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
                    '''.format(start, timerun, end, ofile)
            print(message)
            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(list_log[1]))
            f.close()
        else:
            continue
