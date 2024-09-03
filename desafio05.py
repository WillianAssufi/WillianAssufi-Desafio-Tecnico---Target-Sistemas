def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

def main():
    string_original = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string_original)
    print(f"A string invertida é: {string_invertida}")
    
if __name__ == "__main__":
    main()