from peewee import *


db = SqliteDatabase('distances.db')


class Data(Model):
    serialNumber = AutoField(PrimaryKeyField)
    distance = DoubleField()
    sentiment_type = TextField()

    class Meta:
        database = db


# db.connect()
# db.create_tables([Data])
# Data.add_index(SQL('CREATE INDEX idx on Data(distance);'))


def saveData(ref_distance,  type):
    data = Data(distance=ref_distance, sentiment_type=type)
    data.save()
    db.close()


def search(ref_distance):
    # Data.distance > ref_distance-0.00000000000000000000001 and Data.distance < ref_distance+0.0000000000000000000001
    lb, ub = 0.9995*ref_distance, 1.0005*ref_distance
    print("Using LB={0} and UB={1}".format(lb, ub))

    # sql = 'select (d.distance - %s) AS dist from "data" d where d.distance BETWEEN 0.999 * %s AND 1.001 * %s order by 1 desc'

    # cur = db.execute_sql(sql, (ref_distance, ref_distance, ref_distance))
    # for idx, row in cur.fetchall():
    #     print("Row-{0} = {1}".format(idx, row[0]))

    query = Data.select(
        Data.distance, (Data.distance-ref_distance).alias("dist")).where(
        Data.distance.between(lb, ub)).order_by()

    print("*******")
    for y in query:
        print("distance is", y.distance)
        print("difference is", y.dist)

    diff_array = []
    for x in query:
        diff_array.append(abs(x.dist))
    diff_array.sort()

    # min_dist = ref_distance
    tp = 0
    sentiment_type_of_this_sentence = "None"
    print(len(query))
    if(query.exists()):
        tp = query[0].distance
        #tp = distance_arr[0]
        print("Distance = {0}. Diff={1}".format(tp, diff_array[0]))
        # for i in query:
        #     if (i.distance - ref_distance < min_dist):
        #         min_dist = (i.distance - ref_distance)
        #         tp = i.distance
        x = Data.select().where(Data.distance == tp)
        print(len(x))
        for i in x:
            sentiment_type_of_this_sentence = i.sentiment_type
    else:
        print("**** No results found withing the distance range!")

    # sentiment_type_of_this_sentence = "unknown"

    return sentiment_type_of_this_sentence
