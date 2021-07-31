while True:
    sexo = str(input('Digite seu sexo: [Masculino/Feminio] ')).strip().lower()
    if sexo == 'masculino' or sexo == 'homem':
        print(f'Sexo Masculino cadastrado!')
        break
    elif sexo == 'feminino' or sexo == 'mulher':
        print(f'Sexo Feminino Cadastrado')
        break
    else:
        print('Opção Inválida, Digite novamente...')
