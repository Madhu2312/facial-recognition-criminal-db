import pymysql

def insertData(data):
    rowId = 0

    # Updated connection with correct password
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="2312",  # Updated MySQL password
        database="criminaldb"
    )
    
    cursor = db.cursor()
    print("Database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
             data["Nationality"], data["Religion"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("Data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")

    db.close()
    print("Connection closed")
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    # Updated connection with correct password
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="2312",  # Updated MySQL password
        database="criminaldb"
    )

    cursor = db.cursor()
    print("Database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'" % name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            id = result[0]
            crim_data = {
                "Name": result[1],
                "Father's Name": result[2],
                "Mother's Name": result[3],
                "Gender": result[4],
                "DOB(yyyy-mm-dd)": result[5],
                "Blood Group": result[6],
                "Identification Mark": result[7],
                "Nationality": result[8],
                "Religion": result[9],
                "Crimes Done": result[10]
            }
            print("Data retrieved")
        else:
            print("No record found for the given name")

    except Exception as e:
        print("Error: Unable to fetch data", e)

    db.close()
    print("Connection closed")

    return (id, crim_data)
