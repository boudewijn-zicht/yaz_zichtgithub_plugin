import yaz

from .log import logger, set_verbose


class ZichtGithub(yaz.BasePlugin):
    @yaz.task
    async def hello_world(self, greeting: str = "Hello World!", shout: bool = False, verbose: bool = False):
        set_verbose(verbose)
        if shout:
            greeting = greeting.upper()
        logger.debug("Sending greeting")
        return greeting
