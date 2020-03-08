from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


ENTITY_TYPES = ["UNKNOWN", "PERSON", "LOCATION", "ORGANIZATION", "EVENT", "WORK_OF_ART", "CONSUMER_GOOD",
                "OTHER"]
IMP_ENTITY_IDX = [1, 2, 3, 4, 5, 6]
REALLY_IMP_ENTITY_IDX = [1, 2, 3, 4]

class GoogleLanguage(object):

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def get_entities(self, text):
        words = []
        document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT}
        response = self.client.analyze_entities(document=document, encoding_type=enums.EncodingType.UTF8)
        for entity in response.entities:
            print(u"Representative name for the entity: {}".format(entity.name))
            print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
            print(u"Salience score: {}".format(entity.salience))

            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{}: {}".format(metadata_name, metadata_value))
            
            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
                words.append(mention.text.content)
                print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))
        return words

    def get_entities_sentiment(self, text):
        document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT}
        response = self.client.analyze_sentiment(document, encoding_type=enums.EncodingType.UTF8)
        
        for sentence in response.sentences:
            print(u"Sentence Sentiment Score: {}".format(sentence.sentiment.score))
            print(u"Sentence Sentiment Magnitude: {}".format(sentence.sentiment.magnitude))
        
        #return response.sentiment

    # def get_document_sentiment(self, text):
    #     document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT}
    #     sentiment = self.client.analyze_sentiment(document=document, encoding_type=enums.EncodingType.UTF8).document_sentiment

    #     print(u"Document Sentiment Score: {}".format(sentiment.document_sentiment.score))
    #     print(u"Document Sentiment Magnitude: {}".format(sentiment.document_sentiment.magnitude))

    #     #return sentiment

# TEXT = "Trump thinks that coronavirus is a hoax created by the democrats"
# list_of_entities = (GoogleLanguage().get_entities(TEXT))
# string_of_entities = ', '.join(list_of_entities)

# print(string_of_entities)