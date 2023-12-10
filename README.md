# DRF Boilerplate

Um boilerplate para projetos Django focado para API com [Django REST Framework](https://www.django-rest-framework.org/)

## Ferramentas utilizadas
- python = "3.11.3"
- django = "4.2"
- python-decouple = "^3.8"
- dj-database-url = "^2.1.0"
- psycopg2-binary = "^2.9.9"
- django-cors-headers = "^4.3.1"
- djangorestframework = "^3.14.0"
- drf-spectacular = "^0.26.5"
- pre-commit = "^3.6.0"
- ruff = "^0.1.7"
- black = "^23.11.0"
- ipdb = "^0.13.13"
- pytest-django = "^4.7.0"
- pytest-cov = "^4.1.0"
- pytest-factoryboy = "^2.6.0"
- faker = "^20.1.0"

## Banco de dados
Caso seja necessário a criação de um banco de dados para a aplicação, há um arquivo `docker-compose.yml` que cria um container de postgres. Para rodar o container basta executar:

```
docker-compose up --build
```

---
