curso01 = int(input("digite quantas avaliações o curso01 teve:"))
curso02 = int(input("digite quantas avaliações o curso02 teve:"))


if curso01 > curso02:
    print("curso01 teve mais avaliações")
elif curso02 > curso01:
    print("curso02 teve mais avaliações")
else:
    print("os dois cursos tiveram as mesmas avaliações")