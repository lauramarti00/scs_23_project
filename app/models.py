from app import db

class TitleCrew(db.Model):
    tconst = db.Column(db.String(64), primary_key=True)
    directors = db.Column(db.String(64))
    writers = db.Column(db.String(120))

    def __repr__(self):
        return '<TitleCrew {}>'.format(self.username)
    



class TitleAkas(db.Model):
    titleId = db.Column(db.String(200), primary_key=True)
    ordering = db.Column(db.Integer )
    title = db.Column(db.String(200))
    region = db.Column(db.String(200))
    language = db.Column(db.String(200))
    types = db.Column(db.String(200))
    attributes = db.Column(db.String(200))
    isOriginalTitle = db.Column(db.Boolean)

    def __repr__(self):
        return '<TitleAkas {}>'.format(self.username)
    

class TitleBasics(db.Model):
    tconst = db.Column(db.String(200), primary_key=True)
    titleType = db.Column(db.String(200) )
    primaryTitle = db.Column(db.String(200))
    originalTitle = db.Column(db.String(200))
    isAdult = db.Column(db.Boolean)
    startYear = db.Column(db.Integer)
    endYear = db.Column(db.Integer)
    runtimeMinutes = db.Column(db.String(200))
    genres = db.Column(db.String(500))

    #relationships
    episodes = db.relationship('TitleEpisode', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<TitleBasics {}>'.format(self.username)
    

class TitleEpisode(db.Model):
    tconst = db.Column(db.String(200), primary_key=True)
    parentTconst = db.Column(db.String(200), db.ForeignKey('title_basics.tconst'))
    seasonNumber = db.Column(db.Integer)
    episodeNumber = db.Column(db.Integer)
    
    def __repr__(self):
        return '<TitleEpisode {}>'.format(self.username)
    

class TitleRatings(db.Model):
    tconst = db.Column(db.String(200), primary_key=True)
    averageRating = db.Column(db.Float)
    numVotes = db.Column(db.Integer)
    
    
    def __repr__(self):
        return '<TitleRatings {}>'.format(self.username)
    

class NameBasics(db.Model):
    nconst = db.Column(db.String(200), primary_key=True)
    primaryName = db.Column(db.String(200))
    birthYear = db.Column(db.Integer)
    deathYear = db.Column(db.Integer)
    primaryProfession = db.Column(db.String(500))
    knownForTitles = db.Column(db.String(500))
    
    
    def __repr__(self):
        return '<NameBasics {}>'.format(self.username)
    