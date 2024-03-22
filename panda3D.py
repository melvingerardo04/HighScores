from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase


actor = Actor('models/panda-model', {
    'walk': 'models/panda-walk4',
    # 'swim': 'hero-swim.egg',
})

actor.play('walk')

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)