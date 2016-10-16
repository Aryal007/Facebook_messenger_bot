import fbchat
import aiml
import os

class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=False, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        user_info = bot.getUserInfo(author_id)
        user_name = user_info['name']

        print("%s: %s"%(user_name, message))
        response = kernel.respond(message)

        #if you are not the author, echo
        if str(author_id) != str(self.uid):
            self.send(author_id,"Bot Says: "+response)

fbid = raw_input("Enter facebook id: ")
password = raw_input("Enter facebook password: ")

bot = EchoBot(fbid, password)
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "./aiml/*", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

#Set bot parameters, some are here in example
kernel.setBotPredicate(name="name", value="Jarvis")
kernel.setBotPredicate(name="location", value="Kathmandu")
kernel.setBotPredicate(name="gender", value="robo-man")
kernel.setBotPredicate(name="master", value="Aryal Bibek")
kernel.setBotPredicate(name="botmaster", value="master")
kernel.setBotPredicate(name="birthday", value="September 23 2016")
kernel.setBotPredicate(name="birthplace", value="My master's PC")
kernel.setBotPredicate(name="favouritefood", value="Transistors")
kernel.setBotPredicate(name="favouritemovie", value="Star Treks")
kernel.setBotPredicate(name="favouriteband", value="Imagine Dragon")
kernel.setBotPredicate(name="favouritebook", value="You can win")
kernel.setBotPredicate(name="favouritecolor", value="Black")
kernel.setBotPredicate(name="friends", value="I have a lot of friends")
kernel.setBotPredicate(name="favouritesong", value="PPAP")
kernel.setBotPredicate(name="phylum", value="Cyborg")
kernel.setBotPredicate(name="domain", value="Super Robot")
kernel.setBotPredicate(name="genus", value="Android")
kernel.setBotPredicate(name="kingdom", value="SuperBot")
kernel.setBotPredicate(name="nationality", value="Nepali")
kernel.setBotPredicate(name="country", value="Nepal")
kernel.setBotPredicate(name="city", value="Kathmandu")
kernel.setBotPredicate(name="state", value="Bagmati")

# # kernel now ready for use

bot.listen()