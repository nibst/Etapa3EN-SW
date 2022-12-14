
from src.data.Event import Event
from src.exception.no_invited_participants_exception import NoInvitedParticipantsException
from src.exception.invalid_date_exception import InvalidDateException
from datetime import date

#TODO, maybe do in a class?
def validate_event(event:Event):
    if __validate_invited_participants_in_private_event(event.get_visibility(),event.get_list_of_participants()) == False:
        raise NoInvitedParticipantsException("Event is private and no participants were invited")
    if __verify_event_end_after_start(event.get_start_date(),event.get_end_date()) == False:
        raise InvalidDateException("Event start date is after end date")
    if __validate_event_date(event.get_start_date()) == False:
        raise InvalidDateException("Event start date is in the past")
    if __validate_event_date(event.get_end_date()) == False:
        raise InvalidDateException("Event end date is in the past")
    if event.get_event_parent():
        if __verify_subevent_date_outside_of_event_period(event.get_event_parent(),event):
            raise InvalidDateException("Sub-Evento fora do período de tempo do evento")

def __verify_subevent_date_outside_of_event_period(event:Event,sub_event:Event):
    if event.get_start_date() >= sub_event.get_start_date() or event.get_start_date() >= sub_event.get_end_date():
        return True
    if event.get_end_date() <= sub_event.get_start_date() or event.get_end_date() <= sub_event.get_end_date():
        return True
def __verify_event_end_after_start(start:date,end:date):
    return start <= end

def __validate_event_date(date:date):
    return date >= date.today()

def __validate_invited_participants_in_private_event(visibility:bool,list_of_participants:list):
    if visibility == False:
        return len(list_of_participants) > 0
    else:
        return True
 