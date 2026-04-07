from connect import connect


def search_contacts(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def upsert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    conn.close()
    print("Upsert done!")


def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    conn.close()
    print("Deleted!")


def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    get_paginated(5, 0)