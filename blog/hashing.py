from passlib.context import CryptContext

#Encrypted/hashed the password
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_ctx.hash(password)
