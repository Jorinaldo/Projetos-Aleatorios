from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="pt", target="en")

texto = "Fala Pessoal: Meu nome e jorinaldo sou Analista de Dados e falo portugues"

traducao = tradutor.translate(texto)
print(traducao)