import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user


def test_serialize_user_completo():

    user = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuário",
        "address": "123 Rua Exemplo",
        "role": "admin"
    }

    resultado = serialize_user(user)

    esperado = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuário",
        "address": "123 Rua Exemplo",
        "role": "admin"
    }

    assert resultado == esperado

def test_serialize_user_incompleto():

    user = {
        "email": "teste@exemplo.com",
    }

    resultado = serialize_user(user)

    esperado = {
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado


def test_serialize_user_incompleto():

    user = {}

    resultado = serialize_user(user)

    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado

def test_serialize_user_inteiro():

    with pytest.raises(AttributeError):
        serialize_user(123456)

def test_serialize_user_string():

    with pytest.raises(AttributeError):
        serialize_user("String de teste")

def test_serialize_user_inesperado():
    user = {
        "email": 1234,
        "name": ["Nome Inesperado", "Outro nome"],
        "address": {"rua":"123 Exemplo"},
        "role": True
    }

    resultado = serialize_user(user)

    esperado = {
        "email": 1234,
        "name": ["Nome Inesperado", "Outro nome"],
        "address": {"rua":"123 Exemplo"},
        "role": True
    }


def test_serialize_user_lista():
    with pytest.raises(AttributeError):
        serialize_user(["item1", "item2"])


def test_serialize_user_none():
    with pytest.raises(AttributeError):
        serialize_user(None)

def test_serialize_user_dict_none():
    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    resultado = serialize_user(user)

    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    assert resultado == esperado

