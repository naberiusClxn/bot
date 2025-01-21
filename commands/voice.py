import disnake
from disnake.ext import commands
from .. config import ROLE_PERMISIONS

class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, interaction: disnake.ApplicationCommandInteraction):

        user_roles = [role.id for role in interaction.author.roles]
        return any(role in ROLE_PERMISIONS for role in user_roles)

    @commands.slash_command(description="Создать сообщение об озвучке")
    async def voice(
        self,
        inter: disnake.AppCmdInter,
        title: str = commands.Param(name="название", description="Название аниме"),
        description: str = commands.Param(name="описание", description="Описание озвучки"),
        voice_link: str = commands.Param(name="ссылка_на_войс", description="Ссылка на войс-канал"),
        hosts: str = commands.Param(name="ведущие", description="Ведущие озвучки"),
        photo_url: str = commands.Param(name="фото_url", description="Ссылка на изображение", default=None)
    ):
        if not self.is_admin(inter):
            await inter.response.send_message("У вас нет прав для выполнения этой команды.", ephemeral=True)
            return

        embed = disnake.Embed(
            description=(
                f"## ОЗВУЧКА \n\n"
                f"**Аниме:** {title}\n"
                f"**Ведущие:** {hosts}\n\n"
                f"> {description}"
            ),
            color=disnake.Color.dark_gray()
        )

        if photo_url:
            embed.set_image(url=photo_url)

        await inter.response.send_message(content=f"{voice_link}", embed=embed)

def setup(bot):
    bot.add_cog(VoiceCog(bot))
