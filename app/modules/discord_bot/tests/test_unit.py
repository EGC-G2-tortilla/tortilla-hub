import pytest
from unittest.mock import AsyncMock, patch
from app.modules.discord_bot.bot import (
    help_command,
    most_downloaded,
    total_dataset_downloads,
    datasets_counter,
    feature_models_counter,
)


@patch("app.modules.discord_bot.bot.help")
@pytest.mark.asyncio
async def test_help_command(mock_help):

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await help_command(interaction_mock)
    # Verifica el contenido del embed
    embed = interaction_mock.response.send_message.call_args[1]["embed"]
    assert embed.title == "📖 Ayuda del Bot"
    assert (
        "Aquí tienes la lista de comandos disponibles para interactuar con este bot."
        in embed.description
    )
    assert len(embed.fields) == 4

    for field in embed.fields:
        assert field.name in [
            "📂 Gestión de Datasets",
            "📊 Estadísticas Generales",
            "🔧 Modelos de Características",
            "📚 Autores",
        ]
        assert field.value != ""


# Test for most_downloaded_datasets
@patch("app.modules.discord_bot.bot.dataset_service")
@pytest.mark.asyncio
async def test_most_downloaded_datasets(mock_dataset_service):
    mock_datasets = [
        {"name": "dataset1", "downloads": 10},
        {"name": "dataset2", "downloads": 5},
        {"name": "dataset3", "downloads": 3},
        {"name": "dataset4", "downloads": 1},
    ]
    mock_dataset_service.most_downloaded.return_value = mock_datasets
    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await most_downloaded(interaction_mock)

    mock_dataset_service.most_downloaded.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()
    sent_message = interaction_mock.response.send_message.call_args[1]
    assert "Gráfico de descargas" in sent_message["embed"].title
    # Validar que el archivo del gráfico fue adjuntado correctamente
    file = interaction_mock.response.send_message.call_args[1]["file"]
    assert file.filename == "top_datasets.png"


# Test for datasets_counter
@patch("app.modules.discord_bot.bot.dataset_service")
@pytest.mark.asyncio
async def test_datasets_counter(mock_dataset_service):
    mock_dataset_service.count_synchronized_datasets.return_value = 42

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await datasets_counter(interaction_mock)

    mock_dataset_service.count_synchronized_datasets.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()
    sent_message = interaction_mock.response.send_message.call_args[1]
    assert "Total de Datasets Sincronizados" in sent_message["embed"].title
    assert "42" in sent_message["embed"].description


# Test for feature_models_counter
@patch("app.modules.discord_bot.bot.feature_model_service")
@pytest.mark.asyncio
async def test_feature_models_counter(mock_feature_model_service):
    mock_feature_model_service.count_feature_models.return_value = 10

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await feature_models_counter(interaction_mock)

    sent_message = interaction_mock.response.send_message.call_args[1]
    mock_feature_model_service.count_feature_models.assert_called_once()
    assert "Total de Modelos de Características" in sent_message["embed"].title
    interaction_mock.response.send_message.assert_called_once()
    assert "10" in sent_message["embed"].description


# Test for total_dataset_downloads
@patch("app.modules.discord_bot.bot.dataset_service")
@pytest.mark.asyncio
async def test_total_dataset_downloads(mock_dataset_service):
    mock_dataset_service.total_dataset_downloads.return_value = 150

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await total_dataset_downloads(interaction_mock)

    mock_dataset_service.total_dataset_downloads.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()
    sent_message = interaction_mock.response.send_message.call_args[1]
    assert "Total de Descargas de Datasets" in sent_message["embed"].title
    assert "150" in sent_message["embed"].description
