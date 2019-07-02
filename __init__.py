# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.skills.context import adds_context, removes_context

from DPIClass import DPI

class EvolucareSkill(MycroftSkill):
    def __init__(self):
        super(EvolucareSkill, self).__init__(name="EvolucareSkill")
        self.last_tension = 0


    @intent_handler(IntentBuilder("TensionMesure")
                    .require("mesure")
                    .require("tension"))
    @adds_context('TensionProtocol')
    def handle_tension_question_mesure(self, message):
        self.speak_dialog('tension.mesure.protocol')
        
        

    @intent_handler(IntentBuilder("TensionQuestion")
                    .require("tension"))
    @adds_context('TensionContext')
    def handle_tension_question(self, message):
        self.speak_dialog('tension.question', expect_response=True)
         
         
         
    @intent_handler(IntentBuilder("TensionQuestionDecline")
                    .require("negation")
                    .require("TensionContext")
                    .build())
    @removes_context('TensionContext')
    def handle_tension_question_decline(self, message):
        self.speak_dialog('tension.question.decline')
    
    
    
    @intent_handler(IntentBuilder("TensionProtocolIntent")
                    .require("acceptation")
                    .require("TensionContext")
                    .build())
    @adds_context('TensionProtocol')
    @removes_context('TensionContext')
    def handle_tension_question_accept(self, message):
        self.speak_dialog('tension.mesure.protocol')
        
         
         
    @intent_handler(IntentBuilder("TensionCalculIntent")
                    .require("pret")
                    .require("TensionProtocol")
                    .optionally("negation")
                    .build())
    def handle_tension_calcul_intent(self, message):
        neg = message.data.get("negation")
        if not neg:
            self.TensionCalulate()
        else:
            self.speak_dialog("tension.protocol.wait")



    @removes_context('TensionProtocol')   
    def TensionCalulate(self):
        self.speak_dialog('tension.calcul')
        # TO DO : calculate and return tension
        self.last_tension = 0
        self.speak_dialog("tension.response", data={"tension": self.last_tension} )





    #@intent_handler(IntentBuilder(""))
    #def handle_default_intent(self, message):
        #self.speak_dialog("response", data={"response": message.data["utterance"]})
        

    #@intent_handler(IntentBuilder("").require("Count").require("Dir"))
    #def handle_count_intent(self, message):
        #if message.data["Dir"] == "up":
            #self.count += 1
        #else:  # assume "down"
            #self.count -= 1
        #self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False



def create_skill():
    return EvolucareSkill()
