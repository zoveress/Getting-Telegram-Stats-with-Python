import logging
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
import config as cfg
import datetime
import pygsheets

def _initiate_client_connection(telegramchannel):
    api_id                              = cfg.API_ID
    api_hash                            = cfg.API_HASH
    client                              = TelegramClient(f'./{telegramchannel}_session_name', api_id, api_hash)
    return client

def _get_stats(telegramchannel):
    client  = _initiate_client_connection(telegramchannel)
    with client:
        stats = client.get_stats(telegramchannel)
        current_members     = stats.members.current
        previous_members    = stats.members.previous
        current_viewers     = stats.viewers.current
        previous_viewers    = stats.viewers.previous
        current_messages    = stats.messages.current
        previous_messages   = stats.messages.previous
        current_posters     = stats.posters.current
        previous_posters    = stats.posters.previous
    return current_members, previous_members, current_viewers, previous_viewers, current_messages, previous_messages, current_posters, previous_posters

def _main(telegramchannel):    
    current_members, previous_members, current_viewers, previous_viewers, current_messages, previous_messages, current_posters, previous_posters = _get_stats(telegramchannel)
    print (f"current_members: {current_members} previous_members: {previous_members}")
    print (f"current_viewers: {current_viewers} previous_viewers: {previous_viewers}")
    print (f"current_messages: {current_messages} previous_messages: {previous_messages}")
    print (f"current_posters: {current_posters} previous_posters: {previous_posters}")

if __name__ == "__main__":
    telegramchannel = cfg.CHANNEL
    logfile = f'{cfg.LOG_PATH}/telegramListener_{telegramchannel}.log'
    logging.basicConfig(level=logging.INFO, filename=logfile, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    timestamp = datetime.datetime.now()
    try:
        _main(telegramchannel)
    except Exception as ex:
        logging.error(f"Error: {ex}")
        logging.exception('Got exception on main handler')   
