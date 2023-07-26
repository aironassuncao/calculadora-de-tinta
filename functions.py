def nec_tint():
    tint = int(input("Qual a quantidade de tinta: "))
    wall_h = int(input("Qual a Altura da parede: "))
    wall_w = int(input("Qual a largura da parede: "))
    print((wall_h * wall_w) / tint)
