# mabi-enchant-translate


## Objective
1. Using langchain and related tech, translate a query into a SQL query with defined MRO.


## Technique
Query Construction: 
We would like to interact with database using domain-specific language, such as SQL or mongo.


## Timeline
- [x] Nov-20: Complete a notebook that can translate a sentence into SQL query in an appropreiate SQL grammar
- [ ] Nov-17: Build a fastAPI server to serve as a microservice
- [ ] Nov-17: Containerize it
- [ ] Nov-18: Write a helm chat and deploy it on docker desktop


## Reference

https://omershahzad.medium.com/agent-for-mongodb-langchain-ccf69913a11a

https://github.com/langchain-ai/langchain/blob/master/cookbook/retrieval_in_sql.ipynb?ref=blog.langchain.dev
https://khadkechetan.medium.com/natural-language-to-sql-query-using-an-open-source-llm-6b4b91a5519a

https://arxiv.org/pdf/2408.05109

https://www.uber.com/en-GB/blog/query-gpt/

https://medium.com/@marvin_thompson/how-to-use-langchain-to-build-a-text-to-sql-solution-54a173f312a5

https://github.com/langchain-ai/langchain/discussions/19973

https://www.llamaindex.ai/blog/easily-finetune-llama-2-for-your-text-to-sql-applications-ecd53640e10d

***
https://github.com/langchain-ai/langchain/blob/master/cookbook/LLaMA2_sql_chat.ipynb

