from cpf_cnpj import Documento

exemplo = "47886522000104"
exemplo_02 = "07222914340"

documento = Documento.cria_documento(exemplo)
documento_02 = Documento.cria_documento(exemplo_02)


print(documento)
print(documento_02)