# Commands

## secret_key generation

```python
from django.core.management.utils import get_random_secret_key

get_random_secret_key()
```

## pytest execute

```
pytest
```

## pytest coverage

```
coverage run -m pytest

# show test coverage in terminal
coverage report

# generate test coverage html
coverage html
```

```
# execute test and show coverage
pytest --cov
```

### drf-spectacular generate schema

```
python manage.py spectacular --file schema.yml
```
