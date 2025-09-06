from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv
from sqlalchemy.exc import ProgrammingError

load_dotenv()


#llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"])
llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.environ["GOOGLE_API_KEY"])
#"
print(llm("write few lines on Generative AI"))

#from langchain_community.utilities import SQLDatabase


db_user = "root"
db_password = "root123"
db_host = "localhost"
db_name = "retail_sales_db"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)


print(db.table_info)

#Convert question to SQL query

chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many customers are there"})
print(response)

cleaned_query = response.strip('```sql\n').strip('\n```')
print(cleaned_query)

# Execute the cleaned query
result = db.run(cleaned_query)
print(result)
#
# chain = create_sql_query_chain(llm, db)
# def execute_query(question):
#     try:
#         # Generate SQL query from question
#         response = chain.invoke({"question": question})
#         print(response)
#         print("###################################################")
#         # Strip the formatting markers from the response
#         cleaned_query = response.strip('```sql\n').strip('\n```')
#         print(cleaned_query)
#         print("###################################################")
#         # Execute the cleaned query
#         result = db.run(cleaned_query)
#         print("###################################################")
#         # Display the result
#         print(result)
#     except ProgrammingError as e:
#         print(f"An error occurred: {e}")
#
#
#
#
# q1 = "How many unique customers are there for each product category"
# execute_query(q1)
#
#
# q2 = "Calculate total sales amount per product category:"
# execute_query(q2)
#
#
# q3 = "calculates the average age of customers grouped by gender."
# execute_query(q3)
#
# q4 = "identify the top spending customers based on their total amount spent."
# execute_query(q4)
#
# q5 = "counts the number of transactions made each month."
# execute_query(q5)
#
#
# q6 = "calculates the total sales amount and average price per unit for each product category."
# execute_query(q6)