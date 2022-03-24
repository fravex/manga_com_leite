from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import BigtableNomes, AnvisaPrincipioativo, DrugbankAnvisa, AnvisaNome, AnvisaNomePrincipioativo, DrugbankInteracao

#LISTA TODOS OS MEDICAMENTOS DA BIGTABLE EM 2 CAMPOS DE BUSCA PARA CONSULTA DE INTERACAO
def lista_medicamentos(request):

    #RECEBE O MEDICAMENTOS SELECIONADOS PELO USUARIO NA REQUISICAO NO BANCO DE DADOS BIGTABLE
    search = request.GET.get('search')
    search1 = request.GET.get('search1')
    if search:
        dados_big_table_1 = BigtableNomes.objects.filter(id=search)
        dados_big_table_2 = BigtableNomes.objects.filter(id=search1)
        
    #VERIFICA O TIPO DE DADO NA BIGTABLE - TIPO 1 DRUGBANK, TIPO 2 ANVISA NOME COMERCIAL E TIPO 3 ANVISA PRINCIPIO ATIVO    
        tipo_dados_big_table_1 = dados_big_table_1.get().tipo_origem
        tipo_dados_big_table_2 = dados_big_table_2.get().tipo_origem

        print('tipo de dados: = ', tipo_dados_big_table_1, tipo_dados_big_table_2)

        if tipo_dados_big_table_1 == 1 or tipo_dados_big_table_2 == 1:
            if tipo_dados_big_table_1 == 1:
                bd_id_principal_1 = dados_big_table_1.get().id_principal
                print(bd_id_principal_1)
                bd_drugbank_id_1 = DrugbankAnvisa.objects.filter(drugbank_id = bd_id_principal_1).get().drugbank_id
                print(bd_drugbank_id_1)
            if tipo_dados_big_table_2 == 1:
                bd_id_principal_2 = dados_big_table_2.get().id_principal
                print(bd_id_principal_2)
                bd_drugbank_id_2 = DrugbankAnvisa.objects.filter(drugbank_id = bd_id_principal_2).get().drugbank_id
                print(bd_drugbank_id_2)

        if tipo_dados_big_table_1 == 2 or tipo_dados_big_table_2 == 2:
            if tipo_dados_big_table_1 == 2:
                
                bd_id_principal_1 = dados_big_table_1.get().id_principal
                print('big table id_principal = ', bd_id_principal_1)
                
                try:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_1 )
                    print('anvisa_nome_pricipio idPrincipio = ', bd_anvisa_nome_idprincipio)
                except:
                    bd_anvisa_principioativo_idPativo = AnvisaPrincipioativo.objects.filter(id_pativo=bd_id_principal_1 ).get().id_pativo
                    print('bd_anvisa_principioativo_idPativo = ', bd_anvisa_principioativo_idPativo)
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_principioativo_idPativo ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_1 = bd_drugbank_anvisa_drugbank_id
                else:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_1 )
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_nome_idprincipio ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_1 = bd_drugbank_anvisa_drugbank_id

            if tipo_dados_big_table_2 == 2:
                
                bd_id_principal_2 = dados_big_table_1.get().id_principal
                print('big table id_principal = ', bd_id_principal_2)
                
                try:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_2 )
                    print('anvisa_nome_pricipio idPrincipio = ', bd_anvisa_nome_idprincipio)
                except:
                    bd_anvisa_principioativo_idPativo = AnvisaPrincipioativo.objects.filter(id_pativo=bd_id_principal_2 ).get().id_pativo
                    print('bd_anvisa_principioativo_idPativo = ', bd_anvisa_principioativo_idPativo)
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_principioativo_idPativo ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_2 = bd_drugbank_anvisa_drugbank_id
                else:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_2 )
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_nome_idprincipio ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_2 = bd_drugbank_anvisa_drugbank_id

        if tipo_dados_big_table_1 == 3 or tipo_dados_big_table_2 == 3:
            if tipo_dados_big_table_1 == 3:
                
                bd_id_principal_1 = dados_big_table_1.get().id_principal
                print('big table id_principal = ', bd_id_principal_1)
                
                try:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_1 )
                    print('anvisa_nome_pricipio idPrincipio = ', bd_anvisa_nome_idprincipio)
                except:
                    bd_anvisa_principioativo_idPativo = AnvisaPrincipioativo.objects.filter(id_pativo=bd_id_principal_1 ).get().id_pativo
                    print('bd_anvisa_principioativo_idPativo = ', bd_anvisa_principioativo_idPativo)
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_principioativo_idPativo ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_1 = bd_drugbank_anvisa_drugbank_id
                else:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_1 )
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_nome_idprincipio ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_1 = bd_drugbank_anvisa_drugbank_id

            if tipo_dados_big_table_2 == 3:
                
                bd_id_principal_2 = dados_big_table_1.get().id_principal
                print('big table id_principal = ', bd_id_principal_2)
                
                try:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_2 )
                    print('anvisa_nome_pricipio idPrincipio = ', bd_anvisa_nome_idprincipio)
                except:
                    bd_anvisa_principioativo_idPativo = AnvisaPrincipioativo.objects.filter(id_pativo=bd_id_principal_2 ).get().id_pativo
                    print('bd_anvisa_principioativo_idPativo = ', bd_anvisa_principioativo_idPativo)
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_principioativo_idPativo ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_2 = bd_drugbank_anvisa_drugbank_id
                else:
                    bd_anvisa_nome_idprincipio = AnvisaPrincipioativo.objects.filter(idproduto = bd_id_principal_2 )
                    bd_drugbank_anvisa_drugbank_id = DrugbankAnvisa.objects.filter(id_pativo=bd_anvisa_nome_idprincipio ).get().drugbank_id
                    print('bd_drugbank_anvisa_drugbank_id = ', bd_drugbank_anvisa_drugbank_id)
                    bd_drugbank_id_2 = bd_drugbank_anvisa_drugbank_id

        print(bd_drugbank_id_1, bd_drugbank_id_2)

    #EFETUA A CONSULTA NO BANCO DE DADOS DRUGBANK INTERACAO - VERIFICA SE HA INTERACAO
        drug_contains = DrugbankInteracao.objects.filter(drugbank_id1 = bd_drugbank_id_1, drugbank_id2 = bd_drugbank_id_2)
        print(drug_contains)
        try:
            drug_contains.get()
            print(type(drug_contains))
        except:
            dados3 = BigtableNomes.objects.filter(id=search)
            dados4 = BigtableNomes.objects.filter(id=search1) 
            print(dados3, dados4)
            return render(request, 'app_interacao_medicamentos/exibe_resultado.html', {'dados3':dados3, 'dados4':dados4,'no_interation': 'Não existe Interação entre: '} )
        else:
            dados3 = BigtableNomes.objects.filter(id=search)
            dados4 = BigtableNomes.objects.filter(id=search1) 
            return render(request, 'app_interacao_medicamentos/exibe_resultado.html', {'dados3':dados3, 'dados4':dados4,'drug_contains':drug_contains} )

    else:
        dados = BigtableNomes.objects.all().order_by('nome')
        return render(request, 'app_interacao_medicamentos/lista_medicamentos.html', {'dados':dados})
 
#EFETUA A BUSCA DE TODOS OS MEDICAMENTOS REGISTRADOS NA ANVISA PARA MAIS INFORMACOES E BULA
def busca_anvisa(request):
    search_anvisa = request.GET.get('nomeProduto')
    if search_anvisa:
        dados =BigtableNomes.objects.filter(id=search_anvisa).order_by('nome')
        dados_anvisa = str(dados.get().nome)
        return render(request, 'app_interacao_medicamentos/meta.html', {'dados':dados, 'dados_anvisa':dados_anvisa} )

    dados = BigtableNomes.objects.filter(tipo_origem=3).order_by('nome')
    return render(request, 'app_interacao_medicamentos/busca_anvisa.html', {'dados':dados} )

#REDIRECIONA A BUSCA PARA O SITE DA ANVISA
def redireciona_anvisa(request):
    return render(request, 'app_interacao_medicamentos/meta.html')

def exibe_medicamento(request, id):
    dados = get_object_or_404(BigtableNomes, pk=id)
    return render(request, 'app_interacao_medicamentos/exibe_medicamento.html',  {'dados':dados})