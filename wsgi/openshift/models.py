from django.db import models

class Aluno(models.Model):
    student_id = models.CharField(max_length=30)
    login = models.CharField(max_length=80)
    semana = models.CharField(max_length=80)
    dificuldade = models.CharField(max_length=80)
    precisa_estudar = models.CharField(max_length=80)
    praticado = models.CharField(max_length=80)
    nivel1 = models.CharField(max_length=80)
    nivel2 = models.CharField(max_length=80)
    dominado = models.CharField(max_length=80)
    pontos = models.CharField(max_length=80)
    exercises_points = models.CharField(max_length=80)
    videos_watched = models.CharField(max_length=80)
    total = models.CharField(max_length=80)

    def __unicode__(self):
        return self.login

class Rede(models.Model):
    nome = models.CharField(max_length=80)

    def __unicode__(self):
        return self.nome

class Escola(models.Model):
    login = models.CharField(max_length=80)
    student_id = models.IntegerField()
    turma = models.CharField(max_length=40)
    rede = models.ForeignKey(Rede) 

    def __unicode__(self):
        return self.login
