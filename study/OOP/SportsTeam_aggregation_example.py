#Super interesting to brush up real world objects relationship problems


class Player:

    def __init__(self, ID=0, name=None, teamName=None):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:

    def __init__(self, name=None):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)  #how can I get the player object here

    def getNumberOfPlayers(self):
        return len(self.players)


class School:

    def __init__(self, teams=None, name=None):
        self.teams = []
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length


