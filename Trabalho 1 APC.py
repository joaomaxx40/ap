T=int(input()) #Indica qual tarefa
N=input() #quantas linhas de dados

if T == 1:
    lista_situ=list()
    entradas=list()
    for i in range(int(N)):
        z=int(N)
        ano_unb,dia,mes,ano_nasc,genero,situação=input().split()
        ref=ano_unb,dia,mes,ano_nasc,genero,situação
        entradas.append(ref)
        lista_situ.append(situação)
        x=lista_situ.count('6')+lista_situ.count('2')
        y=(x/z)*100
        outra_situ=100-y
    print(f'matriculados ou formados: {y:.1f} ')
    print(f'alunos em outras situacoes: {outra_situ:.1f}')
if T == 2:
    lista_sexo=list()
    entradas=list()
    for i in range(int(N)):
        z=int(N)
        ano_unb,dia,mes,ano_nasc,genero,situação=input().split()
        ref=ano_unb,dia,mes,ano_nasc,genero,situação
        entradas.append(ref)
        lista_sexo.append(genero)
        x=lista_sexo.count('1')
        y=(x/z)*100
        homens=100-y
    print(f'sexo masculino: {homens:.1f}')
    print(f'sexo feminino: {y:.1f}')
    
if T == 3:
    lista_tempo=list()
    entradas=list()
    for i in range(int(N)):
        z=int(N)
        ano_unb,dia,mes,ano_nasc,genero,situação=map(int,input().split())
        ref=ano_unb,dia,mes,ano_nasc,genero,situação
        entradas.append(ref)
        lista_tempo.append(2019-ano_unb)
        x=sum(lista_tempo)
        y=x/z
    print(f'media de anos desde ingresso:  {y:.1f}')
       
if T == 4:
    import datetime
    z=int(N)
    L_dias=[] 
    for w in range(z):
        ano_unb,dia,mes,ano_nasc,genero,situação=map(int,input().split())
        w=datetime.datetime(ano_nasc,mes,dia).weekday()
        L_dias.append(w)
    c0=(L_dias.count(0)/z)*100
    c1=(L_dias.count(1)/z)*100
    c2=(L_dias.count(2)/z)*100
    c3=(L_dias.count(3)/z)*100
    c4=(L_dias.count(4)/z)*100
    c5=(L_dias.count(5)/z)*100
    c6=(L_dias.count(6)/z)*100
    print(f'domingo: {c6:.1f}')
    print(f'segunda: {c0:.1f}')
    print(f'terca: {c1:.1f}')
    print(f'quarta: {c2:.1f}')
    print(f'quinta: {c3:.1f}')
    print(f'sexta: {c4:.1f}')
    print(f'sabado:  {c5:.1f}')
if T == 5:
    z=int(N)
    L_top=[]
    lista_situ=list()
    lista_sexo=list()
    for w in range(z):
        ano_unb,dia,mes,ano_nasc,genero,situação=map(int,input().split())
        w=(genero,situação)
        L_top.append(w)
        lista_sexo.append(genero)
        lista_situ.append(situação)
    homens=lista_sexo.count(2)
    mulheres=lista_sexo.count(1)
    x=L_top.count((2,2))+L_top.count((2,6))
    M=L_top.count((1,2))+L_top.count((1,6))
    mat_form_homem=(x/homens)*100
    outra_situ_hom=(100-mat_form_homem)
    mat_form_mulher=(M/mulheres)*100
    outra_situ_mulher=(100-mat_form_mulher)
    print(f'dentre masculinos:')
    print(f'matriculados ou formados: {mat_form_homem:.1f}')
    print(f'alunos em outras situacoes: {outra_situ_hom:.1f}')
    print(f'dentre femininos:')
    print(f'matriculados ou formados:{mat_form_mulher:.1f}')
    print(f'alunos em outras situacoes:  {outra_situ_mulher:.1f}')
if T == 6:
    z=int(N)
    L_6=[]
    l_6=[]
    L_6a=[]
    l_6a=[]
    for w in range(z):
        ano_unb,dia,mes,ano_nasc,genero,situação=map(int,input().split())
        if situação == 2 or situação == 6:
            w=(2019-ano_unb)
            k=(situação)
            L_6.append(w)
            l_6.append(k)
            n_situ=l_6.count(2)+l_6.count(6)
            n_ano_unb=len(L_6)
            soma_unb=sum(L_6)
            media_mat_form=soma_unb/n_ano_unb
        else:
            W=(2019-ano_unb)
            L_6a.append(W)
            num_nao_unb=len(L_6a)
            soma_n_unb=sum(L_6a)
            media=soma_n_unb/num_nao_unb
    print('dentre matriculados ou formados:')
    print(f'media de anos desde ingresso:  {media_mat_form:.1f}')
    print('dentre alunos em outras situacoes:')
    print(f'media de anos desde ingresso:  {media:.1f}')
           
if T == 7:
    import datetime
    z=int(N)
    L_dias=[]
    l_dias=[]
    lista_mulher=[]
    lista_homem=[]
    for w in range(z):
        ano_unb,dia,mes,ano_nasc,genero,situação=map(int,input().split())
        if genero == 1:
            M=(genero)
            w=datetime.datetime(ano_nasc,mes,dia).weekday()
            L_dias.append(w)
            lista_mulher.append(M)
            numero_mulheres=len(lista_mulher)
            c0=(L_dias.count(0)/numero_mulheres)*100
            c1=(L_dias.count(1)/numero_mulheres)*100
            c2=(L_dias.count(2)/numero_mulheres)*100
            c3=(L_dias.count(3)/numero_mulheres)*100
            c4=(L_dias.count(4)/numero_mulheres)*100
            c5=(L_dias.count(5)/numero_mulheres)*100
            c6=(L_dias.count(6)/numero_mulheres)*100
        else:
            H=(genero)
            W=datetime.datetime(ano_nasc,mes,dia).weekday()
            l_dias.append(W)
            lista_homem.append(H)
            num_homem=len(lista_homem)
            H0=(l_dias.count(0)/num_homem)*100
            H1=(l_dias.count(1)/num_homem)*100
            H2=(l_dias.count(2)/num_homem)*100
            H3=(l_dias.count(3)/num_homem)*100
            H4=(l_dias.count(4)/num_homem)*100
            H5=(l_dias.count(5)/num_homem)*100
            H6=(l_dias.count(6)/num_homem)*100
    print('dentre masculinos:')
    print(f'domingo: {H6:.1f}')
    print(f'segunda:  {H0:.1f}')
    print(f'terca: {H1:.1f}')
    print(f'quarta: {H2:.1f}')
    print(f'quinta: {H3:.1f}')
    print(f'sexta:  {H4:.1f}')
    print(f'sabado: {H5:.1f}')
    print('dentre femininos:')
    print(f'domingo:  {c6:.1f}')
    print(f'segunda:  {c0:.1f}')
    print(f'terca: {c1:.1f}')
    print(f'quarta:  {c2:.1f}')
    print(f'quinta: {c3:.1f}')
    print(f'sexta:  {c4:.1f}')
    print(f'sabado: {c5:.1f}')

            
            