import nextcord
import logging
from nextcord.ext import commands
from nextcord import Embed, Colour
from dotenv import load_dotenv
from app.modules.dataset.services import DataSetService, AuthorService
from app.modules.featuremodel.services import FeatureModelService
from app.modules.auth.services import AuthenticationService
import os
import matplotlib.pyplot as plt
import io
from app import app
import textwrap

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nextcord")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter
logger.addHandler(handler)

bot = commands.Bot()

dataset_service = DataSetService()
feature_model_service = FeatureModelService()
auth_service = AuthenticationService()
author_service = AuthorService()

DOMAIN = os.getenv("DOMAIN")


@bot.event
async def on_ready():
    try:
        # Sincroniza comandos globales
        await bot.sync_application_commands()
        print("Comandos globales sincronizados.")

    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

    print(f"Bot conectado como {bot.user}!")


@bot.event
async def on_guild_join(guild):
    general_channel = next(
        (
            channel
            for channel in guild.text_channels
            if channel.permissions_for(guild.me).send_messages
        ),
        None,
    )
    if general_channel:
        embed = Embed(
            title="¡Gracias por añadirme! 🎉",
            description=(
                "¡Hola a todos! 🎉 \n"
                "Gracias por añadirme. Soy un bot diseñado para ayudarte con algunas utilidades de uvlhub "
                "como gestionar datasets y más.\n"
                "Usa /help para ver mis comandos disponibles. ¡Empecemos! 🚀"
            ),
            colour=Colour.blue(),
        )
        embed.set_footer(text="Usa /help para más información.")
        await general_channel.send(embed=embed)


@bot.slash_command(name="help", description="Muestra los comandos disponibles")
async def help_command(interaction: nextcord.Interaction):
    # Define las categorías de comandos
    commands_info = {
        "📂 Gestión de Datasets": [
            {"name": "/most_downloaded", "description": "Dataset más descargado."},
            {"name": "/datasets", "description": "Muestra los datasets disponibles."},
            {
                "name": "/datasets_counter",
                "description": "Cuenta de datasets sincronizados.",
            },
        ],
        "📊 Estadísticas Generales": [
            {
                "name": "/total_dataset_downloads",
                "description": "Total de descargas de datasets.",
            },
            {
                "name": "/total_dataset_views",
                "description": "Total de vistas de datasets.",
            },
        ],
        "🔧 Modelos de Características": [
            {
                "name": "/feature_models_counter",
                "description": "Cuenta de modelos de características.",
            },
            {
                "name": "/total_feature_model_downloads",
                "description": "Total de descargas de modelos de características.",
            },
            {
                "name": "/total_feature_model_views",
                "description": "Total de vistas de modelos de características.",
            },
        ],
        "📚 Autores": [
            {
                "name": "/most_popular_authors",
                "description": "Muestra los autores más populares.",
            },
        ],
    }

    # Crear un embed principal
    embed = nextcord.Embed(
        title="📖 Ayuda del Bot",
        description=(
            "Aquí tienes la lista de comandos disponibles para interactuar con este bot.\n\n"
            "Cada comando está organizado por categoría. Usa el comando que desees ¡y comienza a explorar! 🚀\n\n"
            "Si tienes dudas o problemas, contacta con los administradores del bot. 😊"
        ),
        colour=nextcord.Colour.blue(),
    )
    embed.set_footer(text="Gracias por usar el bot. ¡Disfruta explorando tus datos!")

    # Añadir comandos por categoría
    for category, command in commands_info.items():
        commands_list = "\n".join(
            [f"**{cmd['name']}**: {cmd['description']}" for cmd in command]
        )
        embed.add_field(name=category, value=commands_list, inline=False)

    # Responder con el embed
    await interaction.response.send_message(embed=embed)


