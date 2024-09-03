import json 

with open("dados.json", encoding='utf-8') as lista_faturamento:
    dados = json.load(lista_faturamento)
    
faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_faturamento = sum(faturamentos) / len(faturamentos)

quantidade_dias_acima_media = sum(1 for valor in faturamentos if valor > media_faturamento)

print(f"Menor valor de faturamento do mês: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento do mês: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {quantidade_dias_acima_media}")