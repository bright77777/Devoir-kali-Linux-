def generate_password_dictionary(first_name, last_name, birth_date, email):
    passwords = []

    # Combinaisons de base avec prénom, nom, et date de naissance
    passwords.append(f"{first_name}{last_name}")
    passwords.append(f"{last_name}{first_name}")
    passwords.append(f"{first_name}{birth_date}")
    passwords.append(f"{last_name}{birth_date}")
    passwords.append(f"{first_name}.{last_name}")
    passwords.append(f"{last_name}.{first_name}")


    # Ajouter l'adresse e-mail
    passwords.append(email.split('@')[0])  # Partie avant le @

    # Retirer les tirets et extraire les chiffres de la date de naissance
    digits = birth_date.replace("-", "")  # Supprimer les tirets
    pairs = [digits[i:i+2] for i in range(0, len(digits), 2)]  # Créer des paires

    # Caractères spéciaux à ajouter
    special_characters = ["!", "@", "#", "$", "&", "%"]

    # Ajouter des variations avec les paires de chiffres et caractères spéciaux
    for pair in pairs:
        passwords.append(f"{first_name}{last_name}{pair}")
        passwords.append(f"{first_name}{pair}")
        passwords.append(f"{last_name}{pair}")
        passwords.append(f"{last_name}{first_name}{pair}")
        passwords.append(f"{first_name}{birth_date}{pair}")
        passwords.append(f"{last_name}{birth_date}{pair}")
        for char in special_characters:
            passwords.append(f"{first_name}{last_name}{pair}{char}")
            passwords.append(f"{first_name}{char}{last_name}{pair}")
            passwords.append(f"{first_name}{birth_date}{pair}{char}")
            passwords.append(f"{first_name}{char}{birth_date}{pair}")
            passwords.append(f"{last_name}{char}{birth_date}{pair}")
            passwords.append(f"{last_name}{char}{first_name}")
            passwords.append(f"{last_name}{char}{first_name}{pair}")
            passwords.append(f"{last_name}{char}{first_name}{birth_date}{pair}")
            passwords.append(f"{last_name}{birth_date}{pair}{char}")
            passwords.append(f"{last_name}{char}{birth_date}{pair}")
            passwords.append(f"{last_name}{birth_date}{pair}{char}")

    return passwords

# Exemple d'utilisation
if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer les informations
    first_name = input("Entrez votre prénom : ")
    last_name = input("Entrez votre nom de famille : ")
    birth_date = input("Entrez votre date de naissance (YYYY-MM-DD) : ")
    email = input("Entrez votre adresse e-mail : ")

    password_dict = generate_password_dictionary(first_name, last_name, birth_date, email)
    
    # Afficher le dictionnaire généré
    print("\nDictionnaire de mots de passe généré :")
    for pwd in password_dict:
        print(pwd)