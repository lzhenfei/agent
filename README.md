
# demo.py
调用openai
1. 通过openai开放平台注册api key
https://platform.openai.com/home
2. 安装openapi
pip3 install openai

# RAG工作原理
检索、生成、增强
1. 知识库文件embedding，存入向量数据库
2. 对搜索词embeding，检索向量数据库，通过cos余弦相似度，欧式距离，点积计算向量相似度
cos余弦相似度，计算两个向量之间的夹角
欧式距离，计算两个向量终点之间的距离
点积
3. 从向量数据库中搜索出相似度最高的topn条数据（n可配置）
4. 对搜索结果进行重排序
5. 将重排后的数据加搜索词送给大模型