from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as loc 
from classification c
order by c.Localization"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["loc"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c1.Localization as v1 ,c2.Localization as v2, count(distinct i.`Type`) as peso
from interactions i ,classification c1, classification c2
where i.GeneID1 =c1.GeneID and i.GeneID2 =c2.GeneID 
and c1.Localization !=c2.Localization 
group by c1.Localization ,c2.Localization """

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result