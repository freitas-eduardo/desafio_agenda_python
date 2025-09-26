contact_list =[]

def add_contact(new_contact):
    contact_list.append(new_contact)
    print("\nContato adicionado com sucesso!")

def remove_contact(index):
    # Adjust for 1-based user input if you decide to print 1-based indices, 
    # but based on the main loop's current use of an integer index, 
    # we'll assume a 0-based index for now or rely on the user to input 0-based.
    # A safer approach for a user-facing program would be to list contacts with 
    # 1-based indices and convert back.
    if 0 <= index < len(contact_list):
        removed_contact = contact_list.pop(index)
        print(f"\nContato {removed_contact['name']} removido com sucesso!") 
    else:
        print("\nÍndice inválido. Nenhum contato foi removido.")
    return ''

def show_contacts(list_to_show=None):
    if list_to_show is None:
        list_to_show = contact_list
        
    if not list_to_show:
        print("\nA lista de contatos está vazia.")
        return ''

    print("\n--- Lista de Contatos ---")
    for i, contact in enumerate(list_to_show):
        # Displaying index for user interaction
        print(f"[{i}] Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}, Favorito: {'\U00002b50' if contact['favorite'] else '-'}")
    print("-------------------------")
    return ''

# --- New Function: Edit Contact ---
def edit_contact(index):
    if 0 <= index < len(contact_list):
        contact = contact_list[index]
        print(f"\nEditando contato: {contact['name']}")
        print("Deixe em branco para manter o valor atual.")
        
        # New name
        new_name = input(f"Novo nome (Atual: {contact['name']}): ")
        if new_name:
            contact['name'] = new_name
            
        # New phone
        new_phone = input(f"Novo telefone (Atual: {contact['phone']}): ")
        if new_phone:
            contact['phone'] = new_phone
            
        # New email
        new_email = input(f"Novo email (Atual: {contact['email']}): ")
        if new_email:
            contact['email'] = new_email
            
        print(f"\nContato {contact['name']} atualizado com sucesso!")
    else:
        print("\nÍndice inválido. Nenhum contato foi editado.")
    return ''

# --- Implemented Function: Toggle Favorite Status ---
def toggle_favorite_status(index):
    if 0 <= index < len(contact_list):
        contact = contact_list[index]
        # Toggle the boolean value
        contact['favorite'] = not contact['favorite']
        status = "favorito" if contact['favorite'] else "desfavoritado"
        print(f"\nStatus de favorito do contato {contact['name']} alterado para: {status}!")
    else:
        print("\nÍndice inválido. Nenhum contato foi alterado.")
    return ''

while True:
    print('\n================================')
    print('1 - Adicionar contato')
    print('2 - Remover contato')
    print('3 - Favoritar/Desfavoritar contato')
    print('4 - Listar contatos')
    print('5 - Listar favoritos')
    print('6 - Editar contato') # New Option
    print('7 - Sair') # Updated Exit Option
    print('================================')
    
    try:
        option = int(input('Escolha uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Por favor, digite um número.')
        continue

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
        show_contacts() # Show contacts with indices first
        try:
            index = int(input("Digite o índice do contato a ser removido: "))
            remove_contact(index)
        except ValueError:
            print("\nÍndice inválido. Por favor, digite um número inteiro.")
            
    elif option == 3:
        show_contacts() # Show contacts with indices first
        try:
            index = int(input("Digite o índice do contato para alterar o status de favorito: "))
            toggle_favorite_status(index)
        except ValueError:
            print("\nÍndice inválido. Por favor, digite um número inteiro.")
            
    elif option == 4:
        show_contacts()
        
    elif option == 5:
        # Filter for favorites and pass the list to show_contacts
        favorites = [contact for contact in contact_list if contact.get('favorite')]
        show_contacts(favorites)
        
    # --- New Option for Editing Contact ---
    elif option == 6:
        show_contacts() # Show contacts with indices first
        try:
            index = int(input("Digite o índice do contato a ser editado: "))
            edit_contact(index)
        except ValueError:
            print("\nÍndice inválido. Por favor, digite um número inteiro.")
            
    # --- Updated Exit Option ---
    elif option == 7:
        print("\nSaindo do programa. Até mais! 👋")
        break
        
    else:
        print('\nOpção inválida, tente novamente.')