import mysql.connector

banco = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="yuri"
)

cursor = banco.cursor()

#comando_sql = "SELECT * FROM pessoas where idade<40"
#comando_sql ="deleter * from pessoas where idade >40"
cursor.execute(comando_sql)

valores_lidos = cursor.fetchall()

print(valores_lidos)


# comando_SQL="INSERT INTO pessoas(nome,idade,email) VALUES(%s,%s,%s)"
# dados = ("Sakura","41","sakura.icapui@hotmail.com")
# cursor.execute(comando_SQL,dados)



# banco.commit()



# link para abrir no navegador http://localhost/phpmyadmin/


#cursor.execute("CREATE TABLE pessoas(nome VARCHAR(255),idade INT(3),email VARCHAR(255))")