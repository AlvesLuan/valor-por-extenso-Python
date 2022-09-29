from num2words import num2words

def NumeroPorExtenso(valor):
    if valor.find(',')!=-1:
        valor = valor.split(',')
        valorReais = int(valor[0])
        ValorCentavos = int(valor[1])
        #print (valor) 
        #Se o find encontrar uma virgula (,) no valor inserido, eu Separo o valor em duas variaveis (valorReais e ValorCentavos), uma sendo tudo que está antes da virgula e outra sendo tudo depois.

      
    else:
        valorReais = int(valor)
        ValorCentavos = 0    
        #Se nao encontrar uma virgula, atribui zero a variavel valorCentavos para poder printar apenas os reais.

      
    if valorReais == 1:
        complemento1 = ' real'
    else:
        complemento1 = ' reais'
    #Se o valor for maior que 1 ele se torna plural(reais).
        
    if ValorCentavos == 1:
        complemento2 = ' centavo'
    else:
        complemento2 = ' centavos'
    #mesma logica de cima.

      
    textoReais = ''
    if valorReais > 0:
        textoReais = num2words(valorReais,lang='pt_BR') + str(complemento1)
    else:
        textoReais = ''
    #Se o valor em reais for zero, ele nao informa (pra nao ocorrer o erro de 0 reais e xx centavos).

      
    if ValorCentavos > 0:
        textoCentavos = num2words(ValorCentavos,lang='pt_BR') + str(complemento2) 
    else: 
        textoCentavos = ''
    #mesma logica de cima, para evitar de informar "xx reais e 0 centavos".

      
    if (valorReais > 0 and ValorCentavos > 0):
        valorConcatenado = textoReais + ' e ' + textoCentavos
        #Se ambos valores nao forem zero ele informa os reais e os centavos.
      
    else:
        valorConcatenado = textoReais + textoCentavos
        #se tiver um zero ou algum valor oculto ele apenas nao informa ;) 
      
    print (valorConcatenado)
    return


valor = str(input("Digite uma quantia em reais: "))
NumeroPorExtenso(valor)

