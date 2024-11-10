import pytest
from io import BytesIO


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass

    yield test_client


def test_sample_assertion(test_client):
    """
    Sample test to verify that the test framework and environment are working correctly.
    It does not communicate with the Flask application; it only performs a simple assertion to
    confirm that the tests in this module can be executed.
    """
    greeting = "Hello, World!"
    assert greeting == "Hello, World!", "The greeting does not coincide with 'Hello, World!'"


def test_validate_uvl_file_valid(test_client):
    """
    Prueba la función validate_uvl_file con un archivo UVL extremadamente básico.
    """
    basic_uvl_content = """features
    Chat
        mandatory
            Connection
                alternative
                    "Peer 2 Peer"
                    Server
            Messages
                or
                    Text
                    Video
                    Audio
        optional
            "Data Storage"
            "Media Player"

constraints
    Server => "Data Storage"
    Video | Audio => "Media Player"
"""
    data = {
        'file': (BytesIO(basic_uvl_content.encode('utf-8')), 'extremely_basic_model.uvl')
    }

    response = test_client.post('/flamapy/validate_uvl', data=data, content_type='multipart/form-data')

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200, f"Expected 200, got {response.status_code} with message {response.get_json()}"
    assert response.get_json() == {"message": "Valid Model"}


def test_validate_uvl_file_invalid(test_client):
    """
    Prueba la función validate_uvl_file con un archivo UVL inválido.
    """
    # Contenido de un archivo UVL inválido (falta el ':' después de 'features')
    invalid_uvl_content = """
    features
        Root

    constraints:
    """

    # Crear un objeto BytesIO a partir del contenido del archivo UVL
    data = {
        'file': (BytesIO(invalid_uvl_content.encode('utf-8')), 'invalid_model.uvl')
    }

    # Hacer una petición POST al endpoint de validación
    response = test_client.post('/flamapy/validate_uvl', data=data, content_type='multipart/form-data')

    # Verificar que la respuesta indica un error
    assert response.status_code == 400
    json_data = response.get_json()

    # Añadir un print para ver el contenido real de json_data en caso de fallo
    print("Respuesta JSON:", json_data)  # Esto nos ayudará a depurar

    assert 'errors' in json_data
    assert len(json_data['errors']) > 0

    # Verificar que el mensaje de error contiene partes clave
    error_messages = json_data['errors']
    expected_messages = [
        "Line 5:15 - token recognition error at",  # Verifica que el error en la línea 5 esté presente
        "Line 2"  # Asegura que hay un problema en la línea 2 (por ejemplo, al no reconocer el input)
    ]

    for expected in expected_messages:
        assert any(expected in error for error in error_messages), f"Expected'{expected}' not found in message."
