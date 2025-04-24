Explicação do Código

Primeiro criei 3 classes de exceções para quando um produto não existe, outra para quando ao
realizar uma compra o saldo for insuficiente e outra para quando o carrinho está vazio. Após
a criação das exceções criei um classe LojaVirtual como classe principal que contém todas as
funções necessárias para o funcionamento do programa entre elas a função com o dicionário
dos produtos e o saldo do cliente, uma para exibir os produtos, outra para adicionar produtos
ao carrinho, mostrar o carrinho e efetuar o pagamento dos produtos bem como um menu de
opções. Ao inicializar o programa deparamos-nos com o menu com as opções mencionadas
anteriormente em que cada uma irá desempenhar uma função diferente, assim, o cliente
deverá conseguir visualizar os produtos, adicionar produtos ao carrinho, visualizar o carrinho
e/ou efetuar o pagamento assim como sair do programa. Existem 5 produtos disponíveis com
diferentes preços e um cliente com um total de 100€ para gastar, se por acaso o cliente
ultrapassar este saldo o programa não irá concluir a compra. Para além disto existem os
tratamentos de erros como por exemplo se o carrinho estiver vazio irá aparecer uma
mensagem a informar que está vazio ou então se por acaso escolher um produto que não
exista irá aparecer uma mensagem para escolher apenas os ID disponíveis no catálogo
