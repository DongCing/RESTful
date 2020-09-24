# RESTful

-- REST是Representational State Transfer三个单词的缩写

-- 它代表着分布式服务的架构风格

-- 每一个URI代表一种资源

-- 客户端和服务器之间，传递这种资源的某种表现层

-- 客户端通过HTTP动词，对服务端资源进行操作，实现”表现层状态转换“

- GET（SELECT）：从服务器取出资源
- POST（CREATE or UPDATE）：在服务器创建资源或更新资源
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）
- ELETE（DELETE）：从服务器删除资源
-- 如果你的api想被称为restful api，只要遵循其规定的约束即可
