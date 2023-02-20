from flask import Flask, render_template

app = Flask(__name__)

#POSTS MOCK
#MOCK sao substitutos para se iniciar um desenvolvimento
#sem a necessidade de se criar todo o banco de dados, ou seja, usa-se substitutos temporarios para teste
posts =  [
    {
        "title" : "Post 1",
        "text" : "My first post"
    },
    {
        "title" : "Post 2",
        "text" : "My seccond post"
    }

]

@app.route('/')

def exibir_entradas():
    return render_template("exibir_entradas.html")
