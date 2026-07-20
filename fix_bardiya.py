from db import get_db_connection

def fix_bardiya_search():
    conn = get_db_connection()
    cursor = conn.cursor()

    # We append the alternate spelling "Bardiya" to the description so that
    # the LIKE '%bardiya%' query will catch it.
    cursor.execute("""
        UPDATE destinations 
        SET description = CONCAT(description, ' (also spelled Bardiya)') 
        WHERE name = 'Bardia National Park'
    """)
    
    # Also update the package description just in case the user expects 
    # the package to show up directly when searching "bardiya"
    cursor.execute("""
        UPDATE packages 
        SET description = CONCAT(description, ' (also known as Bardiya)') 
        WHERE title LIKE '%Bardia Tiger%'
    """)

    conn.commit()
    print("Successfully added alternate spelling 'Bardiya' to the database entries.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    fix_bardiya_search()
