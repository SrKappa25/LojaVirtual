class ProdutoInexistenteError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class CarrinhoVazioError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class LojaVirtual:
    def __init__(self):
        self.produtos = {
            1: {"nome": "Camisola", "preco": 13.99},
            2: {"nome": "Calças", "preco": 7.95},
            3: {"nome": "Ténis", "preco": 44.67},
            4: {"nome": "Meias", "preco": 12.96},
            5: {"nome": "Chapéu", "preco": 5.99}
        }
        
        self.carrinho = {}

        self.saldo_cliente = 100.00

    def exibir_produtos(self):
        print("\nProdutos Disponíveis")
        for id_produto, produto in self.produtos.items():
            print(f"{id_produto}. {produto['nome']} - {produto['preco']:.2f}€")
    
    def adicionar_ao_carrinho(self):
        try:
            self.exibir_produtos()
            id_produto = int(input("\nID do produto: "))

            if id_produto not in self.produtos:
                raise ProdutoInexistenteError("Produto não existe.")
            
            quantidade = int(input("Quantidade: "))
            
            if id_produto in self.carrinho:
                self.carrinho[id_produto] += quantidade
            else:
                self.carrinho[id_produto] = quantidade
            
            print(f"\n{quantidade} {self.produtos[id_produto]['nome']} adicionado ao carrinho!")

        except ValueError:
            print("\nDigite apenas o ID do produto e quantidade como números válidos")
        except ProdutoInexistenteError as e:
            print(f"\nErro: {e}")
        except Exception as e:
            print(f"\nErro inesperado: {e}")
    
    def exibir_carrinho(self):
        if not self.carrinho:
            print("\nO seu carrinho está vazio.")
            return 0

        total_geral = 0
        print("\nO Seu Carrinho")
        
        for id_produto, quantidade in self.carrinho.items():
            nome = self.produtos[id_produto]["nome"]
            preco = self.produtos[id_produto]["preco"]
            subtotal = preco * quantidade
            total_geral += subtotal
            
            print(f"{nome} - {quantidade} x {preco:.2f}€ = {subtotal:.2f}€")
        
        print(f"\nTotal: {total_geral:.2f}€")
        return total_geral
    
    def efetuar_pagamento(self):
        try:
            if not self.carrinho:
                raise CarrinhoVazioError("Carrinho Vazio.")
            
            total = self.exibir_carrinho()
            
            if total > self.saldo_cliente:
                raise SaldoInsuficienteError("Saldo insuficiente.")
            
            print(f"\nSaldo atual: {self.saldo_cliente:.2f}€")
            confirmacao = input("\nConfirmar pagamento? S/N: ").upper()
            
            if confirmacao == 'S':
                self.saldo_cliente -= total
                print("\nPagamento realizado com sucesso!")
                print(f"Saldo: {self.saldo_cliente:.2f}€")
                self.carrinho = {}
            else:
                print("\nOperação cancelada.")    
        except CarrinhoVazioError as e:
            print(f"\nErro: {e}")
        except SaldoInsuficienteError as e:
            print(f"\nErro: {e}")
        except Exception as e:
            print(f"\nErro inesperado: {e}")
    
    def menu_principal(self):
        opcoes = {
            1: ("Ver produtos", self.exibir_produtos),
            2: ("Adicionar ao carrinho", self.adicionar_ao_carrinho),
            3: ("Ver carrinho", self.exibir_carrinho),
            4: ("Efetuar pagamento", self.efetuar_pagamento),
            5: ("Sair", None)
        }
        
        while True:
            print("\nMENU")
            for num, (desc, _) in opcoes.items():
                print(f"{num}. {desc}")
            
            try:
                escolha = int(input("\nEscolha uma opção: "))
                
                if escolha == 5:
                    print("\nObrigado!")
                    break
                
                if escolha not in opcoes:
                    print("\nOpção inválida.")
                    continue
                
                if opcoes[escolha][1] is not None:
                    opcoes[escolha][1]()
            except ValueError:
                print("\nDigite apenas números para selecionar uma opção.")
            except Exception as e:
                print(f"\nErro inesperado: {e}")
              
def main():
    print("Loja Virtual")
    loja = LojaVirtual()
    loja.menu_principal()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print(f"\n\nPrograma encerrado. Erro: {e}")
