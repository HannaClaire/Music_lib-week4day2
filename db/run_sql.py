import psycopg2
import psycopg2.extras as ext
# this file will run any query


def run_sql(sql, values=None):
    conn = None  # connection
    results = []
    try:
        conn = psycopg2.connect(dbname='music_library')
        # ------- we use this because in the real world the databases are huge
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        # ok for us(because small amount), but not for the real world.
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Hey, we messed up!:", error)
    finally:
        if conn is not None:
            conn.close()

    # return some data
    # in python form
        return results
