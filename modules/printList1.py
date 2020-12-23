def printFor(data_list, cols):
    data_json = list()
    for row in data_list:
        data_json.append({
            'ci': row[cols[0]],
            'first_name': row[cols[1]],
            'last_name': row[cols[2]],
        })
    return data_json