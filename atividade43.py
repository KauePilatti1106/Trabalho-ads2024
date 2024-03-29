Hambúrguer=int(input('Quantos Hambúrguer o usuario comprou?'))
Cheeseburger=int(input('Quantos Cheeseburger o usario comprou?'))
fritas=int(input('Quantas fritas o usuario compru?'))
refrigerantes=int(input('Quantos refrigerantes o usuario compro?'))
Milkshake=int(input('Quantos Milkshake o usuario comporu?'))

Hambúrguer_comprado= 3.00*Hambúrguer
Cheeseburger_comprados= 2.50*Cheeseburger
fritas_vendidas=2.50*fritas
refrigerantes_vedidos=1.00*refrigerantes
Milkshake_vendidos=3.00*Milkshake
Total=Hambúrguer_comprado+Cheeseburger_comprados+fritas_vendidas+refrigerantes_vedidos+Milkshake_vendidos

print('O usuario gatou:', Total)
