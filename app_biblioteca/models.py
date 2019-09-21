from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    nome = models.CharField("Nome", max_length=50)
    data_nacimento = models.DateField("Data de Nascimento")

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField('Matricula', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Categoria", max_length=50)
    descricao = models.CharField(verbose_name="Descrição", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nome

'''class Tipo(models.Model):
    nome = models.CharField(verbose_name="Tipo de Livro", max_length=15)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.nome'''

class Livro(models.Model):
    titulo = models.CharField("Título", max_length=50)
    autor = models.CharField("Autor", max_length=50)
    isbn = models.CharField("isnb", max_length=20)
    ano_public = models.IntegerField()
    edicao = models.CharField("Edição", max_length=15)
    editora = models.CharField("Editora", max_length=20)
    categoria_livro = models.ManyToManyField(Categoria)
    tipo = models.BooleanField('É digital?', default=False)

    def __str__(self):
        return self.titulo

class Emprestimo (models.Model):
    livro = models.ManyToManyField(Livro, blank=True, null=True)
    pessoaPegar = models.ForeignKey(Pessoa, related_name='pessoas', blank=True, null=True, on_delete=models.SET_NULL)
    data_pegar = models.DateTimeField(auto_now_add=True)
    data_lim_devo = models.DateField("Data limite para devolver", blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
    data_efetiva_devolucao = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        s = ''
        for i in self.livro.all():
            s = s +' ' + i.titulo +', '
        return str(self.pessoaPegar) + ' Pegou os livros' + s + ' na data ' + self.data_pegar.strftime('%b/%d/%Y')





