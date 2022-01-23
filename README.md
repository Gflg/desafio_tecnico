# Desafio Técnico - Deloitte
Solução para o case técnico de Back-End proposto pela Deloitte. O desafio está hospedado em https://desafio-deloitte.herokuapp.com.

# Tecnologias utilizadas
Python \
Django \
Django REST Framework \
Swagger/Redoc \
Heroku

# Explicação sobre como utilizar a API
Ao adentrar o site, é possível verificar a home criada pelo próprio Django para a API desse desafio técnico. Aqui, serão exibidos todos os endpoints referentes aos modelos desenvolvidos para o case técnico da Agência Cronos.

A API é composta por CRUDs de Serviços, Posts e Integrantes de Equipe.
Para acessar o endpoint de cada um dos modelos desenvolvidos, é necessário realizar uma autenticação dentro do próprio Django.
Basta logar em https://desafio-deloitte.herokuapp.com/admin/ com as seguintes credenciais:

````
usuário: deloitte
senha: desafiotecnico
````

Com o usuário autenticado no Django, é possível realizar operações na API desenvolvida para esse projeto. \
Para verificar todas as possibilidades de operações dessa API, pode-se verificar a documentação gerada com as bibliotecas Swagger/Redoc.
Basta acessar https://desafio-deloitte.herokuapp.com/redoc.
