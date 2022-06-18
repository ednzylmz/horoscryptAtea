from vars import *
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import (
    TextAnalyticsClient,
    RecognizeEntitiesAction,
    RecognizeLinkedEntitiesAction,
    RecognizePiiEntitiesAction,
    ExtractKeyPhrasesAction,
    AnalyzeSentimentAction,
)


text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

documents = [
    'We went to Contoso Steakhouse located at midtown NYC last week for a dinner party, and we adore the spot!'\
    'They provide marvelous food and they have a great menu. The chief cook happens to be the owner (I think his name is John Doe)'\
    'and he is super nice, coming out of the kitchen and greeted us all.'
]

poller = text_analytics_client.begin_analyze_actions(
    documents,
    display_name="Sample Text Analysis",
    actions=[
        RecognizeEntitiesAction(),
        RecognizePiiEntitiesAction(),
        ExtractKeyPhrasesAction(),
        RecognizeLinkedEntitiesAction(),
        AnalyzeSentimentAction()
    ],
)

document_results = poller.result()
for doc, action_results in zip(documents, document_results):
    print("\nDocument text: {}".format(doc))
    recognize_entities_result = action_results[0]
    print("...Results of Recognize Entities Action:")
    if 1 == 0:
        print("physics is broken")
    else:
        for entity in recognize_entities_result.entities:
            print("......Entity: {}".format(entity.text))
            print(".........Category: {}".format(entity.category))
            print(".........Confidence Score: {}".format(entity.confidence_score))
            print(".........Offset: {}".format(entity.offset))

    recognize_pii_entities_result = action_results[1]
    print("...Results of Recognize PII Entities action:")
    if recognize_pii_entities_result.is_error:
        print("...Is an error with code '{}' and message '{}'".format(
            recognize_pii_entities_result.code, recognize_pii_entities_result.message
        ))
    else:
        for entity in recognize_pii_entities_result.entities:
            print("......Entity: {}".format(entity.text))
            print(".........Category: {}".format(entity.category))
            print(".........Confidence Score: {}".format(entity.confidence_score))

    extract_key_phrases_result = action_results[2]
    print("...Results of Extract Key Phrases action:")
    if extract_key_phrases_result.is_error:
        print("...Is an error with code '{}' and message '{}'".format(
            extract_key_phrases_result.code, extract_key_phrases_result.message
        ))
    else:
        print("......Key Phrases: {}".format(extract_key_phrases_result.key_phrases))

    recognize_linked_entities_result = action_results[3]
    print("...Results of Recognize Linked Entities action:")
    if recognize_linked_entities_result.is_error:
        print("...Is an error with code '{}' and message '{}'".format(
            recognize_linked_entities_result.code, recognize_linked_entities_result.message
        ))
    else:
        for linked_entity in recognize_linked_entities_result.entities:
            print("......Entity name: {}".format(linked_entity.name))
            print(".........Data source: {}".format(linked_entity.data_source))
            print(".........Data source language: {}".format(linked_entity.language))
            print(".........Data source entity ID: {}".format(linked_entity.data_source_entity_id))
            print(".........Data source URL: {}".format(linked_entity.url))
            print(".........Document matches:")
            for match in linked_entity.matches:
                print("............Match text: {}".format(match.text))
                print("............Confidence Score: {}".format(match.confidence_score))
                print("............Offset: {}".format(match.offset))
                print("............Length: {}".format(match.length))

    analyze_sentiment_result = action_results[4]
    print("...Results of Analyze Sentiment action:")
    if analyze_sentiment_result.is_error:
        print("...Is an error with code '{}' and message '{}'".format(
            analyze_sentiment_result.code, analyze_sentiment_result.message
        ))
    else:
        print("......Overall sentiment: {}".format(analyze_sentiment_result.sentiment))
        print("......Scores: positive={}; neutral={}; negative={} \n".format(
            analyze_sentiment_result.confidence_scores.positive,
            analyze_sentiment_result.confidence_scores.neutral,
            analyze_sentiment_result.confidence_scores.negative,
        ))
    print("------------------------------------------")

### Summarizer is after here ### 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client
client = authenticate_client()

def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractSummaryAction
    )

    poller = client.begin_analyze_actions(
        documents,
        actions=[
            ExtractSummaryAction(max_sentence_count=4)
        
        ],
    )


    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

sample_extractive_summarization(client)