from django.db import models

# Create your models here.


class Operacao(models.Model): # CREATE TABLE Operacao (
    # ID INT AUTO_INCREMENT PRIMARY KEY,
    ticker = models.CharField(max_length=10) # ticker VARCHAR(10) NOT NULL,
    tipo = models.CharField(max_length=10) # tipo VARCHAR(10) NOT NULL,
    quantidade = models.IntegerField() # quantidade INT NOT NULL,
    preco = models.DecimalField(max_digits=10, decimal_places=2) # preco DECIMAL(10,2) NOT NULL,
    data_operacao = models.DateField() # data_operacao DATE NOT NULL
    # );

    def __str__(self):
        return f"{self.ticker} - {self.tipo}"





