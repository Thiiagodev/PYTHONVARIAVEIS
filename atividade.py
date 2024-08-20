nome = "Thiago"
idade = 19
cidade = "Imperatriz MA a melhoriznha que ta tendo"
contador = 0

def informacoes_pessoais():
    print(f"Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")

def incrementar_contador():
    global contador
    contador += 1
    print(f"Contador atualizado: {contador}")
    
    mensagem = "Contador foi adicionado!"
    print(mensagem)


informacoes_pessoais()
incrementar_contador()
