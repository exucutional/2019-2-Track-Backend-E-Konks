import psycopg2
import random
from datetime import datetime
from faker import Faker

class DBFilling:
    def __init__(self, dbhost: str, dbname: str, dbuser: str, dbpass: str) -> None:
        self.conn = psycopg2.connect(
            f"host='{dbhost}' dbname='{dbname}' user='{dbuser}' password='{dbpass}'")

        self.cur = self.conn.cursor()


    def create_users(self, count: int) -> None:
        fake = Faker()
        for _ in range(count):
            user = fake.profile()
            self.cur.execute("""INSERT INTO 
            users_user(first_name, last_name, username, password, email, is_superuser, is_staff, is_active, date_joined)
            VALUES (%s, %s, %s, %s, %s, false, true, false, '2020-01-01 00:00:00')""",
            (user['name'].split(' ')[0], user['name'].split(' ')[1], user['username'], fake.password(), user['mail']))


    def create_chats(self, count: int, users_count: int) -> None:
        fake = Faker()
        for _ in range(count):
            self.cur.execute("""INSERT INTO 
            chats_chat(topic) VALUES (%s)""", (fake.word(),))


    def create_messages(self, count: int, users_count: int, chats_count: int) -> None:
        fake = Faker()
        for _ in range(count):
            dt = datetime.now()
            self.cur.execute("""INSERT INTO 
            chat_messages_message(chat_id, user_id, content, added_at) VALUES (%s, %s, %s, %s)""",
            (random.randint(1, chats_count), random.randint(40, users_count), fake.text(), dt.strftime("%d-%m-%Y %H:%M:%S")))


    def save(self) -> None:
        self.conn.commit()


if __name__ == "__main__":
    db = DBFilling('localhost', 'chat_db', 'chat', '123')
    db.create_users(100)
    db.create_chats(100, 100)
    db.save()
    db.create_messages(1000, 100, 100)
    db.save()
