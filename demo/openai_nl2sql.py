"""
https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/

This one is the example that we can buidl a simple chain to convert questions into query.

However, we need to have the access to the database.

A better solution would be to like we just provide the database schemas.

Usage:
    $ cd  <root directory of the project>
    $ python demo/openai_nl2sql.py
"""
# ————————————————————
import os
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv


if __name__ == "__main__":

    load_dotenv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, "Chinook.db")

    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    print(db.dialect)
    print(db.get_usable_table_names())
    db.run("SELECT * FROM Artist LIMIT 10;")

    # ————————————————————
    from langchain.chains import create_sql_query_chain
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": "How many employees are there"})
    print(response)

    # ————————————————————