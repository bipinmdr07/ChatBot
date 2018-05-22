import sqlite3
import pandas as pd

timeframes = ['2015-01']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    q_size = 0
    a_size = 0

    while cur_length == limit:
        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix, limit), connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)
        
        # with open("./model/train.from", 'a', encoding='utf8') as f:
        #     for content in df['parent'].values:
        #         q_size += 1
        # with open("./model/train.to", 'a', encoding = 'utf8') as f:
        #     for content in df['comment'].values:
        #         a_size += 1
        for content in df['parent'].values:
            q_size += 1

        for content in df['comment'].values:
            a_size += 1

        counter += 1
        if counter % 2 == 0:
            print(counter * limit, 'rows completed so far')
        
    print(q_size, a_size)