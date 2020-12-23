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
            file_log = os.path.join(BASE_DIR, 'set/vjsonveriflog.txt')
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
            
            data_frame1 = pd.read_json(file_json).to_dict(orient='records')
            data_join = list()
            line = 0
            counts = dict()
            activities = dict()
            sources = dict()

            for row in data_frame1:
                line += 1
                ci = row['ci']
                if ci not in counts:
                    counts[ci] = 1
                    activities[ci] = row['activity']
                    sources[ci] = row['source']
                    data_join.append({
                        'ci': row['ci'],
                        'ruc': row['ruc'],
                        'name': row['name'],
                        'activity': activities[ci],
                        'status': row['status'],
                        'salary': row['salary'],
                        'source': sources[ci],
                        'count': counts[ci]
                    })
                    print('New: {}, Line: {}'.format(ci,line))
                else:
                    counts[ci] = counts[ci] + 1
                    activities[ci] = activities[ci] + '/' + row['activity'] + '-' + str(counts[ci])
                    sources[ci] = sources[ci] + '/' + row['source']
                    for i in range(len(data_join)):
                        if data_join[i]['ci'] == ci:
                            data_join[i]['activity'] = activities[ci]
                            data_join[i]['source'] = sources[ci]
                            data_join[i]['count'] = counts[ci]
                        else:
                            break
                    print('Duplicated: {}, Line: {}'.format(ci,line))

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
