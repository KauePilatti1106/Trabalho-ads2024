Valor_da_compra=float(input('Qual o valor da compra?'))
Valor_do_desconto_a_vista=Valor_da_compra-(10/100)
Valor_da_compra_a_vista=Valor_da_compra-(Valor_da_compra*Valor_do_desconto_a_vista)
Valor_do_produto_parcelado=Valor_da_compra/3
Comição_a_vista=Valor_do_desconto_a_vista*(5/100)
Comição_parcalado=Valor_da_compra*(5/100)

print(f'''O coprador ira pagar a vista o produto {Valor_da_compra_a_vista} e o vendedor ganhara 
      de comição {Comição_a_vista} por esse produto , se o clinte parcela em 3x ira paga {Valor_da_compra}
      e pagara por parcela {Valor_do_produto_parcelado} e o vendedor ganhara de comição {Comição_parcalado} por esse 
      produto.''')