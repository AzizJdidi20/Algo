def considérer_phrase(phrase):
    longeur_phrase=0
    nombre_mots=0
    nombre_voyelles=0

    for char in phrase:
        longeur_phrase += 1
        if char.isalpha():
            if char ==' ':
                nombre_mots += 1
        if char.lower()in['a','e','i','o','u']:
            nombre_voyelles += 1
    nombre_mots += 1

    print("longeur de la phrase :" , longeur_phrase)
    print("nombre de mots :" , nombre_mots)
    print("nombre de voyelles :" , nombre_voyelles)
