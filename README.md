# AI meets Databases
🔹 Turning raw data into intelligent insights — with just one question!

A Retail Sales Database was created in MySQL Workbench with customer transactions, product categories, prices, and total amounts.
Sample data was inserted to simulate sales records.

An AI-powered application was then built using:

LangChain to generate SQL queries from natural language

Google Gemini as the LLM

Streamlit for the interface

✨ Example:
Question → “How many customers are there?”
The system generated the query:

SELECT COUNT(DISTINCT CustomerID) FROM sales_tb;


and displayed the result instantly.