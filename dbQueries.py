from dbConnection import get_db_connection


# Function to insert username and searched keyword in the table 'googlesearchhistoryprime'
def insert_in_db(username, keyword):
    connection = get_db_connection()
    curr = connection.cursor()
    try:
        postgres_insert_query = """INSERT INTO googlesearchhistoryprime (username, keyword) VALUES (%s,%s)"""
        record_to_insert = (username, keyword)
        print("Inserting ->", username, keyword)
        curr.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = curr.rowcount
        print(count, "Record inserted successfully into googlesearchhistoryprime table")

    except Exception as error:
        print("Failed to insert record into googlesearchhistoryprime table", error)

    finally:
        if connection:
            curr.close()
            connection.close()


# A Function to fetch history of keyword searched by a specific username in the table 'googlesearchhistoryprime'
def search_in_db(username, keyword):
    connection = get_db_connection()
    curr = connection.cursor()
    try:
        postgres_search_query = """SELECT * FROM googlesearchhistoryprime WHERE username = %s AND keyword LIKE %s ORDER by ts DESC"""
        pattern = '%' + keyword + '%'
        record_to_insert = (username, pattern)
        print("#Searching ->", username, pattern)
        curr.execute(postgres_search_query, record_to_insert)
        connection.commit()
        result = curr.fetchall()
        res = ""
        for r in result:
            res += r[2] + "\n"
        print("Record fetched successfully from googlesearchhistoryprime table")
        if res != "":
            output = "History for keyword - " + keyword + "\n" + res
            return output
        else:
            return None

    except Exception as error:
        print("Failed to fetch record into googlesearchhistoryprime table", error)

    finally:
        if connection:
            curr.close()
            connection.close()
