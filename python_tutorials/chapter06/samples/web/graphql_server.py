import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
from fastapi import FastAPI

@strawberry.type
class Book:
    id: int
    title: str
    author: str
    price: float

books_db = []

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        return books_db

    @strawberry.field
    def book(self, id: int) -> Book:
        return next((book for book in books_db if book.id == id), None)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, id: int, title: str, author: str, price: float) -> Book:
        book = Book(id=id, title=title, author=author, price=price)
        books_db.append(book)
        return book

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)