import psycopg
from psycopg_pool import ConnectionPool

class PG:

    def __init__(self):

        self.credentials=(
            "host=aws-1-ap-southeast-1.pooler.supabase.com "
            "dbname=postgres "
            "user=postgres.bdhkjrpezlexaehjnqda "
            "password=U1ky5JPzTj37oqWB "
            "port=5432"
        )

        # setting like min_size,max_size,timeout 
        #Optional
        self.pool=ConnectionPool(
            conninfo=self.credentials,
            min_size=1,
            max_size=5,
            timeout=300,
            open=True
        )
    def pg_query(self,query,params=()):
        #should execute our query  and return
        #any results
        with self.pool.connection() as conn:
             with conn.cursor() as cur:
                  cur.execute(query,params )
                  result=None
                  try:
                      result=cur.fetchall()
                  except Exception:
                      pass
                  conn.commit()
                  return result    

 