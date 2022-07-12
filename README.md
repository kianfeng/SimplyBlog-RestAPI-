# Blog: fast-api
first fastAPI projects,
study python fastapi from [youtube-tutorials](https://www.youtube.com/watch?v=7t2alSnE2-I)

## Todo/Question
- change db from sqllite to mysql
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
pip install -r requirement.txt
```

generate JWT tokens
```sh
openssl rand -hex 32
```

## Development

```sh
uvicorn blog.main:app --reload
```






