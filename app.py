import os 

restaurants = ["Sushirus", "Nanova Pizza"]



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
    print("3. Ativar restaurante ")
    print("4. Sair\n ")

def end_app():
    show_subtitle("Finalizar App")
   
def return_menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()    

def show_subtitle(text):
    os.system("clear")
    print(text)
    print()

def invalid_option():
    print("Opção inválida!\n")
    return_menu()

def register_new_restaurant():
    os.system("clear")
    show_subtitle("Cadastro de novos restaurantes")
    restaurant_name = input("Digite o nome do restaurante que você deseja cadastrar: ")
    restaurants.append(restaurant_name)
    print(f"O restaurante {restaurant_name} foi cadastrado com sucesso! ")
    return_menu()

def list_restaurant():
    show_subtitle("Listando restaurantes ")
    
    for restaurant in restaurants:
        print(f"- {restaurant}")
    return_menu()

def choose_option():
    try:
        chosen_option = int(input("Escolha uma opção: "))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurant()
        elif chosen_option == 3:
            print("Ativar restaurante")
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