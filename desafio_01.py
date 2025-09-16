contact_list =[]


def add_contact(new_contact):
    contact_list.append(new_contact)
    print("\nContato adicionado com sucesso!")

def remove_contact():
    return ''

def show_contacts():
    for contact in contact_list:
        print(f"Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}, Favorito: {'\U00002b50' if contact['favorite'] else '-'}")
    return ''

def toggle_favorite_status():
    return ''

while True:
    print('1 - Adicionar contato')
    print('2 - Remover contato')
    print('3 - Favoritar/Desfavoritar contato')
    print('4 - Listar contatos')
    print('5 - Listar favoritos')
    print('6 - Sair')

    option = int(input('Escolha uma opção: '))

    if option == 1:
        name= input("Digite o nome do contato: ")
        phone= input("Digite o telefone do contato: ")
        email= input("Digite o email do contato: ")
        favorite= input("O contato é favorito? (s/n): ").lower() == 's'
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite
        }    
        add_contact(new_contact)
    elif option == 2:
        remove_contact()
    elif option == 3:
        toggle_favorite_status()
    elif option == 4:
        show_contacts()
        print()
    elif option == 5:
        favorites = [contact for contact in concat_list if contact.get('favorite')]
        print(favorites)
    elif option == 6:
        break
    else:
        print('Opção inválida, tente novamente.')
    