from datetime import datetime
from unicodedata import category
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
    endpoint= summary_endpoint,
    credential=AzureKeyCredential(summary_key),
)

# make this vtt
import webvtt

transcript = [] # used for reminders - entity matching at the end of this file
documents = []
txt = ''

i = 0
for caption in webvtt.read('./artifacts/output.vtt'):
    transcript.append(caption.text + '')
    if i < 45:
        txt += caption.text
    else:
        documents.append(txt)
        txt = ''
        i = 0
    
    i += 1

documents.append(txt)

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

# REMINDERS
dateTimeEntities = []
eventEntities = []

document_results = poller.result()
for doc, action_results in zip(documents, document_results):
    print("\nDocument text: {}".format(doc))
    recognize_entities_result = action_results[0]
    print("...Results of Recognize Entities Action:")

    for entity in recognize_entities_result.entities:
        if entity.confidence_score > 0.799 and entity.category != 'Quantity':
            print("......Entity: {}".format(entity.text))
            print(".........Category: {}".format(entity.category))
            print(".........Confidence Score: {}".format(entity.confidence_score))
            print(".........Offset: {}".format(entity.offset))

        if entity.category == 'DateTime':
            dateTimeEntities.append(entity)
        elif entity.category == 'Event':
            eventEntities.append(entity)


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
    ta_credential = AzureKeyCredential(summary_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=summary_endpoint, 
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


print('------------------------------')
print('------------------------------')
print('------------------------------')

# print(dateTimeEntities)
# print('all transciprt text', transcript)

# remove duplicate dateTimeEntities
entities = []

for e in eventEntities:
    entities.append(e.text.lower())

eventEntities = list(set(entities))

entities.clear()

for e in dateTimeEntities:
    entities.append(e.text.lower())

dateTimeEntities = list(set(entities))

# remove 'now' from the list
# dateTimeEntities.remove('now')
# dateTimeEntities.remove('a month')
# dateTimeEntities.remove('a year')
# dateTimeEntities.remove('a month, a year')
# dateTimeEntities.remove('2024')
#TODO: Add more...

import re

reminders = {}
events = {}

for line in transcript:
    for entity in dateTimeEntities:
        if re.search(r"\b"+entity+r"\b", line):
            if entity not in reminders:
                reminders[entity] = []

            reminders[entity].append(line)
    
    for entity in eventEntities:
        if re.search(r"\b"+entity+r"\b", line):
            if entity not in events:
                events[entity] = []

            events[entity].append(line)
            
for reminder in reminders:
    print(reminder, reminders[reminder])

# for event in events:
    # print(event, events[event])
