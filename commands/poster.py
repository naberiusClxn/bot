import disnake
from disnake.ext import commands
from ..config import ROLE_PERMISIONS

class PosterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, interaction: disnake.ApplicationCommandInteraction):
        user_roles = [role.id for role in interaction.author.roles]
        return any(role in ROLE_PERMISIONS for role in user_roles)

    @commands.slash_command(description="Создать сообщение об афише")
    async def poster(
        self,
        inter: disnake.AppCmdInter,
        title: str = commands.Param(name="название", description="Название афиши"),
        duration: str = commands.Param(name="длительность", description="Длительность события"),
        genre: str = commands.Param(name="жанр", description="Жанр события"),
        age: str = commands.Param(name="возраст", description="Возрастные ограничения"),
        description: str = commands.Param(name="описание", description="Описание события"),
        event_url: str = commands.Param(name="событие_url", description="Ссылка на событие"),
        photo_url: str = commands.Param(name="фото_url", description="Ссылка на изображение")
    ):
        if not self.is_admin(inter):
            await inter.response.send_message("У вас нет прав для выполнения этой команды.", ephemeral=True)
            return

        embed = disnake.Embed(
            description=(
                f"# {title} \n\n"
                f"**Длительность:** {duration}\n"
                f"**Жанр:** {genre}\n"
                f"**Возраст:** {age}\n\n"
                f"> {description}"
            ),
            color=disnake.Color.dark_gray()
        )
        embed.set_author(
            name=f"{inter.author.display_name}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None
        )

        if photo_url:
            embed.set_image(url=photo_url)

        await inter.response.send_message(content=f"{event_url}", embed=embed)

def setup(bot):
    bot.add_cog(PosterCog(bot))
