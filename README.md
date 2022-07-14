# Blog: fast-api
first fastAPI projects,
study python fastapi from [youtube-tutorials](https://www.youtube.com/watch?v=7t2alSnE2-I)

## Todo/Question
- change db from sqllite to mysql
- design pattern: In header or in parameter
- continue study [RestAPI Design](https://www.1point3acres.com/bbs/thread-909427-1-1.html)
- confused about how exatly use [OAuthtoken](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Solution
- with response model
- sql related Question (query Question e.g: .all() . first )
-

## Resources
- python database related [SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/query.html?highlight=query+filter#sqlalchemy.orm.Query.filter)
- office fastAPI doc [fastAPI](https://fastapi.tiangolo.com/)
- local swagger docs/ openAPI: http://127.0.0.1:8000/docs
- office doc database section [SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- personal python note [google-docs](https://docs.google.com/document/d/17jJSKdm6a83o5O2lo61h4JgyYeN1fCdzdHU8_iRxKOI/edit#heading=h.z95qcn10mhm)

## Installation
IDE: using intellij with python pugin
DB tools: TablePlus
```sh
pip3 install -r requirement.txt
```

generate JWT tokens
```sh
openssl rand -hex 32
```

## Development

```sh
uvicorn blog.main:app --reload
```


## RESTAPI-Rule
[original docs](https://www.1point3acres.com/bbs/thread-909427-1-1.html)
come back continue study

Design Sample:
- GET /users 获取所有用户
- GET /users/1234 获取ID为1234的用户
- POST /users **创建**一个新用户
- PUT /users/1234 **更新**ID为1234的用户
- PATCH /users/1234 更新ID为1234的用户的**部分内容**
- DELETE /users/1234 删除ID为1234的用户


如果要设计一个资源拥有另外一个资源的情况的API，例如，设计一个包含用户（users）和用户的评论（comments）的 API 可以采用这样的形式：
- GET /users/1234/comments 获取用户ID为1234的**所有评论**
- GET /users/1234/comments/1 获取用户ID为1234的评论ID为1的**单个评论**
- DELETE /users/1234/messages/1 删除用户评论ID为1，属于用户1234的单个评论

or option 2: using query parameter
- /comments?user_id=1234

if operation is not CRUD?
- 将这些操作变成一个资源的属性，比如 disable 一个 user，可以在 user 里面加一个 disabled 的属性，
可以设计一个 API 使用 PATCH /users/1234 将 disabled 设置成 true 即可。
- 将这个操作看成某个资源的附属资源，比如GitHub的Star a gist API ，
它把star操作放在这个资源的后面，看上去好像是一个附属资源：
  - PUT /gists/:id/star
  - DELETE /gists/:id/star


In header or in parameter
- Headers carry meta info, parameters carry actual data.


response code:
- 200 OK 用于返回 GET, PUT, PATCH 或 DELETE 的操作。有使用也用来返回没有创建数据的 POST 操作；
- 201 Created 用来返回 POST 操作并且成功创建了数据的情况。新创建的数据资源的链接应该放在location中返回，具体参见这里 ；
- 204 No Content 用来返回一次成功的请求，但是该请求返回的 body 为空的情况，如 DELETE 请求；
- 304 Not Modified 表示缓存没有失效，和上次的请求相比，没有新的内容；
- 400 Bad Request 用于返回 API 参数不正确的情况，比如传入的 JSON 格式错误无法解析等；
- 401 Unauthorized 用于表示请求等 API 缺少身份验证信息；
- 403 Forbidden 用于表示该资源不允许特定用户访问；
- 404 Not Found 请求一个不存在的资源；
- 429 Too Many Requests 请求过于频繁，可以用在客户端调用过于频繁的情况。
- more return info in Http body:
  {
  "error": {
  "message":"Message describing the error",
  "type":"OAuthException",
  "code":190,
  "error_subcode":460,
  "error_user_title":"A title",
  "error_user_msg":"A message",
  "fbtrace_id":"EJplcsCHuLu"
  }
  }

Rules:
- path(/users): users use 复数


