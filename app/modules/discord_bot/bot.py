import nextcord
import logging
from nextcord.ext import commands, menus
from dotenv import load_dotenv
from app.modules.dataset.services import DataSetService
from app.modules.featuremodel.services import FeatureModelService
from app.modules.auth.services import AuthenticationService
import os
from app import app

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('nextcord')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter
logger.addHandler(handler)

bot = commands.Bot()

dataset_service = DataSetService()
feature_model_service = FeatureModelService()
auth_service = AuthenticationService()

TESTING_GUILD_ID = int(os.getenv('TESTING_GUILD_ID'))
DOMAIN = os.getenv('DOMAIN')


@bot.slash_command(name="ping", description="Revisa la latencia del bot", guild_ids=[TESTING_GUILD_ID])
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("¡Pong!")


@bot.slash_command(name="most_downloaded", description="Dataset más descargado", guild_ids=[TESTING_GUILD_ID])
async def most_downloaded(interaction: nextcord.Interaction):
    with app.app_context():
        consult = dataset_service.most_downloaded()
        name = consult[0].name
        downloads = consult[0].downloads
        await interaction.response.send_message(f"El dataset más descargado es {name} con {downloads} descargas")


@bot.slash_command(name="datasets_counter", description="Cuenta de datasets sincronizados", guild_ids=[TESTING_GUILD_ID])
async def datasets_counter(interaction: nextcord.Interaction):
    with app.app_context():
        count = dataset_service.count_synchronized_datasets()
        await interaction.response.send_message(f"Total de datasets sincronizados: {count}")


@bot.slash_command(name="feature_models_counter", description="Cuenta de modelos de características", guild_ids=[TESTING_GUILD_ID])
async def feature_models_counter(interaction: nextcord.Interaction):
    with app.app_context():
        count = feature_model_service.count_feature_models()
        await interaction.response.send_message(f"Total de modelos de características: {count}")


@bot.slash_command(name="total_dataset_downloads", description="Total de descargas de datasets", guild_ids=[TESTING_GUILD_ID])
async def total_dataset_downloads(interaction: nextcord.Interaction):
    with app.app_context():
        total_downloads = dataset_service.total_dataset_downloads()
        await interaction.response.send_message(f"Total de descargas de datasets: {total_downloads}")


@bot.slash_command(name="total_feature_model_downloads", description="Total de descargas de modelos de características", guild_ids=[TESTING_GUILD_ID])
async def total_feature_model_downloads(interaction: nextcord.Interaction):
    with app.app_context():
        total_downloads = feature_model_service.total_feature_model_downloads()
        await interaction.response.send_message(f"Total de descargas de modelos de características: {total_downloads}")


@bot.slash_command(name="total_dataset_views", description="Total de vistas de datasets", guild_ids=[TESTING_GUILD_ID])
async def total_dataset_views(interaction: nextcord.Interaction):
    with app.app_context():
        total_views = dataset_service.total_dataset_views()
        await interaction.response.send_message(f"Total de vistas de datasets: {total_views}")


@bot.slash_command(name="total_feature_model_views", description="Total de vistas de modelos de características", guild_ids=[TESTING_GUILD_ID])
async def total_feature_model_views(interaction: nextcord.Interaction):
    with app.app_context():
        total_views = feature_model_service.total_feature_model_views()
        await interaction.response.send_message(f"Total de vistas de modelos de características: {total_views}")


@bot.slash_command(name="login", description="Inicia sesión en la aplicación", guild_ids=[TESTING_GUILD_ID])
async def login(interaction: nextcord.Interaction, username: str, password: str):
    with app.app_context():
        user = auth_service.login(username, password)
        if user:
            await interaction.response.send_message("¡Inicio de sesión exitoso!")
        else:
            await interaction.response.send_message("Credenciales incorrectas. Inténtalo de nuevo.")


class DatasetView(nextcord.ui.View):
    def __init__(self, datasets):
        super().__init__()
        self.datasets = datasets
        self.current_page = 0

    async def update_message(self, interaction):
        dataset = self.datasets[self.current_page]
        embed = nextcord.Embed(title=f"Dataset: {dataset['name']}")
        embed.add_field(name="ID", value=dataset['id'], inline=True)
        embed.set_footer(text=f"Página {self.current_page + 1}/{len(self.datasets)}")
        await interaction.response.edit_message(embed=embed, view=self)

    @nextcord.ui.button(label="Anterior", style=nextcord.ButtonStyle.primary)
    async def prev(self, button, interaction):
        if self.current_page > 0:
            self.current_page -= 1
            await self.update_message(interaction)

    @nextcord.ui.button(label="Descargar", style=nextcord.ButtonStyle.success)
    async def download(self, button, interaction):
        dataset = self.datasets[self.current_page]
        # Endpoint real
        download_url = DOMAIN + f"/dataset/download/{dataset['id']}" 
        await interaction.response.send_message(f"[Haz clic aquí para descargar el dataset]({download_url})", ephemeral=True)

    @nextcord.ui.button(label="Siguiente", style=nextcord.ButtonStyle.primary)
    async def next(self, button, interaction):
        if self.current_page < len(self.datasets) - 1:
            self.current_page += 1
            await self.update_message(interaction)


@bot.slash_command(name="datasets", description="Muestra los datasets disponibles", guild_ids=[TESTING_GUILD_ID])
async def show_datasets(interaction: nextcord.Interaction):
    # Obtén los datasets desde tu servicio
    with app.app_context():
        datasets = dataset_service.get_all_datasets()
        formatted_datasets = [
            {
                "id": dataset.id,
                "name": dataset.name,
            }
            for dataset in datasets
        ]

        # Crea la vista
        view = DatasetView(formatted_datasets)
        dataset = formatted_datasets[0]  # Primer dataset
        embed = nextcord.Embed(title=f"Dataset: {dataset['name']}")
        embed.add_field(name="ID", value=dataset['id'], inline=True)
        embed.set_footer(text=f"Página 1/{len(formatted_datasets)}")

        await interaction.response.send_message(embed=embed, view=view)


if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))

