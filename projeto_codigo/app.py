import os 

restaurants = [{"nome":"Labele","categoria":"Italiana","ativo": False},
               {"nome":"Sushirus","categoria":"Japonesa","ativo": True},
               {"nome":"Navona","categoria":"pizzaria","ativo": False}]



def display_program_name():
    print("""

░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░███╗░░██╗██╗░░░██╗   ██████╗░███████╗░██████╗░██╗░██████╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗████╗░██║╚██╗░██╔╝   ██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝███████║██╔██╗██║░╚████╔╝░   ██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██║██║╚████║░░╚██╔╝░░   ██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║░╚███║░░░██║░░░   ██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░   ╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

""")

def display_options():
    print("1. Cadastrar restaurante ")
    print("2. Listar restaurante ")
    print("3. Alternar estado do restaurante ")
    print("4. Sair\n ")

def end_app():
    
    show_subtitle("Finalizar App")
   
def return_menu():
    
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()    

def show_subtitle(text):
    
    os.system("clear")
    line = "*" * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def invalid_option():
    
    print("Opção inválida!\n")
    return_menu()

def register_new_restaurant():
    
    """ Essa função cadastra um novo restaurant 
    
        Inputs: Nome do restaurant; categoria
        
        Output: Add restaurante a lista de restaurantes
    
    """

    show_subtitle("Cadastro de novos restaurantes")
    restaurant_name = input("Digite o nome do restaurante que você deseja cadastrar: ")
    category = input(f"Digite o nome da categoria do restaurant {restaurant_name}: ")
    restaurant_details = {"nome" :restaurant_name, "categoria": category, "ativo": False}
    restaurants.append(restaurant_details)

    print(f"O restaurante {restaurant_name} foi cadastrado com sucesso! ")
    
    return_menu()

def list_restaurants():
    
    show_subtitle("Listando restaurantes ")
    
    print(f"{"Nome do restautaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n")
    for restaurant in restaurants:
        name_restaurant = restaurant ["nome"]
        category = restaurant ["categoria"]
        active = "Ativado" if restaurant ["ativo"] else "Desativado"
        print(f"- {name_restaurant.ljust(20)} | {category.ljust(20)} | {active}")
    
    return_menu()

def toggle_restaurant_status():
    
    show_subtitle("Alternando estado do restaurante")
    name_restaurant = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurant_found = False

    for restaurant in restaurants:
        if name_restaurant == restaurant["nome"]:
            restaurant_found = True
            restaurant["ativo"] = not restaurant["ativo"]
            message = f"o restaurante {name_restaurant} foi ativado com sucesso" if restaurant["ativo"] else f"O restaurante {name_restaurant} foi desativado com sucesso"
            print(message)
    
    if not restaurant_found:
        print("O restaurante não foi encontrado, verifique se digitou certo")

    return_menu()

def choose_option():
    
    try:
        chosen_option = int(input("Escolha uma opção: "))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            toggle_restaurant_status()
        elif chosen_option == 4:
            end_app()
        else: 
            invalid_option()
    except:
        invalid_option()

def main():
    os.system("clear")
    display_program_name()
    display_options()
    choose_option()

if __name__ == "__main__":
    main()