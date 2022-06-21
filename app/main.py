#!/usr/bin/env python3

import os

import redis
from discord.ext.commands import Bot, Cog, when_mentioned_or


class ReactionCounter(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot


class MyBot(Bot):
    def __init__(self, redis_client) -> None:
        super().__init__(command_prefix=when_mentioned_or("!"))
        self.redis = redis_client
        self.add_cog(ReactionCounter(self))

    async def on_ready(self) -> None:
        print(self.user.name)
        print(self.user.id, "\n")


def main() -> None:
    print("a")
    redis_client = redis.Redis("redis")
    print("b")
    bot = MyBot(redis_client)
    print("c")
    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()
