import unittest


class TestaSolucao(unittest.TestCase):
    #exemplo só
    def test_sucessor(self):
        """
        Testa a funcao sucessor para o estado "2_3541687"
        :return:

        """
        # a lista de sucessores esperados é igual ao conjunto abaixo (ordem nao importa)
        succ_esperados = {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")}

        sucessores = "2_3541687"  # obtem os sucessores chamando a funcao implementada
        self.assertEqual(3, len(sucessores))     # verifica se foram retornados 3 sucessores
        for s in sucessores:                     # verifica se os sucessores retornados estao entre os esperados
            self.assertIn(s, succ_esperados)

if __name__ == '__main__':
    unittest.main()
