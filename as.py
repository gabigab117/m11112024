import asyncio


async def tache_longue(nom: str) ->  None:
    print(f"Début de {nom}")
    await asyncio.sleep(3) # passe la main à une autre tache
    print(f"Fin de {nom}")


async def main():
    task1 = asyncio.create_task(tache_longue("1"))
    task2 = asyncio.create_task(tache_longue("2"))

    await task1
    await task2

    print("Terminé")


asyncio.run(main())
