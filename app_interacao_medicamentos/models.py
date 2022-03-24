from django.db import models

class BigtableNomes(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_principal = models.IntegerField()
    nome = models.CharField(max_length=250)
    tipo_origem = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'bigtable_nomes'

    def __str__(self):
        return self.nome



class AnvisaNome(models.Model):
    id = models.IntegerField(primary_key=True)
    nomeproduto = models.CharField(db_column='nomeProduto', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'anvisa_nome'

    def __str__(self):
        return self.nomeproduto


class AnvisaPrincipioativo(models.Model):
    id_pativo = models.IntegerField(db_column='id_pAtivo', primary_key=True)  # Field name made lowercase.
    nome_pativo = models.CharField(db_column='nome_pAtivo', max_length=250)  # Field name made lowercase.
    translated_pativo = models.CharField(db_column='translated_pAtivo', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'anvisa_principioativo'

    def __str__(self):
        return self.nome_pativo


class DrugbankNome(models.Model):
    drugbank_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'drugbank_nome'

    def __str__(self):
        return self.name

class AnvisaNomePrincipioativo(models.Model):
    idproduto = models.OneToOneField(AnvisaNome, models.DO_NOTHING, db_column='idProduto', primary_key=True)  # Field name made lowercase.
    idprincipio = models.ForeignKey('AnvisaPrincipioativo', models.DO_NOTHING, db_column='idPrincipio')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'anvisa_nome_principioativo'
        unique_together = (('idproduto', 'idprincipio'),)

    def __str__(self):
        return str(self.idproduto)


class DrugbankAnvisa(models.Model):    
    drugbank = models.OneToOneField('DrugbankNome', models.DO_NOTHING, primary_key=True)
    id_pativo = models.ForeignKey(AnvisaPrincipioativo, models.DO_NOTHING, db_column='id_pAtivo')  # Field name made lowercase.
    matchingvalue = models.FloatField(db_column='matchingValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'drugbank_anvisa'
        unique_together = (('drugbank', 'id_pativo'),)

    def __str__(self):
        return str(self.id_pativo) + ' - '+ str(self.drugbank)

#MODELO EXPERIMENTAL
class TesteInteracao(models.Model):
    item_1 = models.IntegerField(primary_key=True)
    item_2 = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'teste_interacao'
        unique_together = (('item_1', 'item_2'),)



class Interacao(models.Model):
    drugbank_id1 = models.ForeignKey(DrugbankAnvisa, related_name= 'drugbank_id1', on_delete=models.CASCADE)
    drugbank_id2 = models.ForeignKey(DrugbankAnvisa, related_name= 'drugbank_id2', on_delete=models.CASCADE)




class DrugbankInteracao(models.Model):
    drugbank_id1 = models.OneToOneField('DrugbankNome',related_name= 'drugbank_id1', db_column='drugbank_id1', primary_key=True , on_delete=models.CASCADE)
    drugbank_id2 = models.ForeignKey('DrugbankNome', related_name= 'drugbank_id2' , db_column='drugbank_id2', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'drugbank_interacao'
        unique_together = (('drugbank_id1', 'drugbank_id2'),)
