from collective.grok import gs
from agape.theme import MessageFactory as _

@gs.importstep(
    name=u'agape.theme', 
    title=_('agape.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('agape.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
