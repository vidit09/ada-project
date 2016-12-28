from pyspark.sql import SQLContext
from pyspark import SparkContext

if __name__ == "__main__":
    #inp_file = "hdfs:///datasets/reddit/RS_full_corpus.bz2"  # Submission
    inp_file = "hdfs:///datasets/reddit/comments/2015"
    #inp_file = "hdfs:///datasets/reddit/comments/2015/RC_2015-08.bz2"
    sc = SparkContext()
    sqlContext = SQLContext(sc)

    df = sqlContext.read.json(inp_file)

    '''
    ############################## Switzerland ########################################################
    swiss_subreddit_list = ['Switzerland', 'AskSwitzerland', 'Basel', 'Bern', 'BielBienne', 'Buenzli',
     'Frauenfeld', 'Fribourg', 'Geneva', 'Liestal', 'Luzern', 'Morcote', 'Neuchatel', 'Schaffhausen', 
     'SanktGallen', 'Schwiiz', 'Solothurn', 'Stans', 'Suisse', 'Thun', 'Ticino', 'Winterthur', 'Zermatt', 
     'Zug', 'Zurich', 'Breitling', 'CHTrees', 'FCBasel', 'MatterhornPorn', 'Migros', 'Schweiz', 'SwissArmy',
      'SwissArmyKnives', 'SwissBuyers', 'SwissGaming', 'SwissGuns', 'SwissHockey', 'SwissESports', 
      'SwissMountainDogs', 'SwissNews', 'SwissProblems', 'SwissRap', 'SwissSuperLeague', 'SwissHistory', 
      'CERN', 'EPFL', 'ETHZ', 'UZH']
    filt_df = df.filter(df['subreddit'].isin(swiss_subreddit_list))
    '''

    ####################################### Europe: Germany, France, Italy, Spain ########################################################
    europe_subreddit_list = ['germany', 'de', 'German', 'GermanPractice', 'GermanFacts', 'GermanConversation',                  ## germany
     'SCHLAND', 'germanyusa', 'DEjobs', 'bundesliga', 'GermanyPics', 'germusic', 'de_punk', 'germanrap', 'NDH',                 ## germany
     'blagues', 'cinemacinema', 'europe', 'france', 'FrancePics', 'frenchelectro', 'Frenchhistory', 'guessthefrenchmovie',      ## france
     'Ligue1', 'Livres', 'musiquefrancaise', 'paris', 'pedale', 'philosophie', 'Politique', 'rance', 'ScienceFr', 'SocialFrance',## france
     'Calcio', 'ITAGLIA', 'Italianhistory', 'ITALIANMUSIC', 'italy', 'ItalyPhotos', 'Libri', 'Abruzzo', 'Apulia', 'bari',       ## italy
     'Basilicata', 'bologna', 'Calabria', 'Campania', 'Catania', 'emilia_romagna', 'firenze', 'friuli', 'Genova', 'Italia',     ## italy
     'lazio', 'Liguria', 'lombardia', 'Lombardy', 'marche', 'messina', 'milano', 'Modena', 'molise', 'Naples_Italy', 'napoli',  ## italy
     'padova', 'Palermo', 'Perugia', 'Piedmont', 'piemonte', 'Pisa', 'puglia', 'roma', 'rome', 'romesocialclub', 'Sardegna',    ## italy
     'Sardinia', 'Sicilia', 'sicily', 'Siracusa', 'torino', 'Toscana', 'trentino_alto_adige', 'trentod', 'Trieste',             ## italy
     'tuscany', 'Umbria', 'valle_daosta', 'Veneto', 'Venezia',                                                                  ## italy
     'Barcelona', 'EPANA', 'es', 'europe', 'futbol', 'Granada', 'LaLiga', 'Madrid', 'spain', 'Andalucia', 'SpanishHistory',     ## spain
     ] 
    filt_df = df.filter(df['subreddit'].isin(europe_subreddit_list))

    '''
    ############################################## United Kingdom ############################################################################
    uk_subreddit_list = ['AskUK', 'britpics', 'AskUK', 'english_articles', 'UKcirclejerk', 'Fringe', 'Humou', 'INGLIN', 'BritishProblems', 
     'TheRedLion', 'gbr4', 'BritishSuccess', 'TwoXUK', 'UKskeptic', 'PoliceUk', 'AskUK', 'GCSE', 'UKVisa', 'LegalAdviceUK', 
     'UKPersonalFinance', 'UKHistory', 'ScottishHistory', 'HistoryWales', 'UKLaw', 'UKLGBT', 'londonlgbt', 'bisexualuk', 'TransgenderUK',
     'BritishMilitary', 'UKNews', 'UKGoodNews', 'PrivateEye', 'edtop', 'MHoC', 'MHoCLabou', 'MHoCLiberalDemocrats', 'MHoCConservatives', 
     'MHoCUKIP', 'MHoCGreens', 'MHoCcommunist', 'MHoCBIP', 'MHoCCWL', 'MHoCIndependents', 'UKPolitics', 'BritishPolitics', 'LabourUK', 
     'Tories', 'LibDem', 'UKIPParty', 'UKGreens', 'PiratePartyUK', 'tusc', 'scottishpolitics', 'upliftingnewsuk', 'ukgovbriefs',
     'UKandIrishBee', 'UKBiscuits', 'ukcigars', 'UKTrees', 'UKBike', 'BristolCycling', 'cambridgecycling', 'leedscycling', 'londoncycling', 
     'cyclemc', 'scottishcycling', 'BTCC', 'BushcraftUK', 'findfashionuk', 'FitnessUK', 'EnglishFootballLeague', 'championship', 'League1', 
     'LeagueTwo', 'conferencefootball', 'ScottishFootball', 'UKGuns', 'HardwareSwapUK', 'UKHealthcare', 'UKHockey', 'KetoUK', 'MakeUpAddictionUK',
     'NFLUK', 'ukpoke', 'SkincareAddictionUK', 'UKSquaredCircle', 'surfuk', 'UKUltimate', 'BitcoinUK', 'dogecoinuk', 'ukforhire', 'freebiesUK', 
     'UKFrugal', 'UKInvesting', 'UKJobs', 'NightshiftUK', 'CarTalkUK', 'MotoUK', 'UKAutos', 'uktrains', 'britishfilms', 'UKFreeMovies', 'iplaye', 
     'BritishSoaps', 'BritishTV', 'UKVideos', 'watchthisuk', 'musicuk', 'ukmusic', 'UKbass', 'UKFunky', 'UKHipHopHeads', 'UKMusos', 'Punx', 
     'UKRave', 'llawenyddhebddiwedd', 'BritishRadio', 'UKgames', 'UKesportshub', 'GameDealsUK', 'UKDota', 'UKGaymers', 'UKIndies', 'UKStarcraft', 
     'ukbabes', 'BritishLadyBoners', 'Britpics', 'ScotlandPorn', 'unitedkingdom', 'Britain', 'England', 'thenorth', 'birkenhead', 'carlisle', 
     'Cheste', 'cumbria', 'darwen', 'fylde', 'Lancaster_uk', 'LancashireProblems', 'Liverpool', 'liverpoolcity', 'Mancheste', 'cyclemc', 
     'merseyside', 'mossley', 'preston', 'southport', 'warrington', 'wigan', 'wirral', 'northeast', 'alnwick', 'ashington', 'durhamuk',
     'morpeth', 'newcastleupontyne', 'Northumberland', 'peterlee', 'sunderland', 'teesside', 'Tyneside', 'whitleybay', 'bradford', 'dewsbury',
     'doncaste', 'goldsborough', 'grimsby', 'harrogate', 'huddersfield', 'hull', 'leeds', 'leedscycling', 'lincolnshire', 'ipponden',
     'scarboroughuk', 'Sheffield', 'wakefield', 'westyorkshire', 'York', 'yorkshire', 'midlands', 'westmidlands', 'brum', 'theblackcountry', 
     'coventry', 'hereford', 'kenilworth', 'shrewsburyuk', 'shropshire', 'stafford', 'staffordshire', 'warwickshire', 'wolverhampton', 'worceste', 
     'eastmidlands', 'beeston', 'caisto', 'chesterfielduk', 'cleethorpes', 'corby', 'daventry', 'derby', 'derbyshire', 'duffield', 'leiceste', 
     'lincolnshire', 'louth', 'northamptonians', 'nottingham', 'nottinghamshire', 'utland', 'worksop', 'westcountry', 'bath', 'bournemouth', 
     'braunton', 'bristol', 'BristolCycling', 'chippenham', 'cirenceste', 'cornwall', 'dartmoo', 'devonuk', 'dorset', 'exete', 'exmoo', 
     'gloucestershire', 'plymouth', 'salisburyUK', 'saltash', 'PooleBayCity', 'swindon', 'westlynndevon', 'wiltshire', 'yeovil', 
     'SouthEastEngland', 'amersham', 'basingstoke', 'bexhill', 'brighton', 'canterbury', 'chicheste', 'crawley', 'graveney', 'hampshire', 
     'hastings', 'highwycombearea', 'isleofwight', 'britishkent', 'margate', 'medway', 'midhurst', 'miltonkeynes', 'newforest', 'oxford', 
     'Portsmouth', 'amsgate', 'eading', 'slough', 'southampton', 'surrey', 'tadley', 'thanet', 'Tunbridgewells', 'winchesterUK', 'wokingham', 
     'worthing', 'London', 'basementboardgames', 'london_arts', 'londoncycling', 'london_entreprenuers', 'LondonFootballMeetup', 'london_forhire', 
     'londonlgbt', 'londonsocialclub', 'londonstudents', 'bromley', 'clapham', 'croydon', 'islington', 'aynes_park', 'omford', 'eastanglia', 
     'bedfordshire', 'cambridge', 'cambridgeshire', 'cambridgecycling', 'ely', 'Essex', 'fenland', 'greatyarmouth', 'harpenden', 'ipswichuk', 
     'kingslynn', 'luton', 'maldon', 'norfolkuk', 'norwich', 'ayleigh', 'stalbans', 'sudburysuffolk', 'suffolk', 'watford', 'northernireland', 
     'Belfast', 'carrickfergus', 'derrylondonderry', 'lisburn', 'Newry', 'scotland', 'Gaidhlig', 'Scots', 'OutdoorScotland', 'scottishcycling', 
     'ScottishHistory', 'ScottishMusic', 'ScottishFootball', 'ScotlandPorn', 'scottishpolitics', 'Scottishproblems', 'ScotlandUnsigned', 
     'aberdeen', 'annan', 'arbroath', 'ayrshire', 'dundee', 'DumfriesAndGalloway', 'Edinburgh', 'eastkilbride', 'elginscotland', 'falkirk', 
     'fife', 'Glasgow', 'glencoe', 'inverness', 'irvinescotland', 'kettins', 'kilmarnock', 'lanarkshire', 'orkney', 'shetland', 'stirlingscotland', 
     'stornoway', 'westernisles', 'whitburn', 'Cymru', 'Wales', 'HistoryWales', 'abergavenny', 'abertillery', 'aberystwyth', 'bango', 'bridgend', 
     'builthwells', 'cardiff', 'flintshire', 'holyhead', 'newportSW', 'pembrokeshire', 'porthcawl', 'southwales', 'swansea', 'wrexham', 'isleofman', 
     'guernsey', 'jerseychannelislands', 'gunners', 'avfc', 'brfc', 'bwfc', 'AFCBournemouth', 'BrightonHoveAlbion', 'BristolCityFC', 'bluebirds', 
     'chelseafc', 'crystalpalace', 'derbycounty', 'Everton', 'FulhamFC', 'HuddersfieldTownFC', 'HullCity', 'itfc', 'LeedsUnited', 'lcfc', 
     'LiverpoolFC', 'MCFC', 'eddevils', 'Middlesbrough', 'MK_Dons', 'nufc', 'NorwichCity', 'nffc', 'PAFC', 'PortsmouthFC', 'superhoops', 'Urz', 
     'Redditch', 'sheffieldwednesday', 'SaintsFC', 'StokeCityFC', 'SAFC', 'swanseacity', 'coys', 'WBAfootball', 'Hammers', 'latics', 'WWFC', 
     'ScottishFootball', 'thedons', 'Glasgow_Celtic', 'CelticFC', 'PARS', 'PartickThistleFC', 'angersfc', 'stjohnstone', 'WelshPremierLeague', 
     'bluebirds', 'swanseacity', 'AlanPartridge', 'BeingHuman', 'blackmirro', 'doctorwho', 'SoupyTwist', 'thehou', 'theinbetweeners', 'itcrowd', 
     'Lifeonmars', 'merlinbbc', 'misfitstv', 'mitchellandwebb', 'theprisone', 'quiteinteresting', 'eddwarf', 'sherlock', 'ickygervais', 'topgea', 
     'torchwood', 'VicAndBob', 'bathuni', 'uob', 'brunel', 'cambridge_uni', 'cityuniversitylondon', 'durhamu', 'essexuni', 'Edinburgh_University', 
     'goldsmiths', 'imperial', 'kcl', 'kingstonu', 'lancasteruni', 'uol', 'leedsuniversity', 'leedsmet', 'lufbra', 'manchester_uni', 'uon', 
     'openuniversity', 'oxforduni', 'oxfordbrookes', 'queensbelfast', 'qmulandbarts', 'hul', 'standrews', 'universityofsussex', 'swanseauni', 
     'ucl', 'uea', 'universityofwarwick', 'uwe', 'universityofyork']
    '''

    #output_file = 'hdfs:///user/karkala/filtered_submissions_swiss_subreddits_full_corpus_with_header'
    #output_file = 'hdfs:///user/karkala/filtered_comments2007_swiss_subreddits_with_header'

    #output_file = 'hdfs:///user/karkala/filtered_submissions_europe_subreddits_full_corpus_with_header'
    output_file = 'hdfs:///user/karkala/filtered_comments2015_europe_subreddits_with_header'

    filt_df.write.format("com.databricks.spark.csv").option("header","true").save(output_file)
    sc.stop()