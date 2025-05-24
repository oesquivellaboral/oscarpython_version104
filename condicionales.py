print("Condicionales:")

edad = 25
status = (
    "Mayor" if edad >= 18 else 
    "Adolescente" if 13 <= edad < 18 else 
    "Niño"
)
print(status)  # Output: "Mayor"

print("Este resultado no es correcto")