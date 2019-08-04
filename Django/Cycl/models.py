from django.db import models
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=100)
    session = models.IntegerField(null=True)
    startDate = models.DateTimeField(null=False,
                                     verbose_name="When the race starts")
    finishDate = models.DateTimeField(null=False,
                                      verbose_name="When the race ends")
    series = models.ForeignKey('Serie', default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ['startDate']

    def __str__(self):
        return self.name + ' - ' + str(self.startDate.year)


class Stage(models.Model):
    name = models.CharField(max_length=150)
    kilometers = models.FloatField(default=0)
    start = models.CharField(max_length=100)
    finish = models.CharField(max_length=100)
    date = models.DateTimeField(null=False)
    race = models.ForeignKey('Race', default=1, on_delete=models.CASCADE)
    parcours = models.ForeignKey('Parcours',
                                 default=1,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return (self.name + ' : ' + self.start + ' > ' + self.finish + ' (' +
                str(self.kilometers) + 'k)')


class Serie(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.name + ' - ' + self.text


class Parcours(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Parcours"

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, null=False)
    abreviation = models.CharField(max_length=3, null=False, default="ABC")
    bike = models.CharField(max_length=30, null=True)
    nation = models.CharField(max_length=50, null=True)
    continent = models.CharField(max_length=50, null=True)
    category = models.ForeignKey("Teamcategory",
                                 default=1,
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Teamcategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    label = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name_plural = "Teamcategories"

    def __str__(self):
        return self.name + ' : ' + self.label


class Staff(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    birthDate = models.DateTimeField(null=True)
    nation = models.ForeignKey("Country", on_delete=models.CASCADE, default=1)
    continent = models.CharField(max_length=50, null=True)
    uciid = models.CharField(max_length=11, null=True)
    function = models.CharField(max_length=50)
    team = models.ManyToManyField(Team, related_name="+", through="Manage")

    class Meta:
        # unique_together = ('lastName', 'firstName')
        ordering = ['lastName', 'firstName']

    def __str__(self):
        return self.lastName + ' ' + self.firstName + ' (' + self.nation + ')'


class Rider(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    birthDate = models.DateTimeField(null=True)
    birthPlace = models.CharField(max_length=100, null=True)
    nation = models.ForeignKey("Country", on_delete=models.CASCADE, default=1)
    continent = models.CharField(max_length=50, null=True)
    weigth = models.FloatField(null=True)
    height = models.FloatField(null=True)
    uciid = models.CharField(max_length=11, null=True)
    uciRank = models.IntegerField(null=True)
    pcsRank = models.IntegerField(null=True)
    team = models.ManyToManyField(Team, related_name="+", through="Lineup")
    stage = models.ManyToManyField(Stage, related_name="+", through="Result")
    startList = models.ManyToManyField(Stage,
                                       related_name="+",
                                       through="StartList")
    race = models.ManyToManyField(Race, related_name="+", through="Register")

    class Meta:
        unique_together = ('lastName', 'firstName', 'uciid')
        ordering = ['lastName', 'firstName']

    def __str__(self):
        return self.lastName + ' ' + self.firstName + ' (' + self.nation + ')'


class Lineup(models.Model):
    arrivalDate = models.DateTimeField(null=False,
                                       default=timezone.now,
                                       verbose_name="Rider arrives in team")
    leavingDate = models.DateTimeField(blank=True,
                                       null=True,
                                       verbose_name="Rider leaves the team")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)

    class Meta:
        ordering = ['rider']

    def __str__(self):
        return self.rider.lastName + ' in ' + self.team.name


class Manage(models.Model):
    startDate = models.DateTimeField(null=False,
                                     default=timezone.now,
                                     verbose_name="Manager arrives in team")
    leavingDate = models.DateTimeField(blank=True,
                                       null=True,
                                       verbose_name="Manager leaves the team")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        ordering = ['staff']

    def __str__(self):
        return self.staff.lastName + ' ' + self.staff.firstName + ' is ' + self.staff.function + ' of ' + self.team.name


class Country(models.Model):
    name = models.CharField(max_length=100, null=False)
    alpha2Code = models.CharField(max_length=2, null=False)
    alpha3Code = models.CharField(max_length=3, null=False)
    numericCode = models.IntegerField()

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ('alpha3Code',)
        unique_together = ('alpha3Code',)

    def __str__(self):
        return self.name


class Result(models.Model):
    rank = models.IntegerField(null=False)
    time = models.TimeField(null=True)
    stagePoints = models.IntegerField(null=True)
    sprintPoints = models.IntegerField(null=True)
    komPoints = models.IntegerField(null=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stage', 'rider')

    def __str__(self):
        return (self.rider.lastName + ' is #' + str(self.rank) + ' of stage ' +
                self.stage.name + ' with time : ' + str(self.time))


class Register(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    bib = models.IntegerField(null=False)

    class Meta:
        unique_together = ('race', 'rider')

    def __str__(self):
        return self.rider.lastName + ' is BIB #' + str(self.bib)


class StartList(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    atStart = models.BooleanField(default=1)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('stage', 'rider')

    def __str__(self):
        if self.atStart:
            return self.rider.lastName + ' will ride stage ' + self.stage.name
        else:
            return (self.rider.lastName + ' won\'t ride stage ' +
                    self.stage.name)


class Player(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=150)
    playerName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    isPremium = models.BooleanField(default=False)
    lastLogin = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['lastName', 'firstName']

    def __str__(self):
        return self.lastName.upper() + ' ' + self.firstName


class Roster(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'stage', 'rider')

    def __str__(self):
        return (self.player.playerName + ' bet on ' + self.rider.lastName +
                ' for stage ' + self.stage.name)


class Ranking(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    rosterTotalTime = models.TimeField(null=True)
    rosterRank = models.IntegerField()
    rosterPointsEarned = models.IntegerField()
    additionnalPoints = models.IntegerField()

    class Meta:
        unique_together = ('player', 'stage')

    def __str__(self):
        return ('Player ' + self.player.playerName + ' earned a total of ' +
                str(self.rosterPointsEarned) + ' + ' +
                str(self.additionnalPoints) + ' points for stage ' +
                self.stage.name + '. Player is #' + str(self.rosterRank))