@bot.slash_command(name="most_downloaded", description="Dataset más descargado")
async def most_downloaded(interaction: nextcord.Interaction):
    with app.app_context():
        # Consulta de los datasets más descargados
        consult = dataset_service.most_downloaded()

        if not consult:  # Manejo adecuado si consult es None o está vacío
            embed = nextcord.Embed(
                title="Sin datos disponibles 😔",
                description=(
                    "No hay datos sobre los **datasets más descargados** en este momento.\n"
                    "Prueba a descargar alguno en la web de UVLHub: "
                    "[UVLHub](https://tortilla-hub-development.onrender.com)."
                ),
                color=nextcord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Obtén los 4 más descargados
        top_datasets = sorted(consult, key=lambda x: x["downloads"], reverse=True)[:4]

        # Extrae nombres y descargas
        names = [dataset["name"] for dataset in top_datasets]
        downloads = [dataset["downloads"] for dataset in top_datasets]

        # Ajustar nombres largos
        wrapped_names = [textwrap.fill(name, width=10) for name in names]

        # Crear colores distintos para cada barra
        colors = plt.cm.tab10(range(len(wrapped_names)))

        # Crear el gráfico de barras
        plt.figure(figsize=(8, 6))
        bars = plt.bar(range(len(wrapped_names)), downloads, color=colors)

        # Agregar etiquetas encima de las barras
        for bar, download in zip(bars, downloads):
            plt.text(
                bar.get_x() + bar.get_width() / 2,  # Posición horizontal
                bar.get_height() + 0.1,  # Posición vertical
                str(download),  # Valor a mostrar
                ha="center",
                va="bottom",
                fontsize=10,
            )

        plt.title("Top 4 Datasets Más Descargados", fontsize=14, pad=20)
        plt.xlabel("Datasets", fontsize=12)
        plt.ylabel("Descargas", fontsize=12)
        plt.yticks(range(0, max(downloads) + 1, 1))
        plt.xticks(range(len(wrapped_names)), wrapped_names, rotation=45, ha="right")

        # Guardar el gráfico en un buffer de memoria
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        plt.close()

        # Crear un embed
        embed = nextcord.Embed(
            title="Gráfico de descargas 📊",
            description=(
                "A continuación se muestra un gráfico de los **4 datasets más populares** "
                "según el número de descargas totales:\n\n"
                "• Cada barra representa un dataset con un color único.\n"
                "• Los nombres de los datasets están ajustados para encajar.\n"
                "• Los valores en la parte superior de cada barra muestran el total de descargas.\n\n"
                "⬇️ **Explora los resultados a continuación:** ⬇️"
            ),
            color=nextcord.Color.purple(),
        )

        # Enviar el gráfico como archivo adjunto
        file = nextcord.File(buffer, filename="top_datasets.png")
        embed.set_image(url="attachment://top_datasets.png")

        await interaction.response.send_message(embed=embed, file=file)


@bot.slash_command(
    name="datasets_counter", description="Cuenta de datasets sincronizados"
)
async def datasets_counter(interaction: nextcord.Interaction):
    with app.app_context():
        count = dataset_service.count_synchronized_datasets()

        embed = nextcord.Embed(
            title="Total de Datasets Sincronizados 🗂️",
            description=(
                f"Actualmente hay **{count} datasets sincronizados** en la base de datos.\n\n"
                "🔍 Puedes explorar los datasets disponibles usando otros comandos como: \n - /datasets\n"
                "🚀 ¡Sigue gestionando y explorando tus datasets con facilidad!"
            ),
            color=nextcord.Color.purple(),
        )

        await interaction.response.send_message(embed=embed)


@bot.slash_command(
    name="feature_models_counter", description="Cuenta de modelos de características"
)
async def feature_models_counter(interaction: nextcord.Interaction):
    with app.app_context():
        count = feature_model_service.count_feature_models()

        embed = nextcord.Embed(
            title="Total de Modelos de Características 🔧",
            description=(
                f"Actualmente hay **{count} modelos de características** registrados en la base de datos.\n\n"
                "💡 Los modelos de características pueden ser utilizados para mejorar tus datasets.\n"
                "🔍 Explora y gestiona los modelos disponibles con otros comandos."
            ),
            color=nextcord.Color.green(),
        )

        await interaction.response.send_message(embed=embed)


@bot.slash_command(
    name="total_dataset_downloads", description="📈 Total de descargas de datasets"
)
async def total_dataset_downloads(interaction: nextcord.Interaction):
    with app.app_context():
        total_downloads = dataset_service.total_dataset_downloads()

        embed = nextcord.Embed(
            title="📈 Total de Descargas de Datasets",
            description=(
                f"En total, los datasets han sido descargados **{total_downloads} veces**.\n\n"
                "📥 Las descargas de datasets son una medida importante para ver qué tan populares "
                "son los recursos disponibles.\n"
                "🔍 Explora más comandos para conocer detalles adicionales sobre los datasets."
            ),
            color=nextcord.Color.orange(),
        )

        await interaction.response.send_message(embed=embed)


# Total de descargas de modelos de características
@bot.slash_command(
    name="total_feature_model_downloads",
    description="📈 Total de descargas de modelos de características",
)
async def total_feature_model_downloads(interaction: nextcord.Interaction):
    with app.app_context():
        total_downloads = feature_model_service.total_feature_model_downloads()
        embed = Embed(
            title="📊 Total de Descargas de Modelos de Características",
            description=(
                f"Nuestros modelos de características han sido descargados un total de **{total_downloads} veces**. "
                "¡Gracias por tu interés! 🌟"
            ),
            colour=nextcord.Color.green(),
        )
        await interaction.response.send_message(embed=embed)


# Total de vistas de datasets
@bot.slash_command(
    name="total_dataset_views", description="👀 Total de vistas de datasets"
)
async def total_dataset_views(interaction: nextcord.Interaction):
    with app.app_context():
        total_views = dataset_service.total_dataset_views()
        embed = Embed(
            title="👀 Total de Vistas de Datasets",
            description=(
                f"Nuestros datasets han sido vistos un total de **{total_views} veces**. "
                "¡Estamos felices de que explores nuestros datos! 🔍"
            ),
            colour=Colour.orange(),
        )
        await interaction.response.send_message(embed=embed)


# Total de vistas de modelos de características
@bot.slash_command(
    name="total_feature_model_views",
    description="🔍 Total de vistas de modelos de características",
)
async def total_feature_model_views(interaction: nextcord.Interaction):
    with app.app_context():
        total_views = feature_model_service.total_feature_model_views()
        embed = Embed(
            title="🔍 Total de Vistas de Modelos de Características",
            description=(
                f"Nuestros modelos de características han sido vistos **{total_views} veces**. "
                "¡Nos encanta compartir conocimiento contigo! 📘"
            ),
            colour=Colour.green(),
        )
        await interaction.response.send_message(embed=embed)


# DatasetView - Navegación de datasets mejorada
class DatasetView(nextcord.ui.View):
    def __init__(self, datasets):
        super().__init__()
        self.datasets = datasets
        self.current_page = 0

    async def update_message(self, interaction):
        dataset = self.datasets[self.current_page]
        embed = Embed(
            title=f"📂 Dataset: {dataset['name']}",
            description="Aquí tienes más información sobre este dataset:",
            colour=Colour.purple(),
        )
        embed.add_field(
            name="🧑‍💻 Autor/es",
            value=(
                ", ".join(dataset["authors"]) if dataset["authors"] else "No disponible"
            ),
            inline=True,
        )
        embed.add_field(
            name="📅 Fecha de Creación", value=dataset["created_at"], inline=True
        )
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
        download_url = DOMAIN + f"/dataset/download/{dataset['id']}"
        await interaction.response.send_message(
            content=f"[Haz clic aquí para descargar el dataset]({download_url})",
            ephemeral=True,
        )

    @nextcord.ui.button(label="Descargar todos", style=nextcord.ButtonStyle.success)
    async def download_all(self, button, interaction):
        download_url = DOMAIN + "/dataset/download_all"
        await interaction.response.send_message(
            content=f"[Haz clic aquí para descargar todos los datasets disponibles]({download_url})",
            ephemeral=True,
        )

    @nextcord.ui.button(label="Siguiente", style=nextcord.ButtonStyle.primary)
    async def next(self, button, interaction):
        if self.current_page < len(self.datasets) - 1:
            self.current_page += 1
            await self.update_message(interaction)


# Comando datasets
@bot.slash_command(name="datasets", description="📚 Muestra los datasets disponibles")
async def show_datasets(interaction: nextcord.Interaction):
    with app.app_context():
        datasets = dataset_service.get_all_datasets()
        formatted_datasets = [
            {
                "id": dataset.id,
                "name": dataset.name(),
                "created_at": dataset.created_at.strftime("%d/%m/%Y"),
                "authors": [
                    author.to_dict()["name"] for author in dataset.ds_meta_data.authors
                ],
            }
            for dataset in datasets
        ]

        view = DatasetView(formatted_datasets)
        dataset = formatted_datasets[0]
        embed = Embed(
            title=f"📂 Dataset: {dataset['name']}",
            description="Aquí tienes información sobre el primer dataset:",
            color=nextcord.Color.purple(),
        )
        embed.add_field(
            name="🧑‍💻 Autor/es",
            value=(
                ", ".join(dataset["authors"]) if dataset["authors"] else "No disponible"
            ),
            inline=True,
        )
        embed.add_field(
            name="📅 Fecha de Creación", value=dataset["created_at"], inline=True
        )
        embed.set_footer(text=f"Página 1/{len(formatted_datasets)}")
        await interaction.response.send_message(embed=embed, view=view)


@bot.slash_command(
    name="most_popular_authors", description="📚 Muestra los autores más populares"
)
async def most_popular_authors(interaction: nextcord.Interaction):
    with app.app_context():
        # Obtén los autores más populares desde el servicio
        most_popular_authors = author_service.most_popular_authors()

        # Verifica si hay autores disponibles
        if not most_popular_authors:
            await interaction.response.send_message(
                "No hay datos sobre autores populares en este momento. 😔",
                ephemeral=True,
            )
            return

        # Formatear los datos de los autores en una lista
        embed = Embed(
            title="📚 Autores Más Populares",
            description="Aquí tienes la lista de los autores más destacados basados en sus descargas:",
            colour=Colour.yellow(),
        )

        for author in most_popular_authors:
            # Añade cada autor como un campo en el embed
            embed.add_field(
                name=f"👤 {author['name']}",
                value=f"**Descargas:** {author['downloads']}",
                inline=False,  # Muestra cada autor en una línea separada
            )

        embed.set_footer(text="Gracias por apoyar a nuestros creadores. 🌟")

        # Envía el embed
        await interaction.response.send_message(embed=embed)


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
