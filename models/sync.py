from models import Model


class Sync(Model):
    def __init__(self, app):
        Model.__init__(self, app)

    def get_data(self):
        query = """SELECT
          (SELECT nome_reduzido
           FROM pessoa
           WHERE grid=h.pessoa) AS nome,
               fs.ts,
               fs.gfid,
          (SELECT last_value
           FROM pgd_fid_seq)-fs.gfid AS atraso,
               fs.ts_preco,
               coalesce(fs.gfid_preco, fs.gfid) AS gfid_preco
        FROM pgd_flow_sync fs
        JOIN pgd_hosts h ON (fs.sid=h.sid)
        WHERE fs.sid >= 0
        ORDER BY fs.gfid DESC,
                 fs.sid
                """
        result = self.db.get(query)
        return result
