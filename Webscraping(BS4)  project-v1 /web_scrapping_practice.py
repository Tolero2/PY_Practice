# web scrapping cryptocurrency prices for personal investment analysis
# importing python inbuilt module for data mining and ingestion

from importlib.resources import path
from operator import index
from textwrap import indent
import pandas as pd
import requests
import json
# optimization for exceuting codes in a non symmetrical fashion
import asyncio
import os
# Importing the Beautiful soup module from the Beautiful soup v4(bs4) package
from bs4 import BeautifulSoup
# Azure EventHub py module for client, placeholder and error message
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azure.eventhub.exceptions import EventHubError


def scrapData():
    # request the webpage using the http get library
    lcw = requests.get('https://cryptowat.ch/assets')
    # parse the content into an html parser in beautifulsoup
    soup = BeautifulSoup(lcw.content,
                         'html.parser')
    # print(soup.prettify()) #look at the content of the response in html indexed K=>V format with V as Json.

    # the content is stored in a json within a tag script format to separate the section of the webpage/ so it has to be stripped off the tag and isolated using the below
    data = soup.find('script', id="__NEXT_DATA__", type="application/json")

    # After isolating the section of the script you want; you load the content of the isolated script into a python JSON
    coin_data = json.loads(data.contents[0])

    # you can now isolate the key Object for your data scrapping;
    listings = coin_data['props']['initialProps']['pageProps']['data']
    # Incorrect perfomance data being pulled which has caused a limitation on the type of analysis that was intended for this pipeline.
    # initial algo is to create a variable x = 0, then a loop to iterate a counting number 0-99 and store the value in x, use the value as the index listings[x].
    # perfomance= listings[1]["performance"]

    # templates to store my table schema attribute with values stored in list array
    position = []
    name = []
    symbol = []
    price = []
    volume = []
    marketcap = []
    # assigning the attributes(nested objects) of the object(listings) from Beautifulsoup to the table schema array( using a )
    for i in listings:
        position.append(i['rank'])
        name.append(i['name'])
        symbol.append(i['symbol'])
        price.append(i['price'])
        volume.append(i['volume'])
        marketcap.append(i['marketcap'])
    # print(json.dumps(symbol))

    # importing this array into panda data frame(df)
    # using a spilt method for the columns by defining the key and value separately

    df = pd.DataFrame(
        columns=['RANK', 'NAME', 'SYMBOL', 'PRICE($)', 'VOLUME', 'MARKETCAP'])
    df['RANK'] = position
    df['NAME'] = name
    df['SYMBOL'] = symbol
    df['PRICE($)'] = price
    df['VOLUME'] = volume
    df['MARKETCAP'] = marketcap


    #Using the PATH package to instantiate path and  define directories/ filename
    from pathlib import Path

    file_path= Path('[YOUR DEGINATED DIRECTORY PATH/FILENAME.CSV]')
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # converting the data frame to dictionary pair value in order to parse easily to Azure event hub since it only takes data type of str or array
        # df_eventhub = df.to_dict(file_path, 'records')

   #Convert the data frame to a csv file and save down to designated path
   df_eventhub = df.to_csv ( file_path, index=False)
    return (df_eventhub)

#
print(scrapData())

# EVENT HUB EVENT STREAMER for your SMB Transfer
# # connecting to Azure cloud via Access point already created in the eventhub instance for this application with send/receive permission
# connection_str = '[YOUR STREAM ENDPOINT];EntityPath=[YOUR EVENT NAME]'
# eventhub_namespace = '[YOUR EVENT HUB NAMESPACE]'  # the eventhub namespace
# eventhub_name = '[YOUR EVENT HUB NAME]'  # the instance(event) name

# # Create a producer client to send messages to the event hub.
# # Specify a credential that has correct role assigned to access
# # event hubs namespace and the event hub name.
# #while True:
# async def run():
#         # to faciltate that it will always run
#         while True:
#             # adding delay to between loop(reload)
#             await asyncio.sleep(5)
#             # Create a producer client to send messages to the event hub.
#             # Specify a connection string to your event hubs namespace and
#             # the event hub name.
#             producer = EventHubProducerClient.from_connection_string(
#                 conn_str=connection_str, eventhub_name=eventhub_name
#             )
#             async with producer:
#                 # Create a batch.
#                 event_data_batch = await producer.create_batch()

#                 # Add events to the batch.
#                 event_data_batch.add(EventData(json.dumps(scrapData())))

#                 # Send the batch of events to the event hub.
#                 await producer.send_batch(event_data_batch)
# asyncio.run(run())

#     # #looping to keep the connection running and also create a way to end the loop
#     # loop = asyncio.get_event_loop()
#     # try:
#     #     asyncio.ensure_future(run())
#     #     loop.run_forever()
#     # except KeyboardInterrupt:
#     #      pass
#     # finally:
#     #     print('Closing loop now')
#     #     loop.close()



