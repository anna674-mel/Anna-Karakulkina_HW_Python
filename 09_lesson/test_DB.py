import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных
DB_URL = "postgresql://postgres:w64Anplka7@localhost:5432/QA_Sky"

engine = create_engine(DB_URL)
metadata = MetaData()

# Описание таблицы users
users = Table(
    "users", metadata,
    Column("user_id", Integer, primary_key=True),
    Column("subject_id", Integer, nullable=False),
    Column("user_email", String, nullable=False)
)

Session = sessionmaker(bind=engine)


@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()


def test_add_user(session):
    userID = 86000
    email = "test_made@up.info"
    # Добавление нового пользователя
    ins = insert(users).values(user_id=userID, subject_id=100, user_email=email)
    session.execute(ins)
    session.commit()

    # Проверка, что пользователь добавлен
    sel = select(users).where(users.c.user_id == userID)
    result = session.execute(sel).fetchone()
    # assert result is not None
    assert result.user_email == email

    # Удаляем добавленного пользователя для чистоты теста
    del_stmt = delete(users).where(users.c.user_id == userID)
    session.execute(del_stmt)
    session.commit()


def test_update_user_email(session):
    userID = 86001
    email_new = "new_email@made_up.info"
    # Вставляем пользователя для обновления
    ins = insert(users).values(user_id=userID, subject_id=102, user_email="old_email@made_up.info")
    session.execute(ins)
    session.commit()

    # Обновляем email пользователя
    upd = update(users).where(users.c.user_id == userID).values(user_email=email_new)
    session.execute(upd)
    session.commit()

    # Проверяем обновление
    sel = select(users).where(users.c.user_id == userID)
    result = session.execute(sel).fetchone()
    assert result.user_email == email_new

    # Удаляем тестового пользователя
    del_stmt = delete(users).where(users.c.user_id == userID)
    session.execute(del_stmt)
    session.commit()


def test_delete_user(session):
    userID = 86002
    
    # Добавляем пользователя для удаления
    ins = insert(users).values(user_id=userID, subject_id=103, user_email="delete@made_up.info")
    session.execute(ins)
    session.commit()

    # Удаляем пользователя
    del_stmt = delete(users).where(users.c.user_id == 10002)
    result = session.execute(del_stmt)
    session.commit()

    # Проверяем, что пользователя нет
    sel = select(users).where(users.c.user_id == 10002)
    result = session.execute(sel).fetchone()
    assert result is None 