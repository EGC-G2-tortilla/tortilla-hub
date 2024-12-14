import pytest
from unittest.mock import AsyncMock, patch
from app.modules.discord_bot.bot import (
    help_command,
    most_downloaded,
    most_popular_authors,
    show_datasets,
    total_dataset_downloads,
    datasets_counter,
    feature_models_counter,
    total_feature_model_downloads,
    total_dataset_views,
    total_feature_model_views,
)
from app.modules.discord_bot.bot import DatasetView


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


@patch("app.modules.discord_bot.bot.feature_model_service")
@pytest.mark.asyncio
async def test_total_feature_model_downloads(mock_feature_model_service):
    mock_feature_model_service.total_feature_model_downloads.return_value = 200

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await total_feature_model_downloads(interaction_mock)

    mock_feature_model_service.total_feature_model_downloads.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()

    sent_message = interaction_mock.response.send_message.call_args[1]
    assert (
        "Total de Descargas de Modelos de Características"
        in sent_message["embed"].title
    )
    assert "200" in sent_message["embed"].description


@patch("app.modules.discord_bot.bot.dataset_service")
@pytest.mark.asyncio
async def test_total_dataset_views(mock_dataset_service):
    mock_dataset_service.total_dataset_views.return_value = 350

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await total_dataset_views(interaction_mock)

    mock_dataset_service.total_dataset_views.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()

    sent_message = interaction_mock.response.send_message.call_args[1]
    assert "Total de Vistas de Datasets" in sent_message["embed"].title
    assert "350" in sent_message["embed"].description


@patch("app.modules.discord_bot.bot.feature_model_service")
@pytest.mark.asyncio
async def test_total_feature_model_views(mock_feature_model_service):
    mock_feature_model_service.total_feature_model_views.return_value = 450

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await total_feature_model_views(interaction_mock)

    mock_feature_model_service.total_feature_model_views.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()

    sent_message = interaction_mock.response.send_message.call_args[1]
    assert (
        "Total de Vistas de Modelos de Características" in sent_message["embed"].title
    )
    assert "450" in sent_message["embed"].description


@patch("app.modules.discord_bot.bot.author_service")
@pytest.mark.asyncio
async def test_most_popular_authors(mock_author_service):
    mock_author_service.most_popular_authors.return_value = [
        {"name": "Author 1", "downloads": 100},
        {"name": "Author 2", "downloads": 80},
    ]

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await most_popular_authors(interaction_mock)

    mock_author_service.most_popular_authors.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()

    sent_message = interaction_mock.response.send_message.call_args[1]
    embed = sent_message["embed"]

    assert embed.title == "📚 Autores Más Populares"

    fields = embed.fields
    assert len(fields) == 2
    assert fields[0].name == "👤 Author 1"
    assert "100" in fields[0].value
    assert fields[1].name == "👤 Author 2"
    assert "80" in fields[1].value


@patch("app.modules.discord_bot.bot.dataset_service")
@pytest.mark.asyncio
async def test_show_datasets(mock_dataset_service):
    from datetime import datetime
    from unittest.mock import Mock

    mock_dataset_service.get_all_datasets.return_value = [
        Mock(
            id=1,
            name="Dataset 1",
            created_at=datetime(2024, 1, 1),
            ds_meta_data=Mock(
                authors=[
                    Mock(to_dict=lambda: {"name": "Author 1"}),
                    Mock(to_dict=lambda: {"name": "Author 2"}),
                ]
            ),
        ),
        Mock(
            id=2,
            name="Dataset 2",
            created_at=datetime(2024, 2, 2),
            ds_meta_data=Mock(authors=[Mock(to_dict=lambda: {"name": "Author 3"})]),
        ),
    ]

    interaction_mock = AsyncMock()
    interaction_mock.response.send_message = AsyncMock()

    await show_datasets(interaction_mock)

    mock_dataset_service.get_all_datasets.assert_called_once()
    interaction_mock.response.send_message.assert_called_once()

    sent_message = interaction_mock.response.send_message.call_args[1]
    embed = sent_message["embed"]

    assert embed.title.startswith("📂 Dataset:")
    assert "Dataset 1" in embed.title


@pytest.mark.asyncio
async def test_dataset_view_navigation():
    datasets = [
        {
            "id": 1,
            "name": "Dataset 1",
            "created_at": "01/01/2024",
            "authors": ["Author 1", "Author 2"],
        },
        {
            "id": 2,
            "name": "Dataset 2",
            "created_at": "02/02/2024",
            "authors": ["Author 3"],
        },
    ]
    view = DatasetView(datasets)

    interaction_mock = AsyncMock()
    interaction_mock.response.edit_message = AsyncMock()

    await view.next.callback(interaction_mock)

    assert view.current_page == 1

    interaction_mock.response.edit_message.assert_called_once()
    embed = interaction_mock.response.edit_message.call_args[1]["embed"]
    assert embed.title == f"📂 Dataset: {datasets[1]['name']}"
    assert "Author 3" in embed.fields[0].value
    assert "02/02/2024" in embed.fields[1].value

    interaction_mock.response.edit_message.reset_mock()

    await view.prev.callback(interaction_mock)

    assert view.current_page == 0

    interaction_mock.response.edit_message.assert_called_once()
    embed = interaction_mock.response.edit_message.call_args[1]["embed"]
    assert embed.title == f"📂 Dataset: {datasets[0]['name']}"
    assert "Author 1, Author 2" in embed.fields[0].value
    assert "01/01/2024" in embed.fields[1].value
