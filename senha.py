import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

senha =  generate_password_hash("Pimenta@123").decode('utf-8')
#senha =  generate_password_hash("123456").decode('utf-8'))

print(senha)