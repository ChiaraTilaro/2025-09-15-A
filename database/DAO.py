from database.DB_connect import DBConnect
from model.driver import Driver


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(anno1 , anno2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query =  """
        select d.driverId , d.driverRef , d.number , d.code , d.forename , d.surname  , d.nationality , d.url 
from drivers d , results r , races r2 
where d.driverId = r.driverId 
and r.position is not null 
and r2.raceId = r.raceId 
and r2.year >= 2007 and r2.year<=2008
group by d.driverId , d.driverRef , d.number , d.code , d.forename , d.surname , d.dob , d.nationality , d.url 
        """
        cursor.execute(query)

        for row in cursor:
            results.append(Driver(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(anno1 , anno2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
        select r.driverId as driver1 , t.driverid as driver2 , COUNT(distinct r.raceId ) as peso
from results r , constructors c , races r2 ,  (
select r.driverId , c.constructorId , r.raceId 
from results r , constructors c , races r2 
where r.constructorId = c.constructorId 
and r.raceId = r2.raceId 
and r.position is not null
and r2.year >= %s and r2.year <=%s
group by r.driverid , c.constructorId , r.raceId  ) as t
where c.constructorId = t.constructorid 
and r.raceId = t.raceId
and r.constructorId = c.constructorId 
and r.raceId = r2.raceId 
and r.driverId  < t.driverid 
and r2.year >=%s and r2.year<=%s
and r.position is not null
group by r.driverId  , t.driverid
        """

        cursor.execute(query, (anno1 , anno2 , anno1 , anno2))

        for row in cursor:
            results.append((row["driver1"] , row["driver2"] , row["peso"]))

        cursor.close()
        conn.close()
        return results


