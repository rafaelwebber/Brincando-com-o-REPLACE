'''9) Elabore um programa que leia uma frase, uma palavra antiga e uma palavra
nova. O programa deve exibir uma string contendo a frase original e outra com
a ocorrência da palavra antiga substituída pela palavra nova.
Exemplo:
Frase: “Quem parte e reparte fica com a maior parte”
Palavra antiga: “parte”
 Palavra nova: “parcela”
Resultado a ser impresso no programa : “Quem parcela
e reparcela fica com a maior parcela”
Dica: use replace'''

a= input("Elabore uma frase contendo a palavra (terra): ")

print(f"A frase original é: \n {a} \n \n A nova frase fica: \n {a.replace("terra", "manteiga")}")