from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization 
                        from genes_small.classification c  """

        cursor.execute(query)

        for row in cursor:
            result.append( row["Localization"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getLoc():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.* 
                            from genes_small.classification c  """

        cursor.execute(query)

        for row in cursor:
            result.append((row["GeneID"], row["Localization"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getInteractions():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i.GeneID1 , i.GeneID2 , i.`Type` as t
                        from genes_small.interactions i   """

        cursor.execute(query)

        for row in cursor:
            result.append((row["GeneID1"], row["GeneID2"], row["t"]))

        cursor.close()
        conn.close()
        return result
