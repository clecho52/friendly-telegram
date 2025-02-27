from .. import loader, utils
import logging, subprocess, platform

logger = logging.getLogger(__name__)

def register(cb):
    cb(InfoMod())


class InfoMod(loader.Module):
    """Provides system information about the computer hosting this bot"""
    def __init__(self):
        self.commands = {'info': self.infocmd}
        self.config = {}
        self.name = "Info"

    async def infocmd(self, message):
        reply = "<code>System Info\nKernel: " + utils.escape_html(platform.release())
        reply += "\nArch: " + utils.escape_html(platform.architecture()[0])
        reply += "\nOS: " + utils.escape_html(platform.system())

        if platform.system() == 'Linux':
            a = open('/etc/os-release').readlines()
            b = {}
            for line in a:
                b[line.split('=')[0]] = line.split('=')[1].strip().strip('"')

            reply += "\nLinux Distribution: " + utils.escape_html(b["PRETTY_NAME"])
        reply += "\nMisc"
        reply += "\nPython version: " + utils.escape_html(platform.python_version())
        reply += '</code>'
        logger.debug(reply)
        await message.edit(reply, parse_mode="HTML")
