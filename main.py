nomes = []
emails = []
telefones = []
usuarios = []
senhas = []

print("=" * 25)
print(' Olá, seja bem-vindo(a)! ')
print("=" * 25)
while True:
  x = input('''
  Selecione a opção desejada:
  [1] Fazer login.
  [2] Criar uma nova conta.
  [3] Finalizar.
  Aqui:  ''')
  if x == '1':
    #fazer login
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if usuario in usuarios:
      i = usuarios.index(usuario)
      if senha == senhas[i]:
        print('Logado')
        break
      else:
        print('Usuário ou senha inválida!')
    else:
      print('Usuário não registrado!')
          
  elif x == '2':
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    telefone = input('Digite seu telefone: ')
    while True:
      usuario = input('Digite seu nome de usuário: ')
      if usuario in usuarios:
        print('Usuário já existe. Tente um novo usuário!')
      else:
        break
      
    senha = input('Digite sua senha: ')
    nomes.append(nome)
    emails.append(email)
    telefones.append(telefone)
    usuarios.append(usuario)
    senhas.append(senha)
    print('Conta criada com sucesso!')
    
  elif x == '3':
    print('  Volte sempre!')
    break
  else:
    print('Opção inválida. Tente novamente!')