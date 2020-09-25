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


视图函数

-- FBV

-- function base view

-- CBV

-- class base view

类视图

-- CBV（以下进行了源码分析）

-- 继承自View

-- 注册的时候使用的as_view()

-- 入口

　　-- 不能使用请求方法的名字作为参数的名字

　　-- 只能接受已经存在的属性对应的参数

　　-- 定义了一个view

　　　　-- 创建了一个类视图对象

　　　　-- 保留，拷贝传递进来的属性和参数

　　　　-- 调用dispatch方法（核心）

　　　　　　-- 分发

　　　　　　-- 如果请求方法在我们的允许的列表中

　　　　　　　　-- 从自己这个对象中获取请求方法名字小写对应的属性，如果没有找到，会给一个默认http_method_not_allowded

　　　　　　-- 如果请求方法不在我们允许的列表中，直接就是http_method_not_allowed

　　　　　　-- 之后将参数传递，调用函数

-- 默认实现了options

　　-- 获取接口信息，可以获取接口都允许什么请求

-- 简化版流程

　　-- as_view

　　-- dispatch

　　-- 调用实现请求方法对应的函数名
