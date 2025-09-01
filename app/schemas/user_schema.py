from pydantic import BaseModel, EmailStr, field_validator, model_validator

class UserBase(BaseModel):
    username: str
    email: EmailStr 

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True





class User(BaseModel):
    username: str

    @field_validator('username') # This is for individual field
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be length of greaterthan 4 cha")
        return v  # If everything goes well return v
      

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after") # It will run after individual field val
    def password_match(clas, values):
        if values.password  != values.confirm_password:
            raise ValueError("Password do not match")
        return values
    

# Computed pydantic: It will be calculated on the go
from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

# Advance Pydantic Validaton: Multiple field validation
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name') #Runs one after other as loop
    def names_must_be_capitalize(cls, v ):
        if not v.istitle():
            raise ValueError('Names must be Capitalize')
        return v
    

# DATA TRANSFORMATIONS:
class Users_(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower().strip()
    

# class Products(BaseModel):
#     price: str

    # @field_validator('price', mode="before")



# NESTED MODELS:
from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class UserS(BaseModel):
    id:int
    name: str
    address: Address # Above address

user_data = {
    "id": 1,
    "street": "Hitesh",
    "address": {
        "street": "321 something",
        "city": "Paris",
        "postal_code": "20002"
    }
}

user = User(**user_data)
print(user)



# RECURSIVE MODELS
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild() #It is required for Self Referencing Model

comment = Comment(
    id= 1,
    content = "First Comment",
    replies = [
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply3", replies=[
            Comment(id=4, content="nested reply")
        ]),
    ] 
)