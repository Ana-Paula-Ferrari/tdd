from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_16_05_1994_retornar_29(self):
        entrada = '16/05/1994' # Given-Contexto
        esperado = 29

        funcionario_teste = Funcionario('Teste', entrada, 12000)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_Ana_Paula_Ferrari_retornar_Ferrari(self):
        entrada = " Ana Paula Ferrari " #contexto
        esperado = "Ferrari"

        ana = Funcionario( entrada, "16/05/1994", 12000)
        resultado = ana.sobrenome() #ação

        assert resultado == esperado #desfecho

    def test_quando_decrescimo_(self):
        entrada_salario = 100000 #given
        entrada_nome = "Carlos Bragança"
        esperado = 90000

        funcionario = Funcionario(entrada_nome, '16/05/1994', entrada_salario)
        funcionario.decrescimo_salario() #when
        resultado = funcionario.salario

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_receber_1000_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario = Funcionario('Ana Maria', '21/05/1989', entrada)
        resultado = funcionario.calcular_bonus()

        assert esperado == resultado
    
    #espera-se que o retorno seja uma exception
    @mark.calcular_bonus
    def test_quando_calcular_bonus_receber_100000_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000
            
            funcionario = Funcionario("Ana Maria", "26/04/2000", entrada)
            resultado = funcionario.calcular_bonus()

            assert resultado


