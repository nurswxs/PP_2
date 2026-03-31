import psycopg2
import csv
from config import DB_CONFIG


class PhoneBook:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name TEXT,
            phone TEXT UNIQUE
        )
        """)
        self.conn.commit()

    def insert_from_csv(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    name, phone = row[0], row[1]
                    try:
                        self.cur.execute(
                            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                            (name, phone)
                        )
                    except:
                        self.conn.rollback()

                self.conn.commit()
                print("CSV импортталды")

        except FileNotFoundError:
            print("Файл табылмады")

    def insert_console(self):
        name = input("name: ")
        phone = input("phone: ")

        try:
            self.cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (name, phone)
            )
            self.conn.commit()
        except:
            self.conn.rollback()
            print("Ошибка")

    def show_all(self):
        self.cur.execute("SELECT * FROM contacts")
        for row in self.cur.fetchall():
            print(row)

    def search(self):
        print("1-name 2-phone prefix")
        t = input(">> ")

        if t == "1":
            name = input("name: ")
            self.cur.execute(
                "SELECT * FROM contacts WHERE name ILIKE %s",
                (f"%{name}%",)
            )
        else:
            prefix = input("prefix: ")
            self.cur.execute(
                "SELECT * FROM contacts WHERE phone LIKE %s",
                (prefix + "%",)
            )

        print(self.cur.fetchall())

    def update(self):
        phone = input("enter phone to update: ")

        print("1-name 2-phone")
        t = input(">> ")

        if t == "1":
            new_name = input("new name: ")
            self.cur.execute(
                "UPDATE contacts SET name=%s WHERE phone=%s",
                (new_name, phone)
            )
        else:
            new_phone = input("new phone: ")
            self.cur.execute(
                "UPDATE contacts SET phone=%s WHERE phone=%s",
                (new_phone, phone)
            )

        self.conn.commit()

    def delete(self):
        print("1-name 2-phone")
        t = input(">> ")

        if t == "1":
            name = input("name: ")
            self.cur.execute(
                "DELETE FROM contacts WHERE name=%s",
                (name,)
            )
        else:
            phone = input("phone: ")
            self.cur.execute(
                "DELETE FROM contacts WHERE phone=%s",
                (phone,)
            )

        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


def main():
    pb = PhoneBook()
    pb.create_table()

    while True:
        print("\n1.Add 2.Show 3.Search 4.Update 5.Delete 6.CSV 7.Exit")
        ch = input(">> ")

        if ch == "1":
            pb.insert_console()
        elif ch == "2":
            pb.show_all()
        elif ch == "3":
            pb.search()
        elif ch == "4":
            pb.update()
        elif ch == "5":
            pb.delete()
        elif ch == "6":
            pb.insert_from_csv("contacts.csv")
        elif ch == "7":
            break

    pb.close()


if __name__ == "__main__":
    main()