from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification
from model_query_service import ModelQueryService

class TextProcessingService:
    def __init__(self):
        self.model_query_service = ModelQueryService()
        self.waiting_for_question = False
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')
        self.sentiment_pipeline = pipeline('sentiment-analysis', model=self.model, tokenizer=self.tokenizer)

    def parse_command(self, text):
        """
        Uses BERT model to parse the text and extract the command and its content.
        """
        try:
            # Sentiment analysis
            sentiment_result = self.sentiment_pipeline(text)
            sentiment = sentiment_result[0]['label']
            
            # Custom logic to decide on command based on NLP analysis
            if sentiment == 'positive' and 'schedule meeting' in text:
                return 'schedule_meeting', text
            elif sentiment == 'neutral' and 'take note' in text:
                if 'transcription' in text:
                    return 'transcription notes', text
                elif 'summary' in text:
                    return 'summary notes', text
                elif 'outline' in text:
                    return 'outline notes', text
                
            elif sentiment == 'neutral' and 'send email' in text:
                return 'send_email', text
            # Check for 'question' keyword
            elif 'question' in text:
                self.waiting_for_question = True
                return 'prepare_for_question', 'Ready for your question.'

            # Handle question querying
            elif self.waiting_for_question:
                self.waiting_for_question = False
                return 'query_model', self.model_query_service.query_model(text)

            return 'unknown', text
        
        except Exception as e:
            print(f"Error: {e}")
            return 'error', str(e)
